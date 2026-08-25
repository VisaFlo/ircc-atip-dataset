# GCMS Full Outage: Post-Incident Report (39p)

> Source: IRCC record released under the Access to Information Act. 1A-2025-13519 · obtained by informal request (open.canada.ca).
> Text below is local-OCR output of the scanned release and carries OCR noise; the release PDF is authoritative.

mmigration, Refugees Immigration, Réfugiés and Citizenship Canadaet Citoyenneté Canada

s.16(2)(c)
L'information divulguée en vertu de la loi sur l’accès à linformation Immigration, Refugees Immigration, Réfugiés and Čitizenship Cānada et Citoyenneté Canada

## Post Incident Report Global Case Management System (GCMS)

# Full Outage

Report prepared by: High Availability Response Team – Major Incident Coordination

#### Date of report 2024-01-14 Start of incident (EST) 2024-03-01 9:00

#### End of Incident (EST)2024-03-01 12:48

Outage Duration 3 hours 48 minutes

#### Ticket number(s)HART: INC000001071681 SSC: INC000000503905

SupportN/A Documentation

### Priority Critical (P1)

#### Incident Description Global Case Management System (GCMS) experienced a full outage. The

crashed and the technical teams put up maintenance pages to stop incoming traffic. Business Impact GCMS Impact

- Affected stakeholders: IRCC, CBSA, GAC, ESDC, Public clients
- Affected locations: All
- IRCC and partner users cannot share biometric/biographic or immigration information with each other
- IRCC users cannot process public client visiting/studying/working/ in Canada, permanent residency, refugee, Canadian citizenship, or official travel applications
- CBSA users cannot process public client enforcement/facilitation/detention cases, refugee claims, and border crossing examinations, make referrals for Immigration hearings or assist airlines with passenger flight boarding allowance
- Public clients traveling to Canada risk travel delays and being held in CBSA secondary areas until GCMS is available
- IRCC and partner operations impaired with backlog clean up post-resolution
- Passport Program may be affected Onlines Services Impact
- Affected stakeholders: IRCC, CBSA, Public clients
- Public clients cannot access or apply to various eServices
- Public clients cannot access Service Delivery Web Tools
- IRCC agents and partners cannot receive requests from public clients for IRCC services
- Passport Program may be affected Impact
- Affected stakeholders: IRCC, ESDC, Public clients
1A-2025-13519-000001

Immigration, Réfugiés migration, Refugees 1*1and Citizenship Canada et Citoyenneté Canada Information disclosed under the Access to Information Act

s.16(2)(c) Lnmdion
Immigration, Refugees Immigration, Réfugiés and Citizenship Canada et Citoyenneté Canada

- Affected programs: Passport
- Affected locations: All
- IRCC and partner users cannot process passport applications of clients who apply in person
- Public clients cannot apply for passports in person
Root Cause Unknown Resolution Reconfiguration of the and restart of the server

# Internal Use Only

1A-2025-13519-000002

and Citizenship Canadaet Citoyenneté Canada L'information divulguée en vertu de la loi sur l’accès à linformation

s.16(2)(c)
Immigration, Refugees Immigration, Réfugiés and Čitizenship Cānada et Citoyenneté Canada

Protected A

### Post Incident Report-FINAL

# Global Case Management System (GCMS) Multiple Disruptions

Report purpose: High Availability Response Team (HART) – Major Incident Coordination (MIC) drafts Post Incident Reports (PIR) to provide additional incident details to senior management about critical (P1) incidents affecting IRCC applications and systems and to provide input into the problem management process.

HART-MIC works with internal and partner IT teams to review incident information before final publication. This report provides the final capture of the incident being reported.

This report is reviewed by the HART Manager and IT Service Management Director prior to publishing the final version.

Target to post final PIRs is seven business days post-incident.

Final Report Publishing Date

## Priority

HART Ticket

### Partner Ticket (SSC) Start Date and Time (EST)

### End Date and Time (EST)

Total Disruption Duration

09-11-2024 Critical (P1) INC000001106379/INC000001106457 INC000000559856 / INC000000559461 2024-06-03 09:01 / 2024-06-0313:39

### 2024-06-03 11:35 / 2024-06-07 24:00

GCMS Degradation - 84hrs 35min

### GCMS Full Outage - 13hrs 11min

eServices Full Outage - 9hrs 08min

## Full Outage – 9hrs 46 min

GCMS Partial Outage - 3hrs 32min eServices Degradation – 1h 20min

### Application Change Known – the new version deployed on June 3rd caused

unforeseen instabilities to the GCMS system and related services

### Deployment of vendor recommended configurations to the impacted servers and SSC connectivity

infrastructure improvements

### IRCC Global Case Management System (GCMS) experienced

### multiple disruptions ranging from degradations to full outages

between June 3 and June 7, 2024.

# Page 1 of 6

1A-2025-13519-000003

### Issue Category Root Cause

Resolution

Primary Resolver Team

### Incident Description

mmigration, Refugees and Citizenship Canadaet Citoyenneté Canada Information disclosed under the Access to Information Act L'information divulguée en vertu de la loi sur l'accès à l’information

s.16(2)(c)
Immigration, Refugees Immigration, Réfugiés and Čitizenship Cānada et Citoyenneté Canada

## Business Impact GCMS Degradation

- Some users intermittently may not be able to log in to GCMS
- Some transactions may experience backlogs and cause various application processing delays
# GCMS Full Outage

- Affected stakeholders: IRCC, CBSA, GAC, ESDC, Public clients
- Affected programs: All, including Passport & Temporary Residence
- Affected locations: All
- ESDC partner users cannot submit passport applications in
- Public clients cannot submit eTA applications
- IRCC and partner users cannot share biometric/biographic or immigration information with each other
- IRCC users cannot process public client visiting/studying/working/ in Canada, permanent residency, refugee, Canadian citizenship, or official travel applications
- CBSA users cannot process public client enforcement/facilitation/detention cases, refugee claims, and border crossing examinations, make referrals for Immigration hearings or assist airlines with passenger flight boarding allowance
- Public clients travelling to Canada risk travel delays and being held in CBSA secondary areas until GCMS is available
- IRCC and partner operations impaired with backlog clean up post-resolution
### eServices Full Outage

- Affected stakeholders: IRCC, CBSA, Public clients-Public clients cannot access or apply to various eServices
- Public clients cannot access Service Delivery Web Tools
- IRCC agents and partners cannot receive requests from public clients for IRCC services
- Passport Program may be affected Full Outage
- Affected stakeholders: IRCC, ESDC, Public clients
- Affected programs: Passport
- Affected locations: All
# Page 2 of 6

1A-2025-13519-000004

mmigration, Refugees and Citizenship Canadaet Citoyenneté Canada L'information divulguée en vertu de la loi sur l'accès à l’information

|||L'information divulguée en vertu de la loi sur l'accès à l’information|
|---|---|---|
|Immigration, Refugees|Immigration, Réfugiés||
|and Čitizenship Cānada|et Citoyenneté Canada||

s.16(2)(c)
- IRCC and partner users cannot process passport applications of clients who apply in person
- Public clients cannot apply for passports in person GCMS Partial Outage Full Outage]
- Affected stakeholders: IRCC, CBSA, ESDC, GAC, Public Clients
- Affected programs: Temporary Residence, Permanent Residence, Citizenship, Refugee Protection, Settlement & Integration, Passport
- GCMS users cannot send correspondence or emails with attachments
- GCMS users cannot load 2D Forms
- ATIP users cannot create some reportsand ATIP) eServices Degradation [eTA Degradation]
- Affected stakeholders: IRCC, CBSA, Public clients
- Affected programs: Temporary Residence
- Some public clients travelling to Canada cannot board flights without an approved eTA, resulting in travel delays/missed flights
- Some IRCC and CBSA users cannot process electronic travel authorizations for travelers
- Som public clients cannot apply to travel to Canada
- CBSA must work with airlines as they determine flight decisions/options for public clients who cannot obtain eTAs to board flights
- CBSA can exercise discretion to allow non-eTA holding public clients to board flights
High Level Timeline June 3, 2024 09:01 – GCMS started to fail (degradation) [INC000001106379]

