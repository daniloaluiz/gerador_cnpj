from datetime import datetime

LENGTH_CNPJ = 14
INITIAL_CNPJ = 46208711
RANGE =100
COMA_SEPARATOR = ','

def completa_cnpj(cnpj):
    cnpj = list(map(int,cnpj)) + [0, 0, 0, 1]
    for _ in range(2):
        value = sum(v * (i % 8 + 2) for i, v in enumerate(reversed(cnpj)))
        digit = 11 - value % 11
        cnpj.append(digit if digit < 10 else 0)
    return "".join(str(x) for x in cnpj)

if __name__ == "__main__":
    print('Começando em: '+str(datetime.now().time().strftime('%H:%M:%S')))
    with open('cnpjs.csv','w') as f:
        f.write('cnpj_basico,cnpj_ordem,cnpj_dv,cnpj\n')
        for i in range(RANGE):
            cnpj =completa_cnpj(str(INITIAL_CNPJ))
            cnpj_dv = cnpj[12:14]
            f.write(str(INITIAL_CNPJ)+ COMA_SEPARATOR +'0001' +COMA_SEPARATOR+cnpj_dv+COMA_SEPARATOR+cnpj+'\n')
            INITIAL_CNPJ +=1

    print('Terminando em: '+str(datetime.now().time().strftime('%H:%M:%S')))

