# API de rastreamento de pacotes
 
É uma `API` feita em `Python` e `Flask` que pesquisa informações de rastreamento de pacotes em uma tabela `.xlsx` e retorna o resultado.

## Sumário

- [Como usar](#como-usar)
	- [Rotas](#rotas)
		- [Com método GET](#com-método-get)
		- [Com método POST](#com-método-post)
	- [Insomnia](#insomnia)
	- [Exemplos de retorno da API](#exemplos-de-retorno-da-api)



## Como usar

Para usar a API basta usar a URL a seguir e adicionar as [rotas](#rotas) no final dependendo do uso que queira na sua aplicação.

```
https://rastreamento-api.herokuapp.com
```

Exemplo:

```
https://rastreamento-api.herokuapp.com/busca-atualizacoes/all/e8f37e1f683e6c472721010956ea5798/
```

Para rodar o servidor localmente você deve:
1. Instalar o Python;
2. Instalar as bibliotecas Flask, Flask-restful e Pandas ou somente rode o seguinte comando no cmd `pip install -r requirements.txt`;
3. Rodar o programa `rastreamento_API.py`. (`python rastreamento_API.py`);
4. Usar as [rotas](#rotas) na sua aplicação.

### Rotas
#### Com método GET
Coloque o id que pretende pesquisar no lugar de `<id>` na url.
Exemplo:
```
http://127.0.0.1:5000/busca-atualizacoes/last/5513bfab82f7a76f4b6127dc9d46c134
```

* `/busca-atualizacoes/all/<id>/` Busca todas as atualizações de rastreamento do pacote.
* `/busca-atualizacoes/last/<id>/` Busca a ultima atualização de restreamento do pacote.

#### Com método POST
Coloque o id que pretende pesquisar no formato `JSON` no payload da requisição na sua aplição.
Exemplo:
```
{
	"id": "5513bfab82f7a76f4b6127dc9d46c134"
}
```

* `/busca-atualizacoes/all/` Busca todas as atualizações de rastreamento do pacote.
* `/busca-atualizacoes/last/` Busca a ultima atualização de restreamento do pacote.

### Insomnia
Se quiser testar a API você mesmo usando o Insomnia clicke no botão abaixo:

[![Run in Insomnia}](https://insomnia.rest/images/run.svg)](https://insomnia.rest/run/?label=Rastreamento_API&uri=https%3A%2F%2Fraw.githubusercontent.com%2FMarcosBB%2FAPI_de_rastreamento_de_pacotes%2Fmain%2Finsomnia%2FInsomnia_2021-06-15.json)


### Exemplos de retorno da API 
Usei o programa Insomnia para isso.

![image](https://user-images.githubusercontent.com/50207805/121764127-64bd2f00-cb0f-11eb-92f2-2d3a7b5df40b.png)
![image](https://user-images.githubusercontent.com/50207805/121764120-5bcc5d80-cb0f-11eb-822f-3215b9da6752.png)
![image](https://user-images.githubusercontent.com/50207805/121764099-3c353500-cb0f-11eb-8783-25b995a6c2ec.png)
![image](https://user-images.githubusercontent.com/50207805/121764106-4c4d1480-cb0f-11eb-8865-656b801e4226.png)