### 09:40 – GCMS maintenance pages went up and servers

restarted [INC000001108668] 11:35 – GCMS maintenance pages brought down (full outage end) 11:35-13:39 – GCMS general degradation continued [INC000001106457]

### 13:39 – GCMS started to fail and maintenance pages went up

for GCMS, eServices, and servers restarted [INC000001108708, INC000001108697] maintenance pages brought 16:30 - GCMS, eServices, down (full outage end)

# Page 3 of 6

1A-2025-13519-000005

|||mmigration, Refugees|Immigration, Réfugiés|
|---|---|---|---|
|||Information disclosed under the Access to Information Actand Citizenship Canada L'information divulguée en vertu de la loi sur l'accès à l’information|et Citoyenneté Canada|
|Immigration, Refugees|Immigration, Réfugiés|||
|and Čitizenship Cānada|et Citoyenneté Canada|||

s.16(2)(c)
16:30-17:45 – GCMS general degradation continued [INC000001109464]

### 17:45 – GCMS started to fail and maintenance pages went up

for GCMS, eServices, and as IT support teams continued the investigation [INC000001108913] [INC000001108916] 20:29 – Reboot ended but IT support teams needed to perform health checks and clear transaction queues so

### maintenance pages didn't come down until later, as follows:

GCMS and eServices at 20:29, and at 21:17 - IT

## support teams continued monitoring GCMS with automated

servers one at a time as errors alerts and restarted came up 20:29 - GCMS general degradation continued until June 4th, at 03:00 [INC000001109465]

June 4, 2024

### 03:00 - GCMS started to fail and maintenance pages went up

for GCMS and eServices and servers were restarted [INC000001108704] [INC000001108705]

## 04:00 - GCMS, and eServices maintenance pages brought

down (full outage end) - IT support teams continued monitoring GCMS overnight with standard automated alerts and restarted servers one at a time as errors came up

## 04:00-12:30 – GCMS general degradation continued

[INC000001109498] 12:30 – GCMS and eServices crashed, as scheduled OS patching was mistakenly applied by SSC to the active production servers. Not related to the ongoing GCMS incident, but happened during the main incident being reported on in this PIR [INC000001106710] [INC000001109191] 14:55 – Patching was stopped before completion once it was identified it was applied by mistake and servers were restarted to stabilize the GCMS environment – GCMS was

## back on line at 14:55. IT support teams continued monitoring

GCMS with standard automated alerts and restarted servers one at a time as errors came up 14:55 – GCMS general degradation continued until June 5th, at 09:07 [INC000001109500] PM (time-stamp not captured) – Vendorprovided performance optimization recommendations

# Page 4 of 6

1A-2025-13519-000006

mmigration, Refugees and Citizenship Canadaet Citoyenneté Canada

|||Information disclosed under the Access to Information Act|and Citizenship Canadaet Citoyenneté Canada|
|---|---|---|---|
|||L'information divulguée en vertu de la loi sur l'accès à l’information||
|Immigration, Refugees|Immigration, Réfugiés|||
|and Čitizenship Cānada|et Citoyenneté Canada|||

Information disclosed under the Access to Information Act

s.16(2)(c)
June 5, 2024 AM (time-stamp not captured) – IT support teams began working on preliminary change steps to implement performance optimization recommendations 09:07 -appliance failed and took GCMS offline [INC000001108707] 09:13-maintenance pages went up 09:15 – eServices maintenance pages went up [INC000001108710] 11:23 – GCMS restart successful after failure and GCMS back on line –and eServices maintenance pages brought down (full outage end) 11:23-13:39 – GCMS general degradation continued [INC000001109473] 13:39 - GCMS experienced a full outage resulting in a GCMS partial outage until 15:30 – GCMS users reported not being able to login to GCMS between 15:19 and 15:33 (partial outage end) [INC000001108715] 13:39 - GCMS general degradation continued until June 6th, at 13:15 [INC000001109207] 17:45 – Change window began to implement recommended performance changes in two phases 19:35 – Initial recommended changes implemented – IT support teams continued monitoring GCMS with automated alerts

June 6, 2024 08:00 - Final recommended changes started on Production servers 11:15 – Final recommended changes were successfully applied to most of the servers, but final work will be completed after hours 13:15 - GCMS experienced a full outage resulting in a GCMS partial outage until 14:53 – IT support teams continued monitoring GCMS with automated alerts [INC000001109211]

June 7, 2024 16:00-00:00 – GCMS general degradation continued [INC000001109207] 18:11 - eTA started experiencing intermittent issues [INC000001109223]

## Page 5 of 6

1A-2025-13519-000007

Immigration, Réfugiés Immigration, Refugees and Citizenship Canadaet Citoyenneté Canada

|||Lnfomnduion|
|---|---|---|
|Immigration, Refugees|Immigration, Réfugiés||
|and Čitizenship Cānada|et Citoyenneté Canada||

19:31 - IRCC technical team restarted some of the eTA host instances and that restored eTA functionality and Technical teams continued to monitor the application over the weekend

June 10, 2024 10:00 - GCMS Release 31.00.02 was applied for fine tuning performance improvements.

June 11, 2024 00:00 - All the additional changes were applied successfully and the system remained stable. 16:00 - The technical teams confirmed the system remained stable after all the changes applied. The incident was considered resolved as of Friday, June 7th at midnight. IT Teams Consulted Add/delete IT teams consulted for report review and check the box if they provided feedback IRCC – ESO: feedback provided IRCC – IM: feedback provided IRCC – PROS: feedback provided IRCC – GCMS RM: feedback provided Shared Services Canada (SSC) Issued on: 2024-06-21 Critical Incident Summary (CIS) Saved with the main HART ticket in Remedy

## Page 6 of 6

1A-2025-13519-000008

Immigration, Réfugiés and Citizenship Canadaet Citoyenneté Canada Information disclosed under the Access to Information Act L'information divulguée en vertu de la loi sur l’accès à linformation

|||L'information divulguée en vertu de la loi sur l’accès à linformation|
|---|---|---|
|Immigration, Refugees|Immigration, Réfugiés||
|and Čitizenship Cānada|et Citoyenneté Canada||

Protected A

#### Post Incident Report-FINAL

eServices

# Full Outage

Report purpose: High Availability Response Team (HART) – Major Incident Coordination (MIC) drafts Post Incident Reports (PIR) to provide additional incident details to senior management about critical (P1) incidents affecting IRCC applications and systems and to provide input into the problem

HART-MIC works with internal and partner IT teams to review incident information before final publication. This report provides the final capture of the incident being reported. This report is reviewed by the HART Manager and IT Service Management Director prior to publishing

Target to post final PIRs is seven business days post-incident. 2024-09-17 Critical (P1) INC000001126012

|Partner Ticket (SSC)|INC000001126008|
|---|---|
|Start Date and Time (EST) End Date and Time (EST)|2024-09-17 05:30|
|Total Disruption Duration Root Cause|0 hours 36 minutes Infrastructure Change|
|Primary Resolver Team|IRCC|
|Incident Description|eServices is experienced a full outage due to an|

##### 2024-09-17 06:06

s.16(2)(c)
management process.

##### the final version.

Final Report Publishing Date

### Priority

HART Ticket

## Issue Category

### Resolution

#### Business Impact

# Known -used

corrected

### being used that caused payments to hang. Maintenance

#### pages were put up while support resources investigated the

issue. This issue resulted after GCMS Release 31.5 (CRQ000000089519) - Affected stakeholders: IRCC, CBSA, Public clients-Public clients could not access or apply to various eServices

- Public clients could not Service Delivery Web Tools
- IRCC agents and partners could not receive requests from public clients for IRCC services
Page 1 of 2 1A-2025-13519-000009

