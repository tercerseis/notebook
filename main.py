import pandas as pd
import numpy as np

OSP_FILE = 'osp_3.csv'
SIG_FILE = 'sig_3.csv'

#Dataframes para DataLoader y tablas auxiliares
dataLoader = pd.DataFrame()
osp_aux = pd.DataFrame()
sig_aux = pd.DataFrame()

file_osp = pd.read_csv(OSP_FILE, delimiter=';', encoding='UTF-8', low_memory=False, on_bad_lines='skip')
file_sig = pd.read_csv(SIG_FILE, delimiter=';', encoding='UTF-8', low_memory=False, on_bad_lines='skip')

#Tablas auxiliares
file_osp_aux = pd.read_csv(OSP_FILE, delimiter=';', encoding='UTF-8', low_memory=False, on_bad_lines='skip')
file_sig_aux = pd.read_csv(SIG_FILE, delimiter=';', encoding='UTF-8', low_memory=False, on_bad_lines='skip')

array_osp = file_osp[['FTTH', 'ID']]
array_sig = file_sig[['FTTH', 'ID']]
emptyDF = pd.DataFrame()

#Seleccion de puertos 
#array_osp = file_osp[['FTTH', 'PUERTO', 'ID']]
#array_sig = file_osp[['FTTH', 'PUERTO', 'ID']]

p = 0
i = 0
j = 0
o = 0
pivote = 0

for i, sig in array_sig.iterrows():
    for j, osp in array_osp.iterrows():

        #Caso 1: Ambas tablas coinciden
        if(sig['FTTH'] == osp['FTTH'] and sig['ID'] == osp['ID']):
            i+=1
            break
        
        #Caso 2: El valor de SIGRES no está en OSP
        elif sig['ID'] in array_osp.iterrows():
            dataLoader['NS_FTTH'] = file_sig['FTTH']
            dataLoader['OSP'] = file_sig['ID']
            i+=1
            break

        #Caso 3: El valor de SIGRES si está en OSP
        else:
            for o, file_osp in array_osp.iterrows():
                if(pivote in array_osp.iterrows()):
                    pivote = file_osp[o]
                    dataLoader['NS_FTTH'] = file_osp['FTTH']
                    dataLoader['OSP'] = pivote
                    p+=1
                    i+=1
                    break
                else:
                    p+=1
                    break
        

        
        

        
dataLoader