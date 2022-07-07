import os
import argparse
from datetime import datetime

from cnpj import Cnpj


OUTPUT_FILE_NAME = 'cnpjs.csv'

def print_count_log(count, total_count, end_line="\n"):
    print(f"{count}/{total_count}", end=end_line)

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
    csv_sep = args.sep_csv
    quantity_cnpj_to_be_generated = args.quantity

    print('Começando em: '+str(datetime.now().time().strftime('%H:%M:%S')))

    output_file_path = os.path.join(dir_output, OUTPUT_FILE_NAME)
    csv_header = 'cnpj_basico,cnpj_ordem,cnpj_dv,cnpj'

    with open(output_file_path,'w') as f:
        f.write(csv_header)
        next_cnpj = initial_cnpj

        for i in range(quantity_cnpj_to_be_generated):
            print_count_log(
                count=i+1,
                total_count=quantity_cnpj_to_be_generated,
                end_line='\r'
            )

            new_cnpj = Cnpj(str(next_cnpj))
            row_content = csv_sep.join([
                new_cnpj.cnpj_basico,
                new_cnpj.ordem,
                new_cnpj.dv,
                str(new_cnpj)
            ])

            f.write('\n' + row_content)
            next_cnpj +=1
            
        print_count_log(
            count=i+1,
            total_count=quantity_cnpj_to_be_generated
        )       

    print('Terminando em: '+str(datetime.now().time().strftime('%H:%M:%S')))
