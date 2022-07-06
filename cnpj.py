from logging import raiseExceptions

class Cnpj:

    def __valid_cnpj_length__(self, cnpj):
        '''
        Rotina que valida o tamanho do CNPJ básico.
        Se igual a 8 retorna True, senão False

        Retorno: boolean
        '''
        try:
            if len(str(cnpj)) == 8:
                return True
        except:
            pass

        return False

    def __gera_dv__(self, cnpj):
        '''
        Rotina que calcula o dígito verificador baseado num número de CNPJ básico

        Retorno: string
        '''
        cnpj = list(map(int,cnpj)) + [0, 0, 0, 1]
        for _ in range(2):
            value = sum(v * (i % 8 + 2) for i, v in enumerate(reversed(cnpj)))
            digit = 11 - value % 11
            cnpj.append(digit if digit < 10 else 0)
        return "".join(str(x) for x in cnpj[12:14])

    def __cnpj_formatado__(self):
        '''
        Rotina que formata o número CNPJ para o modelo padrão

        Retorno: string
        '''
        cnpj = str(self.cnpj_basico)
        return cnpj[:2] +"."+ cnpj[2:5] +"."+ cnpj[5:] +'/'+ self.ordem +'-'+ str(self.dv)

    def __init__(self, cnpj):
        if self.__valid_cnpj_length__(cnpj):
            self.cnpj_basico = cnpj
            self.ordem = '0001'
            self.dv = self.__gera_dv__(str(cnpj))
            self.cnpj_formatado = self.__cnpj_formatado__() 
        else:
            raise Exception("O formato do CNPJ informado é inválido") 

    def __str__(self):
        return str(self.cnpj_basico) + self.ordem + str(self.dv)
    
    