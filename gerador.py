import argparse
from datetime import datetime

from cnpj import Cnpj


if __name__ == "__main__":

    parser = argparse.ArgumentParser(description='Projeto gerador CNPJs válidos salvos em formato CSV.')

    parser.add_argument('-i','--initial_cnpj', 
                        type=int,
                        default=46208711, 
                        help=(
                            "8 primeiros dígitos do CNPJ a ser gerado, " 
                            "esse é o valor que será incrementado, caso precise fazer outra sequência "
                            "basta trocar esse valor."))
    parser.add_argument('-q','--quantity', 
                        type=int, 
                        default=1000,
                        help="Quantidade de CNPJs a serem gerado.")
    parser.add_argument('-o','--output_path', 
                        type=str, 
                        default='',
                        help= "Diretório onde será gerado o arquivo.")
    parser.add_argument('-s','--sep_csv', 
                        type=str, 
                        default=',',
                        help= "Caractere de separação entre as colunas do `.csv`.")

    args = parser.parse_args()    
    initial_cnpj = args.initial_cnpj
    dir_output = args.output_path
    cvs_sep = args.sep_csv
    quantity_cnpj_to_be_generated = args.quantity

    print('Começando em: '+str(datetime.now().time().strftime('%H:%M:%S')))

    with open(dir_output+'cnpjs.csv','w') as f:
        f.write('cnpj_basico,cnpj_ordem,cnpj_dv,cnpj\n')
        next_cnpj = initial_cnpj

        for i in range(quantity_cnpj_to_be_generated):
            print(str(i+1) +' / '+ str(quantity_cnpj_to_be_generated), end='\r')
            new_cnpj = Cnpj(str(next_cnpj))
            f.write(new_cnpj.cnpj_basico + cvs_sep + new_cnpj.ordem + cvs_sep + new_cnpj.dv + cvs_sep + str(new_cnpj) +'\n')
            next_cnpj +=1

        print(str(i+1) +' / '+ str(quantity_cnpj_to_be_generated))        

    print('Terminando em: '+str(datetime.now().time().strftime('%H:%M:%S')))
