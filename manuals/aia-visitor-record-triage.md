# Algorithmic Impact Assessment: Visitor Record Triage (10p)

> Source: IRCC record released under the Access to Information Act. published by IRCC (open.canada.ca).
> Text below is local-OCR output of the scanned release and carries OCR noise; the release PDF is authoritative.

---

Algorithmic Impact Assessment Results
Version: 0.9.1

Project Details
1. Name of Respondent
Various Stakeholders at IRCC

2. Job Title
N/A

3. Department
Citizenship and Immigration (Department of)

4. Branch
Various Branches at IRCC

5. Project Title
Advanced Analytics Triage of Visitor Record Applications

6. Project ID from IT Plan
N/A

7. Departmental Program (from Department Results Framework)
Visitors

8. Project Phase
Implementation                                                                       [ Points: 0 ]

9. Please provide a project description:
This project seeks to streamline the eligibility assessment for all visitor record
applications in order to help IRCC decision-makers process applications more
efficiently. The advanced data analytics system identifies routine applications
for streamlined processing. When the system finds these applications, it can
decide that an applicant is eligible, before sending the file to an officer to
decide if the applicant remains admissible to Canada and make the final
decision. To do this, it uses a mix of rules developed with IRCC officers and
rules generated through machine learning based on previous IRCC case data.
All rules are assessed for potential bias or discrimination.

For all other cases that are not considered routine, the tool helps to sort and
assign cases to officers for manual review and decisions based on their level
of complexity, using rules and criteria developed with IRCC officers. This
means that these cases will be processed using the same process that was
used before IRCC began using this new system. It will also provide case
annotations, or notes for officers, which summarize basic application
information for the officer to support faster processing. Officers still perform a
full individual assessment of each application and its supporting documents.

The tool never refuses or recommends refusing applications. IRCC officers
make the final decision to approve or refuse on all applications.
The tool is expected to result in faster processing times for all applications.

Visitor records are one of IRCC’s most straightforward services. These
applications are considered low impact, as clients are not applying for refugee
status, permanent residence or citizenship, and are not entitled to study or
work in Canada.


Business Driver / Positive Impact
10. What is motivating your team to introduce automation into this decision-making process?
(Check all that apply)
Existing backlog of work or cases
Use innovative approaches
Other (please specify)

11. Please describe
Facilitate more efficient use of IRCC resources in the application processing,
assist in managing the growing volume of applications, improve processing
times, and identify complex cases.


About The System
12. Please check which of the following capabilities apply to your system.
Process optimization and workflow automation: Analyzing large data sets to
identify and anomalies, cluster patterns, predict outcomes or ways to
optimize; and automate specific workflows


Section 1: Impact Level : 2
Current Score: 40

Raw Impact Score: 40

Mitigation Score: 35

Section 2: Requirements Specific to Impact Level 2
Peer Review
At least one of:

   Qualified expert from a federal, provincial, territorial or municipal government institution.
   Qualified members of faculty of a post-secondary institution.
   Qualified researchers from a relevant non-governmental organization.
   Contracted third-party vendor with a related specialization.
   Publishing specifications of the Automated Decision System in a peer-reviewed journal.
   A data and automation advisory board specified by Treasury Board Secretariat.

Notice
Plain language notice posted through all service delivery channels in use (Internet, in person,
mail or telephone).

Human-in-the-loop for decisions
Decisions may be rendered without direct human involvement.

Explanation Requirement
In addition to any applicable legal requirement, ensuring that a meaningful explanation is
provided with any decision that resulted in the denial of a benefit, a service, or other regulatory
action.

Training
Documentation on the design and functionality of the system.

Contingency Planning
None

Approval for the system to operate
None

Other Requirements
The Directive on Automated Decision-Making also includes other requirements that must be met
for all impact levels.

Link to the Directive on Automated Decision-Making

Contact your institution's ATIP office to discuss the requirement for a Privacy Impact
Assessment as per the Directive on Privacy Impact Assessment.

Section 3: Questions and Answers
Section 3.1: Impact Questions and Answers
Risk Profile
1. Is the project within an area of intense public scrutiny (e.g. because of privacy concerns) and/
or frequent litigation?
Yes                                                                                [ Points: +3 ]

