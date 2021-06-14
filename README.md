# API de rastreamento de pacotes
 
É uma `API` feita em `Python` e `Flask` que pesquisa informações de rastreamento de pacotes em uma tabela `.xlsx` e retorna o resultado.

## Como usar

Para usar a API basta usar a URL a seguir e adicionar as [rotas](https://github.com/MarcosBB/API-da-L-Auto/blob/main/README.md#rotas) no final dependendo do uso que queira na sua aplicação.

```
bla bla bla bla
```

Para rodar o servidor localmente você deve:
1. Instalar o Python;
2. Instalar as bibliotecas Flask, Flask-restful e Pandas ou somente rode o seguinte comando no cmd `pip install -r requirements.txt`;
3. Rodar o programa `rastreamento_API.py`. (`python rastreamento_API.py`);
4. Usar as [rotas](https://github.com/MarcosBB/API-da-L-Auto/blob/main/README.md#rotas) na sua aplicação.

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

* `/busca-atualizacoes/all` Busca todas as atualizações de rastreamento do pacote.
* `/busca-atualizacoes/last` Busca a ultima atualização de restreamento do pacote.

### Exemplos de retorno da API 
Usei o programa Insomnia para isso.

![image](https://user-images.githubusercontent.com/50207805/121764127-64bd2f00-cb0f-11eb-92f2-2d3a7b5df40b.png)
![image](https://user-images.githubusercontent.com/50207805/121764120-5bcc5d80-cb0f-11eb-822f-3215b9da6752.png)
![image](https://user-images.githubusercontent.com/50207805/121764099-3c353500-cb0f-11eb-8783-25b995a6c2ec.png)
![image](https://user-images.githubusercontent.com/50207805/121764106-4c4d1480-cb0f-11eb-8865-656b801e4226.png)
