from datetime import datetime
from cnpj import Cnpj

INITIAL_CNPJ = 46208711
QUANTITY = 100000

DIR_OUTPUT = 'C:\\Dev\\'
COMA_SEPARATOR = ','

if __name__ == "__main__":
   
    print('Começando em: '+str(datetime.now().time().strftime('%H:%M:%S')))
    
    with open(DIR_OUTPUT+'cnpjs.csv','w') as f:
        f.write('cnpj_basico,cnpj_ordem,cnpj_dv,cnpj\n')
        next_cnpj = INITIAL_CNPJ

        for i in range(QUANTITY):
            print(str(i+1) +' / '+ str(QUANTITY), end='\r')
            new_cnpj = Cnpj(str(next_cnpj))
            f.write(new_cnpj.cnpj_basico + COMA_SEPARATOR + new_cnpj.ordem + COMA_SEPARATOR + new_cnpj.dv + COMA_SEPARATOR + str(new_cnpj) +'\n')
            next_cnpj +=1

        print(str(i+1) +' / '+ str(QUANTITY))        

    print('Terminando em: '+str(datetime.now().time().strftime('%H:%M:%S')))