2. Are clients in this line of business particularly vulnerable?
No                                                                                  [ Points: +0 ]

3. Are stakes of the decisions very high?
No                                                                                  [ Points: +0 ]

4. Will this project have major impacts on staff, either in terms of their numbers or their roles?
No                                                                                [ Points: +0 ]
Project Authority
5. Will you require new policy authority for this project?
No                                                                                 [ Points: +0 ]


About the Algorithm
6. The algorithm used will be a (trade) secret
No                                                                                 [ Points: +0 ]

7. The algorithmic process will be difficult to interpret or to explain
No                                                                                 [ Points: +0 ]


About the Decision
8. Does the decision pertain to any of the categories below (check all that apply):
Other (please specify)                                                           [ Points: +1 ]

9. Please describe
Immigration services


Impact Assessment
10. Will the system only be used to assist a decision-maker?
No                                                                                 [ Points: +0 ]

11. Will the system be replacing a decision that would otherwise be made by a human?
Yes                                                                            [ Points: +3 ]

12. Will the system be replacing human decisions that require judgement or discretion?
Yes                                                                           [ Points: +4 ]

13. Please describe the decision(s) that will be automated
The system can automate the approval of the eligibility portion of certain
visitor record applications. For these applications, the system determines only
that the applicant is eligible before the application is sent to an officer to
screen for admissibility. In cases where eligibility is auto-approved, officers
continue to make the admissibility determination and the final decision on
each application. If an officer encounters information in the course of their
admissibility assessment that may affect the positive eligibility determination
of an application, they may revisit the eligibility determination.

For applications that do not have the eligibility portion automatically approved
by the system, both the eligibility and admissibility portions are done manually
by officers. The automated system makes no recommendations regarding
eligibility. Consequently, final decisions to approve or refuse are based wholly
on manual review by experienced officers.

The system never refuses applications, nor does it recommend refusals.

All applications continue to receive an individualized assessment.

14. Is the system used by a different part of the organization than the ones who developed it?
Yes                                                                                   [ Points: +4 ]

15. Are the impacts resulting from the decision reversible?
Reversible                                                                            [ Points: +1 ]

16. How long will impacts from the decision last?
Some impacts may last a matter of months, but some lingering impacts may
last longer                                                                           [ Points: +2 ]

17. Please describe why the impacts resulting from the decision are as per selected option
above.
Visitor records are temporary and do not entitle the holder to work, study or
immigrate to Canada. A negative decision may impact a client's travel plans or
ability to remain in Canada. This impact, however, is likely to be temporary as
clients whose application is refused can re-apply. IRCC approves many clients
with prior refusals. The impact of most refusals is not perpetual. However, it
should be noted that although the system will automate the approval of the
eligibility of some clients, it will not make nor recommend any decisions to
refuse. Officers will continue to make all decisions related to admissibility and
all final decisions to approve or refuse.

18. The impacts that the decision will have on the rights or freedoms of individuals will likely be:
Little to no impact                                                              [ Points: +1 ]

19. Please describe why the impacts resulting from the decision are (as per selected option
above).
The system assesses data elements in incoming applications in order to
triage (sort) applications based on complexity and automate positive
eligibility determinations for applications with low complexity. The system is
expected to have a low impact on the rights and freedoms of individuals, as
the sorting of applications and facilitating approvals do not deny the rights of
any clients.

To ensure fairness and transparency, the system’s rules are based only on
data elements with a clear link to legislative and regulatory requirements, and
the system never refuses applications, nor does it recommend refusals. All
refusals continue to be done by officers as per the current practice. All
applications where eligibility cannot be approved automatically by the system
will receive a full assessment by officers in accordance with standard
practice. For applications where the positive eligibility determination is
automated by the system, the system determines only that an applicant is
eligible, before the application is sent to an officer to screen for admissibility.
Thus, even in cases where the system approves the eligibility, officers
continue to make all final decisions.

