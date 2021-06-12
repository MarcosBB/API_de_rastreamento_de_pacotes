# API da L'Auto
 
É uma API feita em Python e Flask que pesquisa informações em uma tabela `.xlsx` e retorna o resultado da pesquisa.

## Como usar
Para usar você deve:
1. Instalar a biblioteca Flask. (pip install Flask)
2. Rodar o programa `routes.py`. (python routes.py)
3. Usar as rotas na sua aplicação ou, se quiser, pode testar rodando o arquivo `teste.py` em outro cmd

## Rotas

* `/busca_todas_atualizacoes` Busca todas as atualizações de rastreamento do pacote
* `/busca_ultima_atualizacao` Busca a ultima atualização de restreamento do pacote

### Exemplos de retorno da API 
Usei o programa Insomnia para isso.
![image](https://user-images.githubusercontent.com/50207805/121727242-a622ef80-cab9-11eb-9faa-86f10a8dba49.png)

![image](https://user-images.githubusercontent.com/50207805/121727357-cce12600-cab9-11eb-8d8e-20d8c0cf35bc.png)

