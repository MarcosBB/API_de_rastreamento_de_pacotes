# API da L'Auto
 
É uma API feita em Python e Flask que pesquisa informações em uma tabela `.xlsx` e retorna o resultado da pesquisa.

## Como usar

Para usar você deve:
1. Instalar a biblioteca Flask. (pip install Flask)
2. Rodar o programa `routes.py`. (python routes.py)
3. Usar as rotas na sua aplicação ou, se quiser, pode testar rodando o arquivo `teste.py` em outro cmd

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