Measures are also in place to mitigate against the potential risk that the triage
function could influence officer decision-making. There is deliberate
separation of officers from the system: officers are not aware of the rules
used by the system, nor do they receive information about the analysis
performed by the system. This separation mitigates the risk that officers
could be unduly influenced by the system’s outputs (also known as
“automation bias”). Additionally, an ongoing quality assurance process has
been implemented to monitor whether officers make the same positive
eligibility determinations as the system. This process ensures that biases
have not been introduced by the system.

As a further safeguard, system rules go through an extensive review process.
Before they are introduced, and at regular intervals afterward, rules are
reviewed by experienced officers, legal, policy, and data science experts, as
well as senior executives to ensure they are logical, understandable, non-
discriminatory and aligned with established eligibility criteria. Regular
monitoring and quality assurance measures also help make sure the system
performs as intended and that any unforeseen negative impacts such as bias
or discrimination can be identified early and mitigated.

20. The impacts that the decision will have on the health and well-being of individuals will likely
be:
Little to no impact                                                              [ Points: +1 ]

21. Please describe why the impacts resulting from the decision are (as per selected option
above)
The system is expected to have little to no negative impact on the health and
well-being of individuals as it will be used to triage applications and to
automate certain positive eligibility determinations.

22. The impacts that the decision will have on the economic interests of individuals will likely
be:
Little to no impact                                                             [ Points: +1 ]

23. Please describe why the impacts resulting from the decision are (as per selected option
above)
The system is expected to have little to no negative impact on the economic
interests of individuals as it will be used to triage applications and to
automate certain positive eligibility determinations.

24. The impacts that the decision will have on the ongoing sustainability of an environmental
ecosystem, will likely be:
Little to no impact                                                              [ Points: +1 ]

25. Please describe why the impacts resulting from the decision are (as per selected option
above)
The system is expected to have little to no negative impact on the
environment as it will be used to triage applications and to automate certain
positive eligibility determinations.


About the Data - A. Data Source
26. Will the Automated Decision System use personal information as input data?
Yes                                                                          [ Points: +4 ]

27. Have you verified that the use of personal information is limited to only what is directly
related to delivering a program or service?
Yes                                                                              [ Points: +0 ]

28. Is the personal information of individuals being used in a decision-making process that
directly affects those individuals?
Yes                                                                             [ Points: +2 ]

29. Have you verified if the system is using personal information in a way that is consistent
with: (a) the current Personal Information Banks (PIBs) and Privacy Impact Assessments (PIAs)
of your programs or (b) planned or implemented modifications to the PIBs or PIAs that take new
uses and processes into account?
Yes                                                                               [ Points: +0 ]

30. What is the highest security classification of the input data used by the system? (Select one)
Protected B / Protected C                                                         [ Points: +3 ]

31. Who controls the data?
Federal government                                                              [ Points: +1 ]

32. Will the system use data from multiple different sources?
Yes                                                                             [ Points: +4 ]

33. Will the system require input data from an Internet- or telephony-connected device? (e.g.
Internet of Things, sensor)
No                                                                              [ Points: +0 ]

34. Will the system interface with other IT systems?
No                                                                              [ Points: +0 ]

35. Who collected the data used for training the system?
Your institution                                                                [ Points: +1 ]

36. Who collected the input data used by the system?
Your institution                                                                [ Points: +1 ]


About the Data - B. Type of Data
37. Will the system require the analysis of unstructured data to render a recommendation or a
decision?
Yes                                                                            [ Points: 0 ]

38. What types of unstructured data? (Check all that apply)
Audio and text files                                                            [ Points: +2 ]


Section 3.2: Mitigation Questions and Answers
Consultations
1. Internal Stakeholders (Strategic policy and planning, Data Governance, Program Policy, etc.)
Yes                                                                            [ Points: +1 ]

2. Which Internal Stakeholders have you engaged?
Strategic Policy and Planning
Program Policy
Legal Services
Access to Information and Privacy Office
Communications
Client Experience / Client Relationship Management
Other (describe)

3. Please describe
- Integrity Risk Management
- Centralized Network
- GBA+

4. External Stakeholders (Civil Society, Academia, Industry, etc.)
Yes                                                                              [ Points: +1 ]

