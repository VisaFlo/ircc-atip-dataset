# IEC Work Permit Eligibility Model: GBA+ Report (8p)

> Source: IRCC record released under the Access to Information Act. published by IRCC (open.canada.ca).
> Text below is local-OCR output of the scanned release and carries OCR noise; the release PDF is authoritative.

---

Gender-Based
Analysis Plus
Automated triage and positive
eligibility determinations of
International Experience Canada
Work Permit Applications
1. Background
Immigration, Refugees and Citizenship Canada (IRCC) issues work permits under the Temporary Foreign Worker Program
(TFWP) and the Internationality Mobility Program (IMP). The TFWP requires Canadian employers to obtain a labour
market impact assessment (LMIA) from ESDC, while the IMP allows employers to hire foreign workers without the need
for an LMIA. IRCC issues two kinds of work permits under the IMP: one that is open, allowing the holder to work for any
employer, and another that restricts the holder to the employer listed on the work permit. In 2022, IRCC issued work
permits to approximately 554,000 foreign nationals; over 470,000 (85%) of these were issued under the IMP and over
84,000 (15%) under the TFWP.

Under the IMP’s International Experience Canada (IEC) program, IRCC issues both open and employer-specific work
permits under three categories:

       Working Holiday (WH) - open work permit
       Young Professionals (YPP) - employer specific work permit
       International Co-op (ICP) - employer specific work permit

Namely, under the IEC, IRCC manages Canada’s bilateral youth mobility instruments that facilitate work and travel
authorizations for youth aged 18 to 35. Currently, Canada has signed youth mobility instruments with over 35 country
and territory partners spanning Europe, Oceania, East Asia, and the Americas. To ensure that the program is as inclusive
as possible, IEC works with partner countries and territories, and stakeholders to identify barriers to youth mobility, and
to develop resources and strategies that will help mitigate those barriers for Canadian and foreign national youth.
Following significant Covid-related disruption to this program in 2020 and 2021, when IEC intake and processing were
placed on hold, numbers have now returned to pre-pandemic levels: in 2022, IEC intake was 72,491 and output was
70,864. This represents approximately 15% of the total IMP caseload and 13% of the total IRCC work permit caseload in
2022 .
In response to record high application inventories and a Ministerial announcement to raise IEC’s global annual quota by
20%, the Department has developed an automated triage tool to assist in the processing of IEC applications.
The tool is designed to apply pre-defined triage criteria created by officers to:

        a. Identify routine cases where the eligibility portion of the decision can receive a positive eligibility
           determination (Tier 1)
        b. Triage remaining applications to support more efficient manual eligibility assessments (Tier 2)

No artificial intelligence or advanced analytics techniques were used in the creation of the triage criteria. The eligibility
assessments are based on human-devised business rules only. The model triages IEC WP applications by grouping files
with similar characteristics based on the regulatory authority for each sub-program and participating country or
territory. The criteria that inform the model are the same that currently exist and that officers would currently examine
(i.e. the model is automating something that is currently done manually).

Eligibility criteria used to determine how applications are sorted into the bins is based on the eligibility requirements
outlined in IEC’s Youth Mobility Arrangements and Agreements (YMAs) with the existing partner countries and the
Department’s existing admissibility requirements.




                                                                                                                                1
2. Expected Overall Impact
Ultimately, the triage model should reduce decision-maker time per application by copying routinely-searched-for
information on each application and client from the Department’s Global Case Management System (GCMS) and
displaying this information with the triage bins in a single unified view (output spreadsheet).

The model’s overall impact on clients is expected to be minimal given that the model neither refuses applications nor
makes any form of negative recommendation but instead assigns applications into one of the bins.

It is worth noting, however, that the Department maintains control over how to distribute any gains in efficiency that
the use of the model brings about. More generally, it is expected that the use of the model will lead to an overall
decrease in processing times for applicants in all bins.

3. Analytical Method
This initial analysis proceeds primarily by comparing, along different dimensions, the proportion of applications in an
inventory before it is run through the model to the proportion of applications in the Tier 1 and Tier 2 bins after
assessment. Any significant variations, or lack thereof, are then noted and discrepancies are explained. Sometimes raw
data tables appear to show differential impacts of the model, but contextual knowledge is important and sometimes
discrepancies are explained by the particularities of certain client groups and the parameters of bilateral agreements,
which can vary from one country to another. For example, while applicants from some countries may represent a larger
share of applications in the overall inventory, their citizens may only have access to IEC’s Young Professional and
International Co-op categories (i.e. no access to Working Holiday program). They would, therefore, always be triaged to
the Tier 2 bin, as these categories require manual officer review due to eligibility requirements outlined in the bilateral
Youth Mobility Arrangements.

