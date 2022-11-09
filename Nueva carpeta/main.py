## Instalar pandas
## Cambiar formato de .txt a .py de este archivo 

import pandas as pd
import time

OLD_FILE = 'archivo old.csv'
NEW_FILE = 'archivo new.csv'

# quedarse sin duplicados y los duplicados llevarlos a otro archivo de duplicados.
# ['LOT_ID', 'COMPL_H_ID', 'COMPL_V_ID', 'EQUIPMENT_ID', 'EQUIPMENT_CODE', 'EQPT_CABLE_NUM_IN', 'EQPT_PORT_NUM', 'EQPT_CO_CODE', 'OLT_CLIENT_IDENT']
class Comparacion:

    def readCSV(self, OLD_FILE, NEW_FILE):
        df_1 = pd.read_csv(OLD_FILE, sep='|', quotechar='\'', encoding='latin-1', low_memory=False)
        df_2 = pd.read_csv(NEW_FILE, sep='|', quotechar='\'', encoding='latin-1', low_memory=False)

        return df_1, df_2

    def compaire2File(self, df_1, df_2):
        with open(OLD_FILE, 'r', encoding='latin-1') as csv1, open(NEW_FILE, 'r', encoding='latin-1') as csv2:
            import1 = csv1.readlines()
            import2 = csv2.readlines()

        df_1, df_2 = self.readCSV(df_1, df_2)
        df_aux1 = df_2.columns.copy()
        df_aux2 = df_2.columns.copy()

        ''' Eliminados '''
        df_aux2 = df_1.merge(df_2, indicator=True, how='outer')
        df_aux2_diff = df_aux2.loc[lambda x: x['_merge'] != 'both']
        df_aux2_diff_2 = df_aux2_diff.loc[lambda x: x['_merge'] != 'right_only']
        df_aux2_diff_2.to_csv('Eliminados.csv', index=False)

        ''' Agregados '''
        df_aux11 = df_1.merge(df_2, indicator=True, how='outer')
        df_aux11_diff = df_aux11.loc[lambda x: x['_merge'] != 'both']
        df_aux11_diff_11 = df_aux11_diff.loc[lambda x: x['_merge'] != 'left_only']
        df_aux11_diff_11.to_csv('Agregados.csv', index=False)

        ''' Duplicados '''
        df_aux11 = df_1.merge(df_2, indicator=True, how='outer')
        df_aux11_diff = df_aux11.loc[lambda x: x['_merge'] != 'both']
        df_aux11_diff.to_csv('Duplicados.csv', index=False)

start = time.time()
c1 = Comparacion()
c1.compaire2File(OLD_FILE, NEW_FILE)
end = time.time()
print((end - start), 'Secs.')
print('Proceso terminado!!')