mmigration, Refugees and Citizenship Canada et Citoyenneté Canada L'nformtondenvedisuanation

s.16(2)(c)
Immigration, Refugees Immigration, Réfugiés and Citizenship Canada et Citoyenneté Canada

- Passport Program may have been affected
## High Level Timeline 05:30 – Incident start 05:50 – IRCC database administrator updated the

and SSC bounced services, eTA and

## 06:06 – Maintenance pages brought down – incident end

IT Teams ConsultedIRCC – DBA: feedback provided

## Shared Services Canada (SSC) Hyperlink added when CIS received from SSC. Critical Incident Summary (CIS)

# Page 2 of 2

1A-2025-13519-000010

Immigration, Réfugiés and Citizenship Canadaet Citoyenneté Canada L'information divulguée en vertu de la loi sur l’accès à linformation

|||L'information divulguée en vertu de la loi sur l’accès à linformation|
|---|---|---|
|Immigration, Refugees|Immigration, Réfugiés||
|and Čitizenship Cānada|et Citoyenneté Canada||

s.16(2)(c)
Protected A

#### Post Incident Report-FINAL

## Global Case Management System (GCMS)

# Full Outage

Report purpose: High Availability Response Team (HART) – Major Incident Coordination (MIC) drafts Post Incident Reports (PIR) to provide additional incident details to senior management about critical (P1) incidents affecting IRCC applications and systems and to provide input into the problem management process.

HART-MIC works with internal and partner IT teams to review incident information before final publication. This report provides the final capture of the incident being reported.

This report is reviewed by the HART Manager and IT Service Management Director prior to publishing the final version.

Target to post final PIRs is seven business days post-incident.

Final Report Publishing Date

### Priority

HART Ticket

#### Partner Ticket (SSC) Start Date and Time (EST)

#### End Date and Time (EST) Total Disruption Duration

## Issue Category Root Cause

Resolution

#### Primary Resolver Team

Incident Description

#### Business Impact

2024-10-18 Critical (P1) INC000001129867 INC000000632698 2024-10-08 13:28

#### 2024-10-08 15:06 1 hour 38 minutes

#### Application Issue

## Unknown

#### Failover to secondary database

SSC Global Case Management System (GCMS) experienced a because pathway issue linking to the primary of an

#### disk was experiencing latency.

### GCMS

- Affected stakeholders: IRCC, CBSA, GAC, ESDC, Public clients
- Affected programs: All, including Passport & Temporary Residence
- Affected locations: All
- ESDC partner users could submit passport applications in but GCMS could not process these applications
- Public clients could submit eTA applications, but CBSA could not process these applications
##### Page 1 of 2

1A-2025-13519-000011

s.16(2)(c)
Immigration, Refugees and Čitizenship Cānada

## High Level Timeline

IT Teams Consulted

Shared Services Canada (SSC) Critical Incident Summary (CIS)

and Citizenship Canadaet Citoyenneté Canada Information disclosed under the Access to Information Act L'information divulguée en vertu de la loi sur l'accès à l’information Immigration, Réfugiés et Citoyenneté Canada

- IRCC and partner users could not share biometric/biographic or immigration information with each other
- IRCC users could not process public client visiting/studying/working/ in Canada, permanent residency, refugee, Canadian citizenship, or official travel applications
- CBSA users could not process public client enforcement/facilitation/detention cases, refugee claims, and border crossing examinations, make referrals for Immigration hearings or assist airlines with passenger flight boarding allowance
- Public clients traveling to Canada risked travel delays and being held in CBSA secondary areas until GCMS is available
- IRCC and partner operations were impaired with backlog clean up post-resolution eServices
- Affected stakeholders: IRCC, CBSA, Public clients
- Public clients could not access or apply to various eServices
- Public clients could not access Service Delivery Web Tools
- IRCC agents and partners could not receive requests from public clients for IRCC services 2024-10-08 13:28 – GCMS maintenance page up 13:59 – eServices maintenance page up 14:15 – failover from primary to secondary server 15:05 – eServices maintenance page down 15:06 – GCMS maintenance page down; GCMS functionality restored. Add/delete IT teams consulted for report review and check the box if they provided feedback. No external vendors or partners are to be consulted. IRCC – ESO: feedback provided IRCC – DBA: feedback provided Hyperlink added when CIS received from SSC.
## Page 2 of 2

1A-2025-13519-000012

Immigration, Réfugiés and Citizenship Canadaet Citoyenneté Canada L'information divulguée en vertu de la loi sur l’accès à linformation

|||L'information divulguée en vertu de la loi sur l’accès à linformation|
|---|---|---|
|Immigration, Refugees|Immigration, Réfugiés||
|and Čitizenship Cānada|et Citoyenneté Canada||

s.16(2)(c)
Protected A

### Post Incident Report-FINAL

## Global Case Management System (GCMS) Partial Outage

# Full Outage

Report purpose: High Availability Response Team (HART) – Major Incident Coordination (MIC) drafts Post Incident Reports (PIR) to provide additional incident details to senior management about critical (P1) incidents affecting IRCC applications and systems and to provide input into the problem management process.

HART-MIC works with internal and partner IT teams to review incident information before final publication. This report provides the final capture of the incident being reported.

This report is reviewed by the HART Manager and IT Service Management Director prior to publishing

Target to post final PIRs is seven business days post-incident.

the final version.

Final Report Publishing Date Priority HART Ticket Partner Ticket (SSC) Start Date and Time (EST)

### End Date and Time (EST)

Total Disruption Duration Issue Category Root Cause

2024-12-31 Critical (P1) INC000001138130 (GCMS) & INC000001138134 INC000000668541 Start time: 2024-12-02 09:43

End time: 2024-12-02 11:12

1 hours 29 minutes Hardware Issue Known-process error – plug for a cabinet Uninterrupted Power Supply (UPS) became disconnected and lost power while SSC was performing work at the

Plugged in UPS and installed a second UPS SSC Multiple critical applications and application components experienced a full outage resulting in GCMS partial outage and full outage. GCMS – full outage

- Affected Stakeholders: IRCC, CBSA, USA, Public Clients
- GCMS could not communicate with USA partner system to verify VISA validation for public clients traveling to Canada
### Page 1 of 3

1A-2025-13519-000013

Resolution Primary Resolver Team Incident Description

### Business Impact

mmigration, Refugees and Citizenship Canadaet Citoyenneté Canada

s.16(2)(c) L'information divulguée en vertu de la loi sur l'accès à l’information

|Immigration, Refugees|Immigration, Réfugiés|||
|---|---|---|---|
|and Čitizenship Cānada|et Citoyenneté Canada|- CBSA agents could not process public client eTA requests while they await VISA validation||

GCMS – full outage

- Affected Stakeholders: IRCC, CBSA, RCMP,USA, AUS, NZL, Public clients
- IRCC users could not receive information from USA, AUS or NZL
- GCMS could not respond to biographic queries from the USA, AUS, NZL
- IRCC and partner users could exercise discretion to finalize applications in GCMS GCMS – full outage
- Affected Stakeholders: IRCC, Funding Recipients (Service Providing Organizations)
- IRCC users could not properly manage Settlement & Resettlement Contribution Agreements
- IRCC could not process payments to funding recipients
- At fiscal year end, IRCC risks not being able to properly allocate and account for funding
- During call for proposal periods, risks to harming IRCC's reputation and damaging relationships with funding recipients across Canada
- Funding recipients could not submit applications for funding, submit claims for reimbursement, or complete other various information exchanges – full outage
- Affected stakeholders: IRCC, ESDC, Public clients
- Affected programs: Passport
- Affected locations: All
- IRCC and partner users could not process passport applications of clients who apply in person
- Public clients could not apply for passports in person
High Level Timeline 10:21 – ESO engaged IRCC SD 10:35 – Technical conference started 10:35 – IRCC SD provided SSC INC 11:12 – SSC plugged in UPS and restored service 11:24 – SSC Incident Coordination joined the technical conference IT Teams ConsultedIRCC-ESO: feedback provided