5. Which External Stakeholders have you engaged?
Office of the Privacy Commissioner
Academia
Other (describe)

6. Please describe
- Statistics Canada
- Immigration lawyers


De-Risking and Mitigation Measures - Data Quality
7. Do you have documented processes in place to test datasets against biases and other
unexpected outcomes? This could include experience in applying frameworks, methods,
guidelines or other assessment tools.
Yes                                                                          [ Points: +2 ]

8. Is this information publicly available?
No                                                                               [ Points: +0 ]

9. Have you developed a process to document how data quality issues were resolved during the
design process?
Yes                                                                         [ Points: +1 ]

10. Is this information publicly available?
No                                                                               [ Points: +0 ]

11. Have you undertaken a Gender Based Analysis Plus of the data?
Yes                                                                              [ Points: +1 ]

12. Is this information publicly available?
No                                                                               [ Points: +0 ]

13. Have you assigned accountability in your institution for the design, development,
maintenance, and improvement of the system?
Yes                                                                             [ Points: +2 ]

14. Do you have a documented process to manage the risk that outdated or unreliable data is
used to make an automated decision?
Yes                                                                         [ Points: +2 ]

15. Is this information publicly available?
No                                                                               [ Points: +0 ]
16. Is the data used for this system posted on the Open Government Portal?
No                                                                                   [ Points: +0 ]


De-Risking and Mitigation Measures - Procedural
Fairness
17. Does the audit trail identify the authority or delegated authority identified in legislation?
Yes                                                                                  [ Points: +1 ]

18. Does the system provide an audit trail that records all the recommendations or decisions
made by the system?
Yes                                                                            [ Points: +2 ]

19. Are all key decision points identifiable in the audit trail?
Yes                                                                                  [ Points: +2 ]

20. Are all key decision points within the automated system's logic linked to the relevant
legislation, policy or procedures?
Yes                                                                              [ Points: +1 ]

21. Do you maintain a current and up to date log detailing all of the changes made to the model
and the system?
Yes                                                                             [ Points: +2 ]

22. Does the system's audit trail indicate all of the decision points made by the system?
Yes                                                                               [ Points: +1 ]

23. Can the audit trail generated by the system be used to help generate a notification of the
decision (including a statement of reasons or other notifications) where required?
Yes                                                                              [ Points: +1 ]

24. Does the audit trail identify precisely which version of the system was used for each
decision it supports?
Yes                                                                              [ Points: +2 ]

25. Does the audit trail show who an authorized decision-maker is?
Yes                                                                                  [ Points: +1 ]

26. Is the system able to produce reasons for its decisions or recommendations when required?
Yes                                                                           [ Points: +2 ]

27. Is there a process in place to grant, monitor, and revoke access permission to the system?
Yes                                                                              [ Points: +1 ]

28. Is there a mechanism to capture feedback by users of the system?
Yes                                                                                  [ Points: +1 ]

29. Is there a recourse process established for clients that wish to challenge the decision?
Yes                                                                               [ Points: +2 ]

30. Does the system enable human override of system decisions?
Yes                                                                                  [ Points: +2 ]
31. Is there a process in place to log the instances when overrides were performed?
Yes                                                                             [ Points: +1 ]

32. Does the system's audit trail include change control processes to record modifications to the
system's operation or performance?
Yes                                                                            [ Points: +2 ]

33. Have you prepared a concept case to the Government of Canada Enterprise Architecture
Review Board?
No                                                                          [ Points: +0 ]


De-Risking and Mitigation Measures - Privacy
34. If your system involves the use of personal information, have you undertaken a Privacy
Impact Assessment, or updated an existing one?
No                                                                             [ Points: +0 ]

35. Have you designed and built security and privacy into your systems from the concept stage
of the project?
Yes                                                                            [ Points: +1 ]

36. Is the information used within a closed system (i.e. no connections to the Internet, Intranet
or any other system)?
No                                                                               [ Points: +0 ]

37. If the sharing of personal information is involved, has an agreement or arrangement with
appropriate safeguards been established?
No                                                                               [ Points: +0 ]
