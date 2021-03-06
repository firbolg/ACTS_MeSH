import pandas as pd
import csv

def getmesh(citations):
    mesh = 'MH  -'
    mod = [i.split('\n') for i in citations]
    combined = [i for sublist in mod for i in sublist]
    mesh = [i for i in combined if i.startswith('MH  - ')]
    mesh = [i.split('/') for i in mesh]
    PIs = []
    for i in mesh:
        for w in i:
            if w.startswith('MH  - *'):
              w = (w[7:])
              PIs.append(w)
            if w.startswith('MH  - '):
              w = (w[6:])
              PIs.append(w)
            else:
              pass
    return PIs

def getkeywords(citations):
    keywords = 'OT  -'
    mod = [i.split('\n') for i in citations]
    combined = [i for sublist in mod for i in sublist]
    keywords = [i for i in combined if i.startswith('OT  - ')]
    keywords = [i.split('/') for i in keywords]
    kw = []
    for i in keywords:
        for w in i:
            if w.startswith('OT  - *'):
              w = (w[7:])
              kw.append(w)
            if w.startswith('OT  - '):
              w = (w[6:])
              kw.append(w)
            else:
              pass
    return kw


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

    PI_k = sorted(PIs, key=lambda x: (-PIs[x], x))
    PI_v = list(PIs.values())

    new_dict = {'MeSH Term':PI_k, 'Total':PI_v}

    #PI_sorted_dict = {
                    #  'PI 1':PI_k[0], 'PI 1 %':PI_v[0], 'PI 2':PI_k[1], 'PI 2 %':PI_v[1], 'PI 3':PI_k[2], 'PI 3 %':PI_v[2],
                     # 'PI 4':PI_k[3],'PI 4 %':PI_v[3], 'PI 5':PI_k[4], 'PI 5 %':PI_v[4], 'PI 6':PI_k[5], 'PI 6 %':PI_v[5], 
                    #  'PI 7':PI_k[6], 'PI 7 %': PI_v[6], 'PI 8':PI_k[7], 'PI 8 %':PI_v[7], 'PI 9':PI_k[8], 'PI 9 %':PI_v[8], 
                     # 'PI 10':PI_k[9], 'PI 10 %':PI_v[9], 
                     # 'Total PIs':total}

    return new_dict


df_source = pd.read_csv('ACTS_CTSI_Health_Equity_Articles_20220209.csv')

f = open('pubmed.txt', 'r')

top_mesh = PI_data(getmesh(f))
top_keywords = PI_data(getkeywords(f))

df = pd.DataFrame(top_mesh)
df1 = pd.DataFrame(top_keywords)

df.to_csv('MeSH Totals.csv')
df1.to_csv('Keyword Totals.csv')