## Page 2 of 3

1A-2025-13519-000014

Immigration, Réfugiés Immigration, Refugees

## 1*and Citizenship Canada et Citoyenneté Canada

L'information divulguée en vertu de la loi sur l’accès à linformation Immigration, Refugees Immigration, Réfugiés and Citizenship Canada et Citoyenneté Canada

Shared Services Canada (SSC)Hyperlink added when CIS received from SSC.

## Critical Incident Summary (CIS)

# Page 3 of 3

1A-2025-13519-000015

Immigration, Réfugiés and Citizenship Canadaet Citoyenneté Canada Information disclosed under the Access to Information Act L'information divulguée en vertu de la loi sur l’accès à linformation

|||L'information divulguée en vertu de la loi sur l’accès à linformation|
|---|---|---|
|Immigration, Refugees|Immigration, Réfugiés||
|and Čitizenship Cānada|et Citoyenneté Canada||

s.16(2)(c)
Protected A

#### Post Incident Report-FINAL

## Global Case Management System (GCMS)

# Partial Outage

Report purpose: High Availability Response Team (HART) – Major Incident Coordination (MIC) drafts Post Incident Reports (PIR) to provide additional incident details to senior management about critical (P1) incidents affecting IRCC applications and systems and to provide input into the problem management process.

HART MIC works with internal and partner IT teams to review incident information before final publication. This report provides the final capture of the incident being reported.

This report is reviewed by the HART Manager and IT Service Management Director prior to publishing the final version.

Target to post final PIRs is seven business days post-incident.

Final Report Publishing Date Priority HART Ticket Partner Ticket (SSC) Start Date and Time (EST) End Date and Time (EST) Total Disruption Duration IT Service Component

## Issue Category

### Root Cause

Resolution Primary Resolver Team Incident Description

#### Business Impact

2025-01-02 Critical (P1) INC000001141735 INC000000681200 2024-12-28 16:07 2024-12-28 19:58

#### 3 hours 51 minutes

Not applicable Application Issue

### Unknown Service restart-SSC

#### Global Case Management System (GCMS) experienced a partial

outage. All GCMS components experienced some level of issue with connectivity. eTA

- Affected stakeholders: IRCC, CBSA, Public clients
- Affected programs: Temporary Residence
- Public clients travelling to Canada could not board flights without an approved eTA, resulting in travel delays/missed flights
- IRCC and CBSA users could not process electronic travel authorizations for travelers
- Public clients could not apply to travel to Canada
##### Page 1 of 3

1A-2025-13519-000016

mmigration, Refugees and Citizenship Canadaet Citoyenneté Canada Information disclosed under the Access to Information Act L'information divulguée en vertu de la loi sur l'accès à l’information

|||L'information divulguée en vertu de la loi sur l'accès à l’information|
|---|---|---|
|Immigration, Refugees|Immigration, Réfugiés||
|and Čitizenship Cānada|et Citoyenneté Canada-CBSA worked with airlines as they determine flight||

s.16(2)(c)
decisions/options for public clients who cannot obtain eTAs to board flights

- CBSA exercised discretion to allow non-eTA holding public clients to board flights
- Affected stakeholders: IRCC, CBSA, Public clients
- CBSA could not receive eTA documentation that is required to process public clients traveling to Canada by plane
- CBSA worked with airlines as they determine flight decisions/options for public clients who cannot obtain eTAs to board flights
- Public clients traveling to Canada risked travel delays and being held in CBSA secondary areas until the service is available
- Affected stakeholders: IRCC, CBSA, ESDC, Public clients
- Affected programs: Passport & Temporary Residence
- ESDC partner users could submit passport applications in but GCMS could not process these applications
- IRCC and partner users could not perform automated processes for or detail results
- Public clients could submit eTA applications and these processed through to CBSA, but CBSA could not process eTAs
- Partner users could not share immigration information with expectant partners
- CBSA users could not process public client enforcement/facilitation/detention cases, refugee claims, and border crossing examinations, make referrals for Immigration hearings or assist airlines with passenger flight boarding allowance
- Public clients traveling to Canada risked travel delays and being held in CBSA secondary areas until GCMS is available
- Partner operations impaired with backlog clean up post-resolution 16:30 – IRCC technical conference started
### High Level Timeline

16:50 – ESO engaged the ITSD 17:42 – SSC IC connected with HART MIC

### 18:14 – SSC technical conference started

## 18:40 – SSC put up GCMS maintenance pages and SSC

restarted GCMS

## 19:58 – SSC took down GCMS maintenance pages

#### Page 2 of 3

1A-2025-13519-000017

and Citizenship Canadaet Citoyenneté Canada Information disclosed under the Access to Information Act

s.16(2)(c)
Lnfomnduion Immigration, Refugees Immigration, Réfugiés et Citoyenneté Canada and Citizenship Canada

IT Teams Consulted IRCC – ESO: feedback provided

## IRCC – IM: feedback provided

### Shared Services Canada (SSC) Hyperlink added when CIS received from SSC.

Critical Incident Summary (CIS) Comments Process issues identified from engaging the IRCC ITSD to engaging the SSC SD to SSC IC technical conference set up that prolonged incident resolution. The ITSD

will take corrective measures on IRCC process issues

### identified by HART MIC.

There was mention on another incident that occurred

## during the same time period and could be related:

INC000000684651. connection

# More investigation required – after

### was re-established, the were not picking up messages from the

# Page 3 of 3

1A-2025-13519-000018

Immigration, Réfugiés and Citizenship Canadaet Citoyenneté Canada L'information divulguée en vertu de la loi sur l'accès à l’information

|||L'information divulguée en vertu de la loi sur l'accès à l’information|
|---|---|---|
|Immigration, Refugees|Immigration, Réfugiés||
|and Čitizenship Cānada|et Citoyenneté Canada||

s.16(2)(c)
Protected A

#### Post Incident Report-FINAL

## Global Case Management System (GCMS)

partial outage

Report purpose: High Availability Response Team (HART) – Major Incident Coordination (MIC) drafts Post Incident Reports (PIR) to provide additional incident details to senior management about critical (P1) incidents affecting IRCC applications and systems and to provide input into the problem management process.

HART-MIC works with internal and partner IT teams to review incident information before final publication. This report provides the final capture of the incident being reported.

This report is reviewed by the HART Manager and IT Service Management Director prior to publishing the final version.

Target to post final PIRs is seven business days post-incident.

Final Report Publishing Date

### Priority

HART Ticket Partner Ticket (SSC) Start Date and Time (EST) End Date and Time (EST) Total Disruption Duration IT Service Component

# Issue Category

### Root Cause

Resolution

Primary Resolver Team Incident Description

2025-02-03

Critical (P1) INC000001145273

#### INC000000700640

2025-01-25 06:51 EST 2025-01-25 10:20 EST 3 hours 29 minutes Global Case Management System (GCMS) Application Issue

### Unknown

Service restart – eServicesand:

SSC Global Case Management System (GCMS) experienced a partial outage. The issue was a communication error between GCMS and a that allows GCMS to

#### middleware component, exchange information by sending and receiving messages and it

affected multiple services.

#### GCMS

- Affected stakeholders: IRCC, CBSA, GAC, ESDC, Public clients
- ESDC partner users could submit passport applications in but GCMS could not process these applications
### Page 1 of 3

1A-2025-13519-000019

##### Business Impact

Immigration, Réfugiés and Citizenship Canadaet Citoyenneté Canada Information disclosed under the Access to Information Act L'information divulguée en vertu de la loi sur l'accès à l’information

s.16(2)(c)
Immigration, Refugees Immigration, Réfugiés and Čitizenship Cānada et Citoyenneté Canada

