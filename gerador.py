from datetime import datetime
from cnpj import Cnpj

# 8 primeiros dígitos do CNPJ a ser gerado, esse é o valor que será incrementado, caso precise fazer outra sequência basta trocar esse valor
INITIAL_CNPJ = 46208711 
# Quantidade de CNPJs a serem gerados
QUANTITY = 10000


# Diretório onde será gerado o arquivo
DIR_OUTPUT = ''
# Caractere de separação entre as colunas do .csv
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
