<p align="center">
  <h1 align="center">:zap: Gerador de CNPJs</h2>
  <p align="center">Projeto gerador CNPJs válidos com Python, gerados em um CSV</p>
</p>

<sub>Onde você me encontra também<br> 
    [<img src = "https://img.shields.io/badge/github-black.svg?&style=for-the-badge&logo=github&logoColor=white">](https://github.com/daniloaluiz)
    [<img src="https://img.shields.io/badge/linkedin-%230077B5.svg?&style=for-the-badge&logo=linkedin&logoColor=white" />](https://www.linkedin.com/in/daniloaluiz/) 
    [<img src = "https://img.shields.io/badge/instagram-%23E4405F.svg?&style=for-the-badge&logo=instagram&logoColor=white">](https://www.instagram.com/daniloaluiz/) 
</sub>
# gerador_cnpj
Projeto gerador CNPJs válidos com Python, gerados em um CSV

No começo do arquivo serão encontradas as seguintes constantes:

LENGTH_CNPJ = 14  
### tamanho padrão do CNPJ, não mexer

INITIAL_CNPJ = 46208711
### 8 primeiros dígitos do CNPJ, esse é o valor que será incrementado, caso precise fazer outra sequência basta trocar esse valor

RANGE =1000
## Aqui você pode escolher quantos novos CNPJs serão gerados no arquivo CSV
COMA_SEPARATOR = ','
## Separador do CSV, que pode ser substituído por ; ou | ....

# Como gerar novo arquivo
Basta entrar na pasta do projeto e rodar o comando {python3 gerador.py} no terminal