- Public clients could submit passport applications though IRCC Portal-New Version, but GCMS could not process these applications
- Public clients could submit eTA applications, but CBSA could not process these applications
- IRCC and partner users could not share biometric/biographic or immigration information with each other
- IRCC users could not process public client visiting/studying/working/ in Canada, permanent residency, refugee, Canadian citizenship, or official travel applications
- CBSA users could not process public client enforcement/facilitation/detention cases, refugee claims, and border crossing examinations, make referrals for Immigration hearings or assist airlines with passenger flight boarding allowance-Public clients traveling to Canada risked travel delays and being held in CBSA secondary areas until GCMS is available
- IRCC and partner operations impaired with backlog clean up post- resolution eTA
- Affected stakeholders: IRCC, CBSA, Public clients
- Affected programs: Temporary Residence
- Public clients travelling to Canada could not board flights without an approved eTA, resulting in travel delays/missed flights
- IRCC and CBSA users could not process electronic travel authorizations for travelers
- Public clients could apply to travel to Canada
- CBSA worked with airlines as they determine flight decisions/options for public clients who cannot obtain eTAs to board flights
- CBSA exercised discretion to allow non-eTA holding public clients to board flights
- Affected stakeholders: IRCC, CBSA, Public clients
- CBSA could not receive eTA documentation that is required to process public clients traveling to Canada by plane
- CBSA worked with airlines as they determine flight decisions/options for public clients who cannot obtain eTAs to board flights
- Public clients traveling to Canada risked travel delays and being held in CBSA secondary areas until the service is available
High Level Timeline 06:55 – GCMS IM (Incident Management) received alerts for and eTA not processing 07:13 – IM engaged ESO

## Page 2 of 3

1A-2025-13519-000020

Immigration, Refugees *and Citizenship Canada et Citoyenneté Canada Information disclosed under the Access to Information Act Lnfomnduion

|||Lnfomnduion|
|---|---|---|
|Immigration, Refugees|Immigration, Réfugiés||
|and Citizenship Canada|et Citoyenneté Canada||

s.16(2)(c)
07:24 – IRCC technical call started 07:46 – ESO engaged the ITSD 08:30 – SSC IC joined the call 08:45 – SSC WASS team joined the call 09:25-All components were stopped 10:08-components were back up again 10:15 – eTA services were restarted 10:20-were also restarted IT Teams Consulted IRCC-ESO: □ feedback provided IRCC – IM: feedback provided

Comments SSC Problem Management along with IRCC Problem Management issue as it seems to be re- teams were engaged to look into the occurring.

## Page 3 of 3

1A-2025-13519-000021

and Citizenship Canadaet Citoyenneté Canada L'information divulguée en vertu de la loi sur l’accès à linformation

|||L'information divulguée en vertu de la loi sur l’accès à linformation|
|---|---|---|
|Immigration, Refugees|Immigration, Réfugiés||
|and Čitizenship Cānada|et Citoyenneté Canada||

s.16(2)(c)
Protected A

#### Post Incident Report-FINAL

## Global Case Management System (GCMS)

# Full Outage

Report purpose: High Availability Response Team (HART) – Major Incident Coordination (MIC) drafts Post Incident Reports (PIR) to provide additional incident details to senior management about critical (P1) incidents affecting IRCC applications and systems and to provide input into the problem management process.

HART-MIC works with internal and partner IT teams to review incident information before final publication. This report provides the final capture of the incident being reported.

This report is reviewed by the HART Manager and IT Service Management Director prior to publishing the final version.

Target to post final PIRs is seven business days post-incident.

Final Report Publishing Date Priority HART Ticket

#### Partner Ticket (SSC) Start Date and Time (EST)

#### End Date and Time (EST)

Total Disruption Duration

#### IT Service Component Issue Category

## Root Cause

Resolution Primary Resolver Team

#### Incident Description

##### Business Impact

2025-05-22 Critical (P1) INC000001159856 INC000000768824/INC000000768905 2025-05-14 20:27

#### 2025-05-15 03:34 7 hours 7 minutes

Not applicable

#### Infrastructure Change

Known – SSC made a change to the VLAN configuration

#### Revert change

SSC

#### Global Case Management System (GCMS) experienced a full

outage.

#### GCMS

- Affected stakeholders: IRCC, CBSA, GAC, ESDC, Public clients
- ESDC partner users could submit passport applications in but GCMS could not process these applications-Public clients could not submit passport applications though
#### IRCC Portal-New Version

- Public clients could submit eTA applications, but CBSA cannot process these applications
- IRCC and partner users could not share biometric/biographic
##### Page 1 of 3

1A-2025-13519-000022

mmigration, Refugees and Citizenship Canadaet Citoyenneté Canada Information disclosed under the Access to Information Act L'information divulguée en vertu de la loi sur l'accès à l’information

s.16(2)(c)
Immigration, Refugees Immigration, Réfugiés and Čitizenship Cānada et Citoyenneté Canada

# or immigration information with each other

- IRCC users could not process public client visiting/studying/working/ in Canada, permanent residency, refugee, Canadian citizenship, or official travel applications
- CBSA users could not process public client enforcement/facilitation/detention cases, refugee claims, and border crossing examinations, make referrals for Immigration hearings or assist airlines with passenger flight boarding allowance
- Public clients traveling to Canada risked travel delays and being held in CBSA secondary areas until GCMS is available
- IRCC and partner operations impaired with backlog clean up post-resolution eServices
- Affected stakeholders: IRCC, CBSA, Public clients-Public clients cannot access or apply to various eServices
- Public clients cannot access Service Delivery Web Tools
- IRCC agents and partners cannot receive requests from public clients for IRCC services
- Passport Program may be affected
High Level Timeline 20:55 – ESO engaged IRCC SD 21:07 – ESO engaged HART MIC 21:15 – IRCC started internal technical call 21:35 – IRCC SD provided SSC INC

# 21:36 – HART engaged SSC IC

22:10 – SSC started technical call 23:00 – SSC identified larger network issue affecting multiple departments 23:22 - SSC identified affected & merged technical calls

# 23:40 – eServices maintenance page put up

00:22 - SSC engaged to help troubleshoot and identified a VLAN configuration change that needed to be reverted 02:16 – SSC re-engaged HART to confirm resolution 02:37 – SSC performed a GCMS restart to stabilize the system

03:34 – GCMS and eServices back on line – incident resolved

IT Teams Consulted IRCC – ESO: feedback provided IRCC-DBA: feedback provided

### Page 2 of 3

1A-2025-13519-000023

Immigration, Réfugiés Immigration, Refugees 1*1and Citizenship Canada et Citoyenneté Canada Information disclosed under the Access to Information Act L'information divulguée en vertu de la loi sur l’accès à linformation Immigration, Refugees Immigration, Réfugiés and Citizenship Canada et Citoyenneté Canada

Comments HART has flagged the VLAN configuration change to IRCC Change and Release Management for follow-up with SSC. CRM confirmed that SSC did not advise them of this change prior to implementation.

## Page 3 of 3

1A-2025-13519-000024

Immigration, Réfugiés and Citizenship Canadaet Citoyenneté Canada L'informatindguéenvedelloisurlacsainfomation

s.16(2)(c)
Immigration, Refugees Immigration, Réfugiés and Čitizenship Cānada et Citoyenneté Canada

Protected A

#### Post Incident Report-FINAL

## Global Case Management System (GCMS)

full outage

Report purpose: High Availability Response Team (HART) – Major Incident Coordination (MIC) drafts Post Incident Reports (PIR) to provide additional incident details to senior management about critical (P1) incidents affecting IRCC applications and systems and to provide input into the problem management process.

HART-MIC works with internal and partner IT teams to review incident information before final publication. This report provides the final capture of the incident being reported.

This report is reviewed by the HART Manager and IT Service Management Director prior to publishing

Target to post final PIRs is seven business days post-incident.

##### the final version.

Final Report Publishing Date

### Priority

HART Ticket

#### Partner Ticket (SSC) Start Date and Time (EST)

End Date and Time (EST) Total Disruption Duration