It should be noted that the main inventory used to test the model is composed of open applications from the current IEC
2023 season. In addition, the report relies on data (see section 5, tables 12 & 13) that contain closed/finalized
applications from two past IEC seasons (2019 & 2022), to allow for an analysis of whether approval and refusal rates
change with the introduction of the new automated triage.

4. GBA Plus Data Tables – Model Development and Testing Data
Gender
                                                                 Table 1: Testing Dataset by applicants Gender
According to the last evaluation of the IEC program, conducted       Gender          Total #        Total %
by IRCC’s Research and Evaluation Branch in 2019, approximately       Male           10288            48%
half of IEC foreign national youth participants were women. This     Female          11119            52%
is consistent with the gender distribution within the data set        Other            4              0%
used to test and develop the model.                                   Total          21411           100%

This data set contained                               Table 2: Testing Dataset by Bin and Gender
21,411 open applications            Bins:        Other Female #       % of Female      Male # % of Male            Total #
from the current IEC 2023         Tier 1 Bin       0        3316           48%          3633     52%                6949
season inventory, 11,119
                                  Tier 2 Bin       4        7790           54%          6644     46%                14438
(52%) of which had female
                                 Withdrawal        0         13            54%            11     46%                 24
applicants, while 10,288
(48%) had male applicants.          Total          4       11119                        10288                       21411


                                                                                                                              2
When these applications were run through the model, 6,949 applications were triaged into the Tier 1 Bin and 14,438
into the Tier 2 Bin.

The gender profile of these bins is very similar to the initial data set. In the Tier 1 Bin, 3,316 (48%) applicants were
female, while 3,633 (52%) were male. There is a slightly higher percentage of female applicants in the Tier 2 Bin, where
from 14,438 applications passed in this bin, 54% of applicants were female and 46% male. This is likely attributable to
the fact that the Tier 2 Bin has a higher volume of applications overall, as it contains applications for employer-specific
categories and all applications which require assessment of other bin-specific parameters such as Police Certificates,
Travel History, and Medical Requests. Although there is no obvious single cause of the minor gender differences
between these bins, the data allows us to reflect on numerous potential causes. One potential conclusion is that this
data reflects the more general over-representation of females in fields that interact with vulnerable populations (e.g.
children, the elderly). As a result, these applications would require a little more scrutiny, involving some form of criminal
check and/or a medical history check. Of note, when the model was tested/evaluated against the data set from two past
IEC seasons, this gender gap in Tier 2 Bin appears non-existent (see section 5, tables 8 & 9). This further confirms that
the model did not result in any major differential output along the dimension of gender.

Country of Citizenship
The potential for the automated triage model to introduce differential impacts along the citizenship dimension is
severely limited by the fact that criteria for triaging are set on either eligibility requirements stipulated in the unique
YMAs that Canada has with each country or territory partner, or departmental admissibility requirements (e.g. police
certificate, medical requests).

                             Table 3 Total Dispersion Across Bins Based on Country of Citizenship
                    Bins:                           # of total applications                % of Total applications
                    Bin 1:                                   6944                                   33%
                    Bin 2:                                  14331                                   67%
                    Total:                                  21275*                                 100%
*Please note discrepancy between Total in table 3 and table 4 as table 4 only references the top 10 countries of citizenship in terms of size rather
than all countries

Tier 1 Bin
A moderate percentage (33%) of applications end up in the Tier 1 Bin. This bin contains Working Holliday applications
that meet the specific eligibility criteria for different subsets of participating countries, and have no other admissibility
factors to review (such as travel history, medical requests).
A higher percentage (60%) of applications from the participating countries in Tier 1 also end up in the Tier 2 Bin when
applications did not meet different regulatory criteria for the IEC Working Holiday category (e.g. there is travel history
on file which triggers an additional police certificate request) and when these countries have applications for the
employer specific categories
Established rules for police certificate requirements were set by IRCC’s International Network when Global Affairs
Canada administered the program, and any new country or territory partners that join the program adopt police
certificate requirements consistent with the requirements established by the Department for other work permit lines of
business.
Tier 2 Bin
The Tier 2 Bin contains the largest number of applications (67%), as any applications with a travel history of more than
six months are triaged here for assessment and additional police certificates/medical requests. In addition, all
applications for the Young Professional and International Co-op categories are triaged into this bin to assess employer-
                                                                                                                                                       3
specific requirements (review of job offers, NOC codes and education credentials). One hundred per cent of applications
from some countries, including Costa Rica, Hong Kong, Italy, Latvia, Lithuania, South Korea, Switzerland and Taiwan, end
up in the Tier 2 Bin due to the need to either review eligibility requirements stipulated in the YMAs or admissibility
requirements set by the Department. For example:

        All applicants from Costa Rica are visa required and are triaged into this bin due to the need to issue a visa
         counterfoil, rendering applications from this country ineligible for bulk approval.
        All applicants from Hong Kong require the issuance of a special police certificate request letter that allows their
         citizens to obtain the correct document from Hong Kong authorities.
        All applicants from Italy must have a residency certificate on file to satisfy residency requirements stipulated by
         the Italian government in the youth mobility arrangement.
        Applications from Latvia, Lithuania, South Korea and Taiwan all require an upfront medical exam; therefore, the
         processing officer’s action is necessary.

