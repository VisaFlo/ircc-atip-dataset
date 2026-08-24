"""Classify thread quality: did IRCC actually answer, deflect, or is the text torn?

``classify(thread)`` returns ``"answered"``, ``"deflected"``, or ``"partial"``
for a thread dict produced by :mod:`pipeline.split_threads`.

Approach: many SUBSTANTIVE answers carry the same webform-redirect footer as
pure deflections, so signal presence alone cannot decide. Instead, known
boilerplate blocks (greeting, case-specific disclaimer, redirect sentences,
support-channel list, signature) are stripped and the REMAINDER is measured:
enough residual text means a real answer; little residue plus a refusal/
redirect signal means the reply was essentially only boilerplate.
"""
from __future__ import annotations

import re

# Threads whose stripped answer keeps at least this many characters carry
# substantive guidance. Post-fix corpus measurement (1,374 answers, 2026-08):
# pure-boilerplate replies strip to <= 182 chars even with worst-case OCR
# debris; the last redirect-only reply sits at 199; genuine short answers
# start at 201 (a portal-enrolment confirmation) with the first unambiguous
# guidance at 214 ("Yes, as long as the LMIA is still valid..."). 200 keeps
# every observed boilerplate reply below and every genuine answer above. The
# 199/201 margin is thin but inherent: that band is a continuum of
# pointer-style replies, not a real gap in the data.
MIN_SUBSTANCE_CHARS = 200

# Marker injected by the OCR stage when a page could not be read.
OCR_ERROR_MARKER = "OCR_ERROR"

# --------------------------------------------------------------- boilerplate
# Stripped before measuring substance. Comments quote the real source text
# (A-2025-85182 unless noted). Patterns are applied to whitespace-collapsed
# text, so plain spaces match across OCR line breaks; accents are classed
# because OCR mangles them.