#### IT Service Component Issue Category

## Root Cause

Resolution

#### Primary Resolver Team Incident Description

2025-07-08 Critical (P1) INC000001164953 INC000000797821 2025-07-01 11:02

#### 2025-07-01 14:08 3 hours 6 minutes

N/A

#### Infrastructure Change Process error-incorrect node patched in production

environment GCMS servers restart SSC GCMS experienced a full outage due to an error during a scheduled change (SSC CRQ000000123676). The change

mistakenly targeted the active server node instead of the inactive node leading to system

#### unavailability. Upon completion of the patching process,

technical teams rebooted the main GCMS components and successfully restored functionality.

##### Page 1 of 3

1A-2025-13519-000025

and Citizenship Canadaet Citoyenneté Canada L'information divulguée en vertu de la loi sur l'accès à l’information

|||L'information divulguée en vertu de la loi sur l'accès à l’information|
|---|---|---|
|Immigration, Refugees|Immigration, Réfugiés||
|and Čitizenship Cānada|et Citoyenneté Canada||

s.16(2)(c)
## Business ImpactAffected stakeholders included IRCC, CBSA, GAC, ESDC, and

public clients. ESDC partner users were able to submit passport

# applications in but GCMS was unable to process

these applications. Public clients were unable to submit passport applications through the IRCC Portal – New Version.

## Public clients were able to submit eTA applications, but

CBSA was unable to process them. IRCC and partner users were unable to share biometric, biographic, or immigration information with each other. IRCC users were unable to process public client applications related to visiting, studying, working in Canada, permanent residency, refugee status, Canadian citizenship, or official travel. CBSA users were unable to process public client

### enforcement, facilitation, or detention cases, refugee

claims, border crossing examinations, make referrals for immigration hearings, or assist airlines with passenger boarding. Public clients traveling to Canada faced risks of travel delays and being held in CBSA secondary areas until GCMS became available.

- IRCC and partner operations were impaired, with backlog cleanup required post-resolution.
#### High Level Timeline 11:02 EDT – Issue started

11:41 EDT – SWAT call started 12:17 EDT – services stopped 12:22 EDT – receive locations were disabled 12:26 EDT -Maintenance Pages up 12:26 EDT – eServices maintenance pages up

12:52 EDT – GCMS eServices stopped 12:54 EDT – Windows servers were rebooted and back online 12:55 EDT – up

# 13:01 EDT -services up

13:10 EDT – services up13:45 EDT -Up 13:49 EDT – sites up 13:50 EDT – application pools recycled

# 13:59 EDT -receive locations enabled

14:02 EDT -and services up 14:03 EDT – eServices up 14:08 EDT – All maintenance pages down and eServices)

# Page 2 of 3

1A-2025-13519-000026

Immigration, Réfugiés

## 1*1and Citizenship Canada et Citoyenneté Canada

L'nformaonduuedoislsinftion Immigration, Refugees Immigration, Réfugiés and Citizenship Canada et Citoyenneté Canada

## IT Teams Consulted IRCC – ESO: feedback provided IRCC – IM: feedback provided

CommentsIRCC Change and Release Management (CRM) team has been made aware of the issue and (SSC) will also be conducting an internal review to determine the root cause and prevent recurrence.

# Page 3 of 3

1A-2025-13519-000027

Immigration, Réfugiés migration, Refugees and Citizenship Canadaet Citoyenneté Canada

s.16(2)(c)
## PROTECTEDA PROTEGE ton

Immigration, Refugees Immigration, Réfugiés and Čitizenship Cānada et Citoyenneté Canada

#### Post Incident Report-FINAL

### Global Case Management System (GCMS)

full outage

Report purpose: High Availability Response Team (HART) – Major Incident Coordination (MIC) drafts Post Incident Reports (PIR) to provide additional incident details to senior management about critical (P1) incidents affecting IRCC applications and systems and to provide input into the problem management process

HART-MIC works with internal and partner IT teams to review incident information before final publication. This report provides the final capture of the incident being reported.

This report is reviewed by the HART Manager and IT Service Management Director prior to publishing the final version.

servers were restarted along with overwriting the

The incident began during the deployment of GCMS Release 34. As the system was errors were encountered, affecting eTA and other integrated interfaces. These issues were resolved, and GCMS was available between 9:00 AM

Target to post final PIRs is seven business days post-incident.

2025-08-14 Final Report Publishing

### Date

#### Priority Critical (P1)

INC000001168841

#### HART Ticket

INC000000812379 Partner Ticket (SSC) Start Date and Time 2025-07-29 7:30

#### (EST)

2025-07-29 11:45 End Date and Time

#### (EST)

3 hours 35 minutes

#### Total Disruption Duration

IT Service Component N/A

#### Issue Category Application Change Root Cause Unknown

Server restart –

### Resolution

#### file on the maintenance page

Primary ResolverSSCs Team Incident Description coming online,

##### and 9:40 AM.

At 09:40, performance degradation was detected in

Version. Further investigation revealed that

To mitigate the issue,

files were missing from the

#### Page 1 of 2

1A-2025-13519-000028

maintenance pages were re-enabled for GCMS, eService, and IRCC Portal – New

Immigration, Réfugiés and Citizenship Canadaet Citoyenneté Canada

s.16(2)(c)
# PROTECTEDA PROTEGE Aton

Immigration, Refugees Immigration, Réfugiés and Čitizenship Cānada et Citoyenneté Canada

### servers. These files were added, and was restarted to apply the

changes.

By 11:00 AM, maintenance pages were removed and user access was successfully restored. However, some users continued to experience issues accessing GCMS. Investigation revealed that the GCMS main index page was still pointing to the maintenance page. Once the file was updated, full access to GCMS was restored for all users. Business Impact-Affected stakeholders: IRCC, CBSA, GAC, ESDC, Public clients

- ESDC partner users can submit passport applications inbut GCMS cannot process these applications
- Public clients cannot submit passport applications though IRCC Portal-New Version
- Public clients can submit eTA applications, but CBSA cannot process these applications
- IRCC and partner users cannot share biometric/biographic or immigration information with each other
- IRCC users cannot process public client visiting/studying/working/ in Canada, permanent residency, refugee, Canadian citizenship, or official travel applications
- CBSA users cannot process public client enforcement/facilitation/detention cases, refugee claims, and border crossing examinations, make referrals for Immigration hearings or assist airlines with passenger flight boarding allowance
- Public clients traveling to Canada risk travel delays and being held in CBSA secondary areas until GCMS is available
- IRCC and partner operations impaired with backlog clean up post-resolution
High Level Timeline 12:00 – 05:30 Scheduled GCMS maintenance window 05:30 – 07:30 Maintenance window extended to address ongoing issues 07:30 – Transition to Major Incident Management process

09:00-servers rebooted; maintenance pages removed

## 09:40-performance issues observed; maintenance pages re-deployed to

### restrict user access. Missingfiles were identified and were added to

servers 11:00-restart completed; paused services resumed. Maintenance pages removed for GCMS, eServices, and IRCC Portal – New Version 11:00 – Health checks revealed that maintenance pages were still displaying for some users due to the file pointing to an incorrect location. 11:45 - The file was updated, resolving the issue and fully restoring

#### GCMS functionality.

IT Teams Consulted IRCC – DBA: feedback provided

Comments

## Page 2 of 2

1A-2025-13519-000029

Immigration, Réfugiés migration, Refugees and Citizenship Canadaet Citoyenneté Canada

# s.16(2)(c) PROTECTEDA PROTEGE ton

Immigration, Refugees Immigration, Réfugiés and Čitizenship Cānada et Citoyenneté Canada

#### Post Incident Report-FINAL

### Global Case Management System (GCMS)

# Partial Outage

Report purpose: High Availability Response Team (HART) – Major Incident Coordination (MIC) drafts Post Incident Reports (PIR) to provide additional incident details to senior management about critical (P1) incidents affecting IRCC applications and systems and to provide input into the problem management process.