Please see below for a table emphasizing the dispersion of applicants country of citizenship through each bin. To ensure
the integrity of the analysis, the table lists the ten highest citizenship totals per country from the sample data (with more
than 500 applications). Other countries may not be listed as their sample size was not large enough to be able to draw
any definitive conclusions. Each country listed has been triaged through the model using pre-existing bilateral
agreements to ensure the models efficacy.
                                   Table 4 Applicants Country of Citizenship dispersed through each bin
Country of citizenship   Tier 1 Bin # of Apps Tier 1 Bin % of Apps Tier 2 Bin # of Apps Tier 2 Bin % of Apps   Total:   % of Total
France                           2377                   37%                     4016                  63%       6403       30%
Korea Republic of                  0                     0%                     2195                 100%       2198       10%
UK - British citizen              709                   39%                     1087                  60%       1798       8%
Australia                         585                   36%                     1027                  64%       1613       8%
Republic of Ireland               613                   43%                      822                  57%       1438       7%
Japan                             682                   49%                      706                  51%       1390       7%
Germany                           564                   44%                      730                  56%       1294       6%
Chile                             603                   52%                      555                  48%       1158       5%
Taiwan                             0                     0%                      922                 100%       922        4%
New Zealand                       203                   40%                      310                  60%       513        2%
Total                            6336                                          12370                           18727

Age
Due to the nature of the program, IEC has a diverse range of applicants between the ages of 18 and 35 years old.
According to the last evaluation of the IEC Program, conducted by IRCC’s Research and Evaluation Branch in 2019, most
(77%) foreign national youth admitted to Canada under IEC were between 21 and 29 years old when they started their
IEC experience. Participants under the Young Professionals stream were slightly older, with a greater share (21%) falling
into the 30 to 35 age group. Foreign national youth participants from the International Co-op stream were slightly
younger than the other streams, with a greater share in the 18 to 20 age group (19%).

The data set used to test and develop the model shows results                      Table 5: Total Age Distribution Table
similar to those from the evaluation of the program.                             Age       Total #         % of Bin total
                                                                                18-20       2670                12%
Many (33%) younger applicants who have recently graduated                       21-23       4552                21%
secondary school take gap years, look for a working holiday
                                                                                24-26       5145                24%
experience, or take advantage of the International Co-op stream to
                                                                                27-29       4332                20%
fulfill their post-secondary academic requirements. There is also an
                                                                                30-32       2808                13%
influx of older applicants in the 30-35 age group who apply to the
                                                                                 33+        1903                 9%
Young Professional category to gain professional experience to
                                                                                Total      21410               100%
contribute to career development.
                                                                                                                                     4
Tier 1 and Tier 2 Bins

The spread of age ranges remains very similar across Tier 1 and Tier 2 bins. Given that Tier 2 Bin is accepting all
applications which were not triaged into the Tier 1 Bin, it is by far larger in terms of the number of applications that it
contains. Yet, the age dispersion within the Tier 2 Bin is largely consistent with the Tier 1 Bin and the overall age
distribution within the program.

          Table 6 Tier 1 Bin: Age Distribution Table                       Table 7 Tier 2 Bin: Age Distribution Table
    Age           Total #              % of Bin total               Age            Total #             % of Bin total
   18-20           1023                     15%                    18-20            1646                    11%
   21-23           1684                     24%                    21-23            2962                    21%
   24-26           1666                     24%                    24-26            3471                    24%
   27-29           1313                     19%                    27-29            3013                    21%
   30-32            779                     11%                    30-32            2027                    14%
    33+             584                     8%                       33+            1318                     9%
    Total          7049                    100%                     Total          14437                   100%


Through the collection of data regarding the age distribution between the bins, there does not appear to be a strong
correlation between age and bin distribution. It is not a determining factor in how an application is triaged across the
bins. However, age dispersions are an important aspect of intersectional analysis. An applicant’s age can affect their
financial status, willingness to travel abroad, education level, and other deciding factors. Although the parameters of
each bin do not explicitly outline these factors, this analysis allow us to better understand foreign travellers' patterns
better relative to their age group. Of note, very similar results were obtained when the model was tested against
historical data for two previous IEC seasons (see section 5, tables 10 & 11).



    5. Validating the automated triage model