BOILERPLATE_PATTERNS = [
    # "Hello," / "Good day," / "Bonjour,"
    r"\b(?:Hello|Good day|Good morning|Good afternoon|Bonjour)\s*[,.!]?",
    # "Thank you for contacting the Immigration Representatives Mailbox."
    # (also seen as "... Representatives Inbox.")
    r"Thank you for contacting the Immigration Representatives?\s?(?:Mailbox|Inbox)[,.]?",
    # "Merci d'avoir contacté la boîte aux courriels pour les représentants en
    # immigration."
    r"Merci d['’]avoir contact[ée] la bo[iî]te aux courriels pour les "
    r"repr[ée]sentants en immigration[,.]?",
    # "Please note that we do not answer case specific inquiries."
    r"Please note that we do not answer case[- ]specific inquiries[,.]?",
    # "Please note that this mailbox is intended for general guidance and does
    # not provide responses to case-specific inquiries but have provided the
    # following information as guidance."
    r"Please note that this mailbox is intended for general guidance and does "
    r"not provide responses to case-? ?specific inquiries(?: but have provided "
    r"the following information as guidance)?[,.]?",
    # French twin: "Veuillez noter que cette boîte aux lettres est destinée à
    # fournir des conseils généraux et ne fournit pas de réponses à des
    # demandes spécifiques à un cas, mais a fourni les informations suivantes
    # comme conseils."
    r"Veuillez noter que cette bo[iî]te aux lettres est destin[ée]e [àa] fournir "
    r"des conseils g[ée]n[ée]raux et ne fournit pas de r[ée]ponses [àa] des demandes "
    r"sp[ée]cifiques [àa] un cas(?:, mais a fourni les informations suivantes "
    r"comme cons\w*)?[,.]?",
    # "If you have case specific questions about a file, you are encouraged to
    # submit the IRCC Web form." — OCR often tears off the leading clause;
    # A-2025-85182_00000 shows "... submit a Webform at: [http://...](...)".
    r"(?:If you have case specific )?questions about a file, you are encouraged "
    # OCR drops the I of IRCC ("submit the RCC Web form"), hence [Il]?RCC.
    r"to submit (?:the |a )?(?:[Il]?RCC )?Web ?form(?: at ?: ?\S+)?[-.]?(?:Canada\.ca\S*)?\.?",
    # "Please see our response to your question." and the "***" separators
    # around it.
    r"Please see our response to your question\.?",
    r"\*+",
    # "For updates on applications outside of normal processing times, requests
    # for expedited processing of an application, or if clients wish to report
    # important changes to their application information, please fill out the
    # IRCC Web form-Canada.ca_or you can use existing client support channels
    # available on our website to communicate with us."
    r"For updates on applications outside of normal processing times, requests "
    r"for expedited processing of an application, or if clients wish to report "
    r"important changes to their application information[,.]?",
    r"please fill out the [Il]?RCC Web ?form[-\s]?Canada\.ca\S*",
    r"(?:_?or )?you can use existing client support channels(?: available on our "
    r"website to communicate with us)?\.?",
    r"available on our website to communicate with us\.?",  # torn tail of the above
    # "Please note that, in the future, for case-specific enquiries you must
    # use existing client support channels available on our website ..."
    r"Please note that, in the future, for case-specific enquiries you must use "
    r"existing client support channels\.?",
    # "Please note this request is outside our scope to assist with and no
    # further action will be taken including forwarding emails to any
    # team/department or any further correspondence."
    r"Please note th(?:is|at this) request is outside our scope to assist with "
    r"and no further action will be taken including forwarding emails to any "
    r"team ?/ ?department or any further correspondence\.?",
    # Torn tail of the refusal above — OCR often severs the sentence head,
    # leaving "and no further action will be taken including forwarding
    # emails to any team/department or any further correspondence." dangling
    # after another stripped block (A-2025-81965_00760).
    r"(?:and )?no further action will be taken including forwarding emails "
    r"to any team ?/ ?department or any further correspondence\.?",
    # "The Immigration Representative inbox is responsible for general
    # enquiries received from authorized immigration representatives and
    # lawyers with respect to general procedures and operational policies for
    # the various immigration lines of business including permanent residence,
    # temporary residence, asylum, citizenship and program integrity."
    r"The Immigration Representatives? inbox is responsible for general "
    r"enquiries received from authorized immigration representatives and "
    r"lawyers with respect to general procedures and operational policies for "
    r"the various immigration lines of business including",
    r"(?:permanent residence, temporary )?residence, asylum, citizenship and "
    r"program integrity\.?",
    # Support-channel list items ("- Use the IRCC Web form: o * to report a
    # technical issue related to IRCC online services, o* to request for
    # expedited processing of an application, ...").
    r"Use the IRCC Web form ?:",
    r"[o0] ?\*? ?to report a technical issue related to IRCC online services[,.]?",
    r"[o0] ?\*? ?to request for expedited processing of an application[,.]?",
    r"[o0] ?\*? ?if your application has exceeded normal processing times[,.]?",
    r"[o0] ?\*? ?to report important changes or an emergency situation\.?",
    # "- Telephone: IRCC Client Support Centre 1-888-242-2100 (in Canada only)."
    r"Telephone ?: ?IRCC Client Support Centre 1-888-242-2100 \(in Canada only\)\.?",
    # "- For general enquiries on programs administered by IRCC: o visit the
    # Help Centre on our website."
    r"For general enquiries on programs administered by IRCC ?: ?"
    r"(?:[o0] visit the Help Centre on our website\.?)?",
    r"[o0] visit the Help Centre on our website\.?",
    # "- To obtain the status of your application: o visit our check
    # application status webpage."
    r"To obtain the status of your application ?: ?"
    r"(?:[o0] visit our check application status webpage\.?)?",
    r"[o0] visit our check application status webpage\.?",
    # "- If you are experiencing technical issues with online applications:
    # o visit What do I do if I have technical problems when applying online?
    # o to report a technical problem: Technical"
    r"If you are experiencing technical issues with online applications ?:",
    r"[o0] visit What do I do if I have technical problems when applying online ?\??",
    r"[o0] to report a technical problem ?: ?Technical\.?",
    # French out-of-scope refusal (A-2025-85182_00040): "Veuillez noter que
    # cette demande ne relève pas de notre compétence et aucune autre mesure ne
    # sera prise, y compris le transfert d'e-mails à une équipe/département
    # quelconque ou toute autre correspondance."
    r"Veuillez noter que cette demande ne rel[eè]ve pas de notre comp[ée]tence et "
    r"aucune autre mesure ne sera prise, y compris le transfert d['’]e-mails [àa] "
    r"une [ée]quipe ?/ ?d[ée]partement quelconque ou toute autre correspondance\.?",
    # "La boîte électronique pour les représentants en immigration est
    # responsable des demandes de renseignements générales reçues des
    # représentants autorisés en immigration et des avocats concernant les
    # procédures générales et les politiques opérationnelles pour les
    # différents secteurs d'activité de l'immigration, y compris la résidence
    # permanente, la résidence temporaire, l'asile, la citoyenneté et
    # l'intégrité des programmes."
    r"La bo[iî]te [ée]lectronique pour les repr[ée]sentants en immigration est "
    r"responsable des demandes de renseignements g[ée]n[ée]rales re[çc]ues des "
    r"repr[ée]sentants autoris[ée]s en immigration et des avocats concernant les "
    r"proc[ée]dures g[ée]n[ée]rales et les politiques op[ée]rationnelles pour les "
    r"diff[ée]rents secteurs d['’]activit[ée] de l['’]immigration, y compris la "
    r"r[ée]sidence permanente, la r[ée]sidence temporaire, l['’]asile, la "
    r"citoyennet[ée] et l['’]int[ée]grit[ée] des programmes\.?",
    # "Si vous avez des questions spécifiques sur un dossier, nous vous
    # encourageons à soumettre un Formulaire Web d'lRCC-Canada.ca" (OCR reads
    # the I of IRCC as l).
    r"Si vous avez des questions sp[ée]cifiques sur un dossier, nous vous "
    r"encourageons [àa] soumettre un",
    r"Formulaire Web d['’][lI]?RCC[-\s]?(?:Canada\.ca\S*)?",
    r"Veuillez consulter notre r[ée]ponse [àa] votre question\.?",
    # "Veuillez noter qu'à l'avenir, pour les demandes spécifiques à un cas,
    # vous devrez utiliser les canaux d'assistance client existants disponibles
    # sur notre site Web pour communiquer avec nous."
    r"Veuillez noter qu['’][àa] l['’]avenir, pour les demandes sp[ée]cifiques [àa] un "
    r"cas, vous devrez utiliser les canaux d['’]assistance client existants "
    r"disponibles sur notre site Web pour communiquer avec nous\.?",
    # French support-channel list ("- Utilisez le formulaire Web d'IRCC : o *
    # pour signaler un problème technique lié aux services en ligne d'IRCC, ...").
    r"Utilisez le(?: formulaire Web d['’]IRCC)? ?:",
    r"[o0] ?\*? ?pour signaler un probl[eè]me technique li[ée] aux services en ligne d['’]IRCC[,.]?",
    r"[o0] ?\*? ?pour demander le traitement acc[ée]l[ée]r[ée] d['’]une demande[,.]?",
    r"[o0] ?\*? ?si votre demande a d[ée]pass[ée] les d[ée]lais normaux de traitement[,.]?",
    r"[o0] ?\*? ?pour signaler des changements importants ou une situation d['’]urgence\.?",
    r"[o0] visitez le centre d['’]aide sur notre site Web\.?",
    r"Pour obtenir le statut de votre candidature ?: ?"
    r"(?:[o0] visitez notre page Web de v[ée]rification de l['’][ée]tat de la demande\.?)?",
    r"Si vous rencontrez des probl[eè]mes techniques avec les applications en ligne ?:",
    r"[o0] pour signaler un probl[eè]me technique ?: ?Techni(?:que|cal)\.?",
    # Signoffs: "We hope this information is of assistance." / "We hope you
    # find this information useful." / "Thank you kindly, The Immigration
    # Representatives Mailbox" / "Sincerely, Immigration Re..." / "Cordialement,"
    r"We hope (?:this|you find this) information (?:is of assistance|useful)[,.]?",
    r"Thank you(?: kindly)?[,.]?",
    r"Sincerely[,.]?",
    r"Cordialement[,.]?",
    # "La boîte électronique pour les représentants en immigration" (French
    # signature line).
    r"La bo[iî]te [ée]lectronique pour les repr[ée]sentants en immigration[,.]?",
    r"(?:The )?Immigration Representatives?\s?(?:Mailbox|Inbox)[,.]?",
    # Outlook header residue glued into bodies: "Categories: Case Specific
    # Request" / "Case Specific Request Categories:" / "Categories: Awaiting
    # Credentials" (A-2025-81965).
    r"(?:Case Specific Request )?Categories ?: ?(?:Case Specific Request|Awaiting Credentials)?",
    # OCR-garbled sender line residue: "Immigraton Representatives /
    # Représentants immigration (IRCC)", "mmmmgtauon nepresenauves /
    # neprésentants immigration (IRCC)", "... (IRCC) Attachments:".
    r"[A-Za-zÀ-ÿ:,. ]{0,60}/ ?[A-Za-zÀ-ÿ]{0,25} ?immigration ?\(I?RCC\)(?: Attachments ?:)?",
    # Tracking stamps glued into bodies: "(AB-2025-269) - Due Nov 29/25",
    # "REP-B-2025-2095 - Due 28-Nov-25", "2025-294) Due 26 Nov 2025".
    # A bare "20xx-xxxx" is only a stamp with a code prefix, a closing paren,
    # or a following "Due" — never eat year ranges like "2024-2026
    # Immigration Levels Plan".
    r"\(?[A-Z]{2,4}-B?-? ?20\d{2}-\d{3,4}\)?",
    r"\(?20\d{2}-\d{3,4}\)",
    r"20\d{2}-\d{3,4}(?=,? ?-? ?Due\b)",
    r"-? ?Due,? ?\d{0,2}[- ]?[A-Za-z]{3,9}[- .,]?\d{0,2},? ?(?:20)?\d{2}(?:/\d{2})?",
]

