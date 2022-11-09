p = 0
i = 0
j = 0
o = 0
pivote = 0
fila = 0

for i, sig in array_sig.iterrows():
    for j, osp in array_osp.iterrows():

        #Caso 1: Ambas tablas coinciden
        if(sig['FTTH'] == osp['FTTH'] and sig['ID'] == osp['ID']):
            fila = pd.DataFrame({'FTTH': [sig['FTTH']], 'ID': [sig['ID']]})
            #dataLoader = pd.concat(dataLoader, fila)
            
            print('Verdadero => {} = {}'.format(sig["ID"], osp["ID"]), 'valor de i: ', i)
            break
        
        #Caso 2: El valor de SIGRES no está libre en OSP4
        elif sig['ID'] in array_osp:
            for o, file_osp in array_osp.iterrows():
                if(pivote in array_osp):
                    pivote = file_osp[o]

                    fila = pd.DataFrame({'FTTH': [sig['FTTH']], 'ID': [sig['ID']]})
                    # dataLoader = pd.concat(dataLoader, fila)

                    print('NO LIBRE => {} = {}'.format(sig["ID"], osp["ID"]), 'valor de i: ', i)
                    
                    if(pivote > 64 or pivote < 0):
                        pivote = 0
                else:
                    print('El archivo no cuenta con filas pivoteables')

        #Caso 3: El valor de SIGRES está libre en OSP
        else:
            print('FALSO | ID SIGRES: {} ID OSP: {}'.format(sig["ID"], osp["ID"]), 'Valor de i: ', i)
            break

            # fila = pd.DataFrame({'FTTH': [sig['FTTH']], 'ID': [sig['ID']]})
            #dataLoader = pd.concat(dataLoader, fila)
        
        