Data tables from previous IEC seasons (2019 & 2022) allow us to draw additional conclusions regarding the effectiveness
of the triage model. The two identity factors we focused on were gender and age. We also looked into the approval and
refusal rate of closed/finalized applications from the past seasons to see if it changes with the introduction of the
automated triage.

Data tables with bin and gender distribution across 2019 and 2022 IEC seasons

                                     Table 8: Historical Dataset by Bin and Gender (2019)
                   Bins:          Another gender      Female      % of female    Male     % of Male          Total
                  Tier 1                1              18338          49%       18858       51%              37197
                  Tier 2                0              20748          48%       22194       52%              42942
                Withdrawal              0                64           60%         43        40%               107
                   Total                1              39150          49%       41095       51%              80246




                                                                                                                              5
                                    Table 9: Historical Dataset by Bin and Gender (2022)
                    Bin            Other    Female        % of Female       Male      % of Male             Total #
                  Tier 1             7        16818             49%            17407            51%         34232
                  Tier 2             4        18080             50%            18416            50%         36501
                Withdrawal           0             1         100%                0              0%             1
                   Total             11       34899             49%            35823            51%         70734


Data tables with total age distribution across 2019 and 2022 IEC seasons


         Table 10: Total Age Distribution Table (2019)                        Table 11: Total Age Distribution Table (2019)
 Age           Total #            % of Bin Total                      Age            Total #           % of Bin Total
 18-20                   12951                           16%          18-20                    9120                               13%
 21-23                   18712                           23%          21-23                    16623                              24%
 24-26                   20354                           25%          24-26                    18344                              26%
 27-29                   15985                           20%          27-29                    14412                              20%
 30-32                     7819                          10%          30-32                    7805                               11%
 33+                       4425                           6%          33+                      4388                               6%
 Total                   80246                           100%         Total                    70692                          100%

Further analysis of this age and gender historical data and comparison to the results within the current data set used to
develop the triage model is referenced previously in the document.

Data tables with final decisions for 2019 & 2022 IEC seasons

By testing the model against historical data for both the 2019 and 2022 seasons, the model successfully triaged all Tier 1
applicants, as those applications maintained a 100% approval rate by officers during both seasons (see tables 12 & 13).
Since the historical data was not used to develop the model, the test set is therefore deemed to be unbiased.

We also notice that in the Tier 2 Bin for both seasons, a high percentage (n=>80) of applications were approved. This
suggests the potential for a future iteration of the triage model to triage more applications into the Tier 1 Bin, allowing
more clients to benefit from an automated positive eligibility determination.

                         Table 12: FinDec Post Bin Triage - Year 2019
 Bin        Approved (#) Approved (%) Refused (#) Refused (%)          Total (#)   Total (%)
 Tier 1           37197             100%              0             0%      37197       46%
 Tier 2           34653              81%          8289             19%      42942       54%
 Withdrawal            0              0%            107           100%         107        0%
 Total            65975                           4759                      80246      100%


                         Table 13: FinDec Post Bin Triage - Year 2022
 Bin        Approved (#) Approved (%) Refused (#) Refused (%) Total (#)      Total (%)
 Tier 1           34227             100%               5            0% 34232        48%
 Tier 2           31748              87%           4753            13% 36501        52%
 Withdrawal            0              0%               1          100%     1         0%
 Total            65975                            4759                70734      100%

                                                                                                                              6
    6. Conclusion

Data from the testing stage indicated that the model does not appear to have any significant, disproportionate impact
on clients. Assignments into the Tier 1 and Tier 2 bins appear to be in accordance with the established eligibility rules
and the notable variances are easily understood following a review of the data.

In terms of gender profile, the distribution within the Tier 1 and Tier 2 bins are very similar to the related profiles in the
testing dataset and model implementation. Thus, the model did not result in any major differential output along the
dimension of gender. However, further analysis of the seemingly minor gender difference across Tier 2 in comparison to
Tier 1 revealed that this is likely attributed to the fact that the Tier 2 Bin contains a higher volume of applications overall,
including applications for IEC employer-specific categories and all applications that require assessment of other bin-
specific parameters, such as Police Certificates, Travel History, and Medical Requests.

In addition, an examination of the country of citizenship data revealed that the model eligibility approval rate is being
accordingly distributed based on the model rules. If some applicants are missing out on a potential benefit by virtue of
being from a particular country, this is due to the strict eligibility requirements stipulated in the unique YMAs that
Canada has with each country or territory partner, or due to departmental admissibility requirements, but not to the
model itself.

In the case of age, it is to be noted that the spread of age ranges remains more or less consistent across bins as it is not a
determining factor when applications are assessed prior to going into the bins.

In sum, it is observed that application assignments into the Tier 1 and Tier 2 bins does not appear to introduce any new
unintended bias into application processing. As a result, it does not appear that the model will have any significant,
disproportionate impact on different groups of clients




                                                                                                                               7