_BOILERPLATE_RES = [re.compile(p, re.IGNORECASE) for p in BOILERPLATE_PATTERNS]

# ---------------------------------------------------------------- signals
# Refusal/redirect fingerprints. Presence alone NEVER deflects (substantive
# answers carry them as footers); they only decide low-substance replies.
DEFLECTION_SIGNAL_PATTERNS = [
    # "we do not answer case specific inquiries"
    r"we do not answer case[- ]specific",
    # "does not provide responses to case-specific inquiries"
    r"does not provide responses to case-? ?specific inquiries",
    # "this request is outside our scope to assist with"
    r"outside our scope",
    r"no further action will be taken",
    # "cette demande ne relève pas de notre compétence"
    r"ne rel[eè]ve pas de notre comp[ée]tence",
    # redirect-only bodies
    r"please fill out the [Il]?RCC Web ?form",
    r"client support channels",
    r"available on our website to communicate with us",
    r"Client Support Centre",
    # torn fragments of the scope blurb
    r"residence, asylum, citizenship and program integrity",
    r"citoyennet[ée] et l['’]int[ée]grit[ée] des programmes",
]

_DEFLECTION_SIGNAL_RES = [re.compile(p, re.IGNORECASE) for p in DEFLECTION_SIGNAL_PATTERNS]


def strip_boilerplate(text: str) -> str:
    """Remove known boilerplate blocks and collapse whitespace (the substance).

    Two passes: stripping one block can splice a neighbouring block back into
    matchable shape (e.g. removing the "***" separators rejoins a sentence the
    OCR tore apart), so a single pass under-strips.
    """
    text = re.sub(r"\s+", " ", text)
    for _ in range(2):
        for rx in _BOILERPLATE_RES:
            text = rx.sub(" ", text)
        text = re.sub(r"\s+", " ", text)
    return text.strip()


def classify(thread: dict) -> str:
    """Label a split_threads thread dict: "answered" | "deflected" | "partial"."""
    if OCR_ERROR_MARKER in (thread.get("raw") or ""):
        return "partial"
    answer = thread.get("answer")
    if not answer or not answer.strip():
        return "partial"
    substance = strip_boilerplate(answer)
    if len(substance) >= MIN_SUBSTANCE_CHARS:
        return "answered"
    # Collapse whitespace before signal search: OCR wraps phrases across
    # lines ("we do not answer case-\nspecific inquiries").
    flat = re.sub(r"\s+", " ", answer)
    if any(rx.search(flat) for rx in _DEFLECTION_SIGNAL_RES):
        return "deflected"
    return "partial"
