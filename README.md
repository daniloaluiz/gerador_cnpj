<p align="center">
  <h1 align="center">:zap: Gerador de CNPJs</h2>
  <p align="center">Projeto gerador CNPJs válidos com Python, gerados em um CSV</p>
</p>

<sub>Onde você me encontra<br> 
    [<img src = "https://img.shields.io/badge/github-black.svg?&style=for-the-badge&logo=github&logoColor=white">](https://github.com/daniloaluiz)
    [<img src="https://img.shields.io/badge/linkedin-%230077B5.svg?&style=for-the-badge&logo=linkedin&logoColor=white" />](https://www.linkedin.com/in/daniloaluiz/) 
    [<img src = "https://img.shields.io/badge/instagram-%23E4405F.svg?&style=for-the-badge&logo=instagram&logoColor=white">](https://www.instagram.com/daniloaluiz/) 
</sub>
## Como gerar um novo arquivo
No terminal, entre na pasta do projeto e execute o comando 
```bash
python3 gerador.py
```
## Parâmetros
No início do arquivo `gerador.py` serão encontradas os seguintes parâmetros:

- INITIAL_CNPJ: 8 primeiros dígitos do CNPJ a ser gerado, esse é o valor que será incrementado, caso precise fazer outra sequência basta trocar esse valor
- QUANTITY: quantidade de CNPJs a serem gerados
- DIR_OUTPUT: diretório onde será gerado o arquivo
- COMA_SEPARATOR: caractere de separação entre as colunas do .csv
## :pushpin: Licença
[MIT License](/LICENSE) <br>
