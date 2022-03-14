import pandas as pd


mesh = ['Allied Health Personnel','Community Health Services','Emergency Medical Services*','Emergency Medical Technicians*','Female','Humans','Infant','Qualitative Research',
        'Adult', 'Betamethasone', 'Case-Control Studies','Delivery, Obstetric','Demography','Female','Fetal Membranes, Premature Rupture','Gestational Age','Humans',
        'Infant, Newborn','Obstetric Labor, Premature','Pregnancy','Premature Birth','Prenatal Care','Prospective Studies','Regression Analysis','Respiratory Distress Syndrome, Newborn',
        'Risk Factors','Treatment Outcome','Crisis Intervention','Humans','Mass Screening','Perception','Referral and Consultation','Substance-Related Disorders',
        'Substance-Related Disorders','Adult','Child','Family Characteristics','Female','Humans','Income','Kenya','Male','Rural Population',''
        
         / therapeutic use*



 / statistics & numerical data

 / prevention & control*


 / drug therapy*

 / prevention & control*

 / statistics & numerical data*

 / etiology

/ diagnosis

* / therapy 

Vaccines* 

 Adolescent

Adult

Alphapapillomavirus*

Female

Gynecology*

Health Knowledge, Attitudes, Practice

Humans

Male

Middle Aged

Obstetrics*

Papillomavirus Infections* / prevention & control

Papillomavirus Vaccines*

Practice Patterns, Physicians'

Vaccination 

 Adolescent

Adult

Aged

Colonoscopy

Colorectal Neoplasms*

Early Detection of Cancer

Female

Financial Stress

Humans

Male

Middle Aged

Uterine Cervical Neoplasms* / diagnosis

Young Adult 

 Diabetes Mellitus* / therapy

Emigrants and Immigrants*

Humans

Mexico

Physicians* 

 Community Health Services

Decision Making

Decision Making, Shared

Female

Humans

Patient Participation*

Reproductive Health* 

 COVID-19* / complications

COVID-19* / epidemiology

COVID-19* / physiopathology

COVID-19* / therapy

Disease Management

Early Diagnosis

Humans

SARS-CoV-2 / isolation & purification*

Skin Diseases* / classification

Skin Diseases* / etiology

Skin Diseases* / therapy

Skin Diseases* / virology

Systemic Inflammatory Response Syndrome* / physiopathology

Systemic Inflammatory Response Syndrome* / therapy 

 Adult

Aged

Bandages / economics

Bandages / supply & distribution

Compression Bandages / economics

Compression Bandages / supply & distribution*

Dermatologic Agents / therapeutic use

Drug Eruptions / therapy

Female

Health Care Costs

Health Services Accessibility

Humans

Kenya

Leg Injuries / therapy

Leg Ulcer / therapy

Lymphedema / etiology

Lymphedema / therapy*

Male

Middle Aged

Sarcoma, Kaposi / complications

Skin Diseases, Vesiculobullous / chemically induced

Skin Diseases, Vesiculobullous / therapy

Varicose Ulcer / therapy

Wounds and Injuries / therapy*

Zinc Oxide / therapeutic use 

 Adult

Blacks*

Female

Health Education*

Health Knowledge, Attitudes, Practice

Hispanic or Latino*

Humans

Infant

Infant Care*

Male

Mothers / education*

Mothers / statistics & numerical data*

Sleep*

Surveys and Questionnaires

United States

Whites* 

 Adult

Asians

Blacks

Delayed Diagnosis

Diabetes Mellitus / ethnology*

Emigrants and Immigrants*

Female

Hispanic or Latino

Humans

Male

Mexican Americans

Middle Aged

Minority Groups / statistics & numerical data*

Nutrition Surveys

Prevalence

United States / epidemiology

Whites 

 Adult

Aged

Blacks / statistics & numerical data

Ethnicity / statistics & numerical data*

Female

Healthcare Disparities / statistics & numerical data*

Hispanic or Latino / statistics & numerical data

Humans

Insurance Coverage / statistics & numerical data*

Liver Transplantation / statistics & numerical data*

Male

Medicaid / statistics & numerical data*

Middle Aged

Minority Groups / statistics & numerical data

Patient Protection and Affordable Care Act

United States

Waiting Lists

Whites / statistics & numerical data 

 Adult

Cross-Sectional Studies

Delivery of Health Care / statistics & numerical data*

Diabetes Mellitus / diagnosis

Disease Management*

Female

Financing, Personal / statistics & numerical data*

HIV Testing

Health Knowledge, Attitudes, Practice

Humans

Hypertension / diagnosis

Income

Insurance Coverage / statistics & numerical data*

Kenya

Male

Mass Screening*

Middle Aged

Rural Population

Tuberculosis / diagnosis

Uterine Cervical Neoplasms / diagnosis

Young Adult 

 Cyclonic Storms*

Disasters*

Economic Factors

Female

Haiti / epidemiology

Humans

Sexual Behavior 

 Aged

Cross-Sectional Studies

Ethnicity

Female

Humans

Male

Medicare Part D*

Medication Therapy Management

United States

Whites 

]


#Create a dictionary from previous indexing MeSH terms with term as key, total count of term occurrences as value
def PI_dict(terms):
    dict = {}
    for i in terms:
        if i in dict:
            dict[i] += 1
        else:
            dict[i] = 1      
    return dict


def PI_data(term_list):
    PIs = PI_dict(term_list)
    PIs = dict(sorted(PIs.items(), reverse=True, key=lambda t: t[::-1]))
    total = sum(PIs.values())

    for key, value in PIs.items():
        pct = value * 100 / total
        PIs[key] = round(pct, 2)

    PI_k = sorted(PIs, key=lambda x: (-PIs[x], x))
    PI_v = list(PIs.values())

    PI_sorted_dict = {
                      'PI 1':PI_k[0], 'PI 1 %':PI_v[0], 'PI 2':PI_k[1], 'PI 2 %':PI_v[1], 'PI 3':PI_k[2], 'PI 3 %':PI_v[2],
                      'PI 4':PI_k[3],'PI 4 %':PI_v[3], 'PI 5':PI_k[4], 'PI 5 %':PI_v[4], 'PI 6':PI_k[5], 'PI 6 %':PI_v[5], 
                      'PI 7':PI_k[6], 'PI 7 %': PI_v[6], 'PI 8':PI_k[7], 'PI 8 %':PI_v[7], 'PI 9':PI_k[8], 'PI 9 %':PI_v[8], 
                      'PI 10':PI_k[9], 'PI 10 %':PI_v[9], 
                      'Total PIs':total}
    return PI_sorted_dict 


df_source = pd.read_csv('ACTS_CTSI_Health_Equity_Articles_20220209.csv')

top_mesh = PI_data(mesh)

print(top_mesh)