HART-MIC works with internal and partner IT teams to review incident information before final publication. This report provides the final capture of the incident being reported.

This report is reviewed by the HART Manager and IT Service Management Director prior to publishing the final version.

Target to post final PIRs is seven business days post-incident.

Final Report Publishing Date 2025-11-17

## Critical (P1)

# Priority

#### HART Ticket INC000001181274

Partner Ticket (SSC) INC000000870879

### Start Date and Time (EST) 2025-11-04 21:27

End Date and Time (EST) 2025-11-06 19:16 Total Disruption Duration1 day, 21 hours, 52 minutes

#### IT Service Component Not applicable Application Issue Issue Category

Root Cause Known – Network Timeouts:

#### server parameters had an incorrect timeout

code calculation Resolution Configuration Change – SSC reconfigured the code calculation Primary Resolver Team SSC Incident Description Global Case Management System (GCMS) experienced a partial outage. Business ImpactGCMS

- Affected stakeholders: IRCC, CBSA, GAC, ESDC, Public clients
- ESDC partner users can submit passport applications in but GCMS may be delayed processing these applications
- Public clients may not be able to submit passport applications though IRCC Portal-New Version
# Page 1 of 4

1A-2025-13519-000030

Immigration, Réfugiés migration, Refugees and Citizenship Canadaet Citoyenneté Canada

### s.16(2)(c) PROTECTEDA PROTEGE ton

Immigration, Refugees Immigration, Réfugiés and Čitizenship Cānada et Citoyenneté Canada

- Public clients can submit eTA applications, but CBSA may be delayed processing these applications
- IRCC and partner users may not be able to share biometric/biographic or immigration information with each other
- IRCC users may not be able to process public client visiting/studying/working/ in Canada, permanent residency, refugee, Canadian citizenship, or official travel applications
- CBSA users may not be able to process public client enforcement/facilitation/detention cases, refugee claims, and border crossing examinations, make referrals for Immigration hearings or assist airlines with passenger flight boarding allowance
- Public clients traveling to Canada risk travel delays and being held in CBSA secondary areas until GCMS is available
- IRCC and partner operations impaired with backlog clean up post-resolution eServices
- Affected stakeholders: IRCC, CBSA, Public clients
- Public clients cannot access or apply to various eServices
- Public clients cannot access Service Delivery Web Tools
- IRCC agents and partners cannot receive requests from public clients for IRCC services
- Passport Program may be affected IRCC Portal-New Version
- Affected stakeholders: IRCC, Public clients
- Affected Program: Passport
- Public clients cannot submit domestic applications for individual adults whose passport is about to expire, is already expired, is lost, or is stolen
- Public clients cannot perform application updates nor obtain application status for applications already submitted
- Public clients cannot manage their accounts
- Public clients cannot complete payment for new submissions
High Level TimelineTuesday, November 4th 22:48 – ESO engaged HART MIC 23:30 – SSC started SWAT call

# Page 2 of 4

1A-2025-13519-000031

Immigration, Réfugiés migration, Refugees and Citizenship Canadaet Citoyenneté Canada

|||et Citoyenneté Canada|
|---|---|---|
|Immigration, Refugees|Immigration, Réfugiés||
|and Čitizenship Cānada|et Citoyenneté Canada||

s.16(2)(c)
# PROTECTEDA PROTEGE ton

Wednesday, November 5th 01:13 – SWAT call ended 07:00 – SWAT call resumed 11:55 - SSC put up GCMS maintenance page 12:00 –SSC put up eServices maintenance page 12:09 – IRCC put up IRCC Portal – New Version maintenance page 14:01 - SSC took down GCMS and eServices maintenance pages 14:02 – IRCC took down IRCC Portal – New Version maintenance page 15:35 - SSC put up GCMS and eServices maintenance pages 15:37 - SSC put up IRCC Portal – New Version maintenance page 16:05 – SSC took down eServices maintenance page 16:19 – IRCC took down IRCC Portal – New Version maintenance page 16:45 - SSC took down GCMS maintenance page 18:00 – Vendorjoined the technical call 19:42 – SSC put up GCMS and eServices maintenance pages 19:38 - SSC put up IRCC Portal – New Version ( maintenance page 21: 13 – SSC took down GCMS and eServices maintenance pages 21:15 – IRCC took down IRCC Portal – New Version maintenance page 21:50 – SWAT call ended

Thursday, November 6th 07:30 – SWAT call resumed

|08:30 – Technical teams meeting with|to explore|
|---|---|
|memory leak on||
|10:30 – SSC applied a memory leak fix to 12:16-|servers|

became unhealthy and communications started to fail again 12:39 – SSC put up GCMS maintenance page 12:47 – SSC put up eServices maintenance page 13:00 – IRCC put up IRCC Portal – New Version maintenance page 14:45-was brought back up in a healthy state 14:31 – IRCC took down IRCC Portal – New Version maintenance page

## Page 3 of 4

1A-2025-13519-000032

Immigration, Réfugiés migration, Refugees and Citizenship Canadaet Citoyenneté Canada

|||et Citoyenneté Canada|
|---|---|---|
|Immigration, Refugees|Immigration, Réfugiés||
|and Čitizenship Cānada|et Citoyenneté Canada||

s.16(2)(c) PROTECTED APROTEGE A
14:34 - SSC took down GCMS and eServices maintenance pages and monitored GCMS health 17:28 – SSC put up GCMS and eServices maintenance pages to support an restart 17:00 – SSC implemented an temporary workaround so could clean up unused connections/sessions established between servers and so resources could be freed up on to avoid memory growth resulting in failovers. 19:16 –SSC took down GCMS and eServices maintenance pages and monitored GCMS health 17:30 – SWAT call ended

Friday, November 7th 08:00 – SWAT call resumed, GCMS monitoring continued and SWAT call ended 12:00 – SWAT call resumed, GCMS monitoring continued and SWAT call ended 13:00 – Go-No-Go meeting with AppDev Release Management, at which GCMS incident was confirmed resolved as of 2025-11-06 19:16

IT Teams ConsultedIRCC-feedback provided IRCC – DBA feedback provided

## Page 4 of 4

1A-2025-13519-000033

Immigration, Réfugiés migration, Refugees and Citizenship Canadaet Citoyenneté Canada

|||and Citizenship Canadaet Citoyenneté Canada|
|---|---|---|
|Immigration, Refugees|Immigration, Réfugiés||
|and Čitizenship Cānada|et Citoyenneté Canada||

s.16(2)(c)
# PROTECTEDA PROTEGE ton

Post Incident Report-FINAL Global Case Management System (GCMS)

# Full Outage

Report purpose: High Availability Response Team (HART) – Major Incident Coordination (MIC) drafts Post Incident Reports (PIR) to provide additional incident details to senior management about critical (P1) incidents affecting IRCC applications and systems and to provide input into the

HART-MIC works with internal and partner IT teams to review incident information before final publication. This report provides the final capture of the incident being reported.

This report is reviewed by the HART Manager and IT Service Management Director prior to

Target to post final PIRs is seven business days post-incident.

problem management process.

publishing the final version.

Final Report Publishing Date

## Priority

HART Ticket

### Partner Ticket (SSC)

Start Date and Time (EST)

### End Date and Time (EST)

Total Disruption Duration IT Service Component

## Issue Category

Root Cause Resolution

Primary Resolver Team

2025-11-17

## Critical (P1)

INC000001181147 (#1) INC000001181169 (#2) INC000001181258 (#3) INC000000870348 (#1) INC000000870705 (#2 and #3) 2025-11-04 07:15 (#1) 2025-11-04 10:30 (#2) 2025-11-04 15:50 (#3) 2025-11-04 09:58 (#1) 2025-11-04 14:26 (#2) 2025-11-04 17:30 (#3) 8 hours 19 minutes (incidents combined) Not applicable Application Issue Unknown INC000001181147 (#1) No intervention INC000001181169 (#2) Configuration change – updates installed, databases shutdown and disabled. restarted, and INC000001181258 (#3) Configuration change – IRCC DBA increased the timeout settings so the would be less sensitive. INC000001181147 (#1) No intervention

### Page 1 of 4

1A-2025-13519-000034

Immigration, Réfugiés migration, Refugees and Citizenship Canadaet Citoyenneté Canada

s.16(2)(c) PROTECTEDA PROTEGE ton
Immigration, Refugees Immigration, Réfugiés and Čitizenship Cānada et Citoyenneté Canada

INC000001181169 (#2) SSC

- INC000001181258 (#3) IRCC
Incident Description Global Case Management System (GCMS) experienced a full outage. Business ImpactGCMS

- Affected stakeholders: IRCC, CBSA, GAC, ESDC, Public clients
- ESDC partner users could not submit passport
but GCMS cannot process these applications in applications

- Public clients could not submit passport applications though IRCC Portal-New Version
- Public clients could not submit eTA applications, but CBSA cannot process these applications
- IRCC and partner users could not share biometric/biographic or immigration information with each other
- IRCC users could not process public client visiting/studying/working/ in Canada, permanent residency, refugee, Canadian citizenship, or official travel applications
- CBSA users could not process public client enforcement/facilitation/detention cases, refugee claims, and border crossing examinations, make referrals for Immigration hearings or assist airlines with passenger flight boarding allowance
- Public clients traveling to Canada risked travel delays and being held in CBSA secondary areas until GCMS is available
- IRCC and partner operations impaired with backlog clean up post-resolution eServices
- Affected stakeholders: IRCC, CBSA, Public clients
- Public clients cannot access or apply to various eServices
- Public clients cannot access Service Delivery Web Tools
- IRCC agents and partners cannot receive requests from public clients for IRCC services
- Passport Program may be affected
### IRCC Portal – New Version

### Page 2 of 4

1A-2025-13519-000035

Immigration, Réfugiés migration, Refugees and Citizenship Canadaet Citoyenneté Canada

|||et Citoyenneté Canada|
|---|---|---|
|Immigration, Refugees|Immigration, Réfugiés||
|and Čitizenship Cānada|et Citoyenneté Canada||

# PROTECTEDA PROTEGE ton

s.16(2)(c)
- Affected stakeholders: IRCC, Public clients
- Affected Program: Passport
- Public clients cannot submit domestic applications for individual adults whose passport is about to expire, is already expired, is lost, or is stolen
- Public clients cannot perform application updates nor obtain application status for applications already submitted
- Public clients cannot manage their accounts
- Public clients cannot complete payment for new submissions
High Level Timeline INC000001181147 (#1) Monday, November 3, 2025 7:37 – SSC INOT indicates GCMS degradation related to servers. HART was not engaged.

### Tuesday, November 4, 2025

00:00 – GCMS Major Release R35 began. 7:00 – GCMS RM engaged HART MIC. 7:15 – SSC put up GCMS maintenance page. 09:58 – SSC took down GCMS maintenance page.

INC000001181169 (#2) 10:32 – GCMS IM engaged HART MIC and the SWAT call resumed. 10:39 - SSC put up GCMS and eServices maintenance page. IRCC put up IRCC Portal-New Version maintenance page 11:07 – SSC provided new SSC INC ticket. 13:34-updates installed. 13:36 – SSC disabled and then restarted GCMS. 14:26 - SSC took down GCMS and eServices maintenance pages. 14:30 – IRCC took down IRCC Portal – New Version maintenance page).

INC000001181258 (#3) 16:00 – ESO engaged HART MIC. 16:17 - SSC put up GCMS and eServices maintenance pages. IRCC put up IRCC Portal – New Version maintenance page. 16:29 – IRCC DBA performed a configuration change on the

### Page 3 of 4

1A-2025-13519-000036

migration, Refugees Immigration, Réfugiés d Citizenship Canada et Citoyenneté Canada

# PROTECTED APROTEGE A

s.16(2)(c)
Immigration, Refugees Immigration, Réfugiés and Citizenship Canada et Citoyenneté Canada

17:30 - SSC took down GCMS and eServices maintenance pages. IRCC took down IRCC Portal – New Version maintenance page. IT Teams ConsultedIRCC – ESO: feedback provided

## Page 4 of 4

1A-2025-13519-000037

Immigration, Réfugiés migration, Refugees and Citizenship Canadaet Citoyenneté Canada

# PROTECTEDA PROTEGE ton

s.16(2)(c)
Immigration, Refugees Immigration, Réfugiés and Čitizenship Cānada et Citoyenneté Canada

## Post Incident Report-FINAL

### Global Case Management System (GCMS)

# Full Outage

Report purpose: High Availability Response Team (HART) – Major Incident Coordination (MIC) drafts Post Incident Reports (PIR) to provide additional incident details to senior management about critical (P1) incidents affecting IRCC applications and systems and to provide input into the problem management process.

HART-MIC works with internal and partner IT teams to review incident information before final publication. This report provides the final capture of the incident being reported.

This report is reviewed by the HART Manager and IT Service Management Director prior to publishing the final version.

Target to post final PIRs is seven business days post-incident.

Final Report Publishing Date 2025-12-30 Critical (P1)

#### Priority

INC000001186803 HART Ticket Partner Ticket (SSC) INC000000883068 2025-12-19 13:53 Start Date and Time (EST) End Date and Time (EST) 2025-12-19 15:50 Total Disruption Duration 1 hours 57 minutes IT Service Component Global Case Management System (GCMS) Network Issue Issue Category Known-SSC had disabled the Root Cause which caused to unreachable. This caused to automatically failover.

#### is an automated process to clean up

records that are out of date. SSC recreated the entries that would have been removed. Resolution became available again. Primary Resolver Team SSC Incident DescriptionGlobal Case Management System (GCMS) is experiencing

### a full outage.

Business Impact GCMS

- Affected stakeholders: IRCC, CBSA, GAC, ESDC, Public clients
- ESDC partner users can submit passport applications in but GCMS cannot process these applications
##### Page 1 of 2

1A-2025-13519-000038

migration, RefugeesImmigration, Réfugiés and Citizenship Canadaet Citoyenneté Canada

s.16(2)(c) PROTECTEDA PROTEGE ton
Immigration, Refugees Immigration, Réfugiés and Čitizenship Cānada et Citoyenneté Canada

- Public clients cannot submit passport applications though IRCC Portal-New Version
- Public clients can submit eTA applications, but CBSA cannot process these applications
- IRCC and partner users cannot share biometric/biographic or immigration information with each other
- IRCC users cannot process public client visiting/studying/working/ in Canada, permanent residency, refugee, Canadian citizenship, or official travel applications
- CBSA users cannot process public client enforcement/facilitation/detention cases, refugee claims, and border crossing examinations, make referrals for Immigration hearings or assist airlines with passenger flight boarding allowance
- Public clients traveling to Canada risk travel delays and being held in CBSA secondary areas until GCMS is available
- IRCC and partner operations impaired with backlog clean up post-resolution eServices
- Affected stakeholders: IRCC, CBSA, Public clients
- Public clients cannot access or apply to various eServices
- Public clients cannot access Service Delivery Web Tools-IRCC agents and partners cannot receive requests from public clients for IRCC services
- Passport Program may be affected
High Level Timeline 13:53-lost connection to until 14:15 14:09 – ESO engaged HART MIC; IRCC SWAT started 14:25-lost connection to again until 14:28 14:27 – SSC put up GCMS and eServices maintenance pages 14:57 – IRCC SD provided SSC INC 15:43 – SSC restarted the

## 15:50 – SSC took down GCMS and eServices maintenance

# pages once it was confirmed that was available and

functioning. IT Teams ConsultedIRCC – ESO: feedback provided IRCC – IM: feedback provided

### Page 2 of 2

1A-2025-13519-000039


<!-- CHUNK_BOUNDARY 1A-2025-13519_00000.md -->

