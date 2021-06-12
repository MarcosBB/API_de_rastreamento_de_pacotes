from flask import Flask, request
from planilha import Planilha
import json


app = Flask(__name__)
base_teste = Planilha('base_teste.xlsx')


@app.route("/busca-atualizacoes/all/<id>/", methods=["GET"])
def buscaTodasAtualizacoesGET(id):
    linhas = base_teste.buscaTodas(id)

    if(linhas == []):
        return json.dumps(geraResponse("Busca mal sucedida", "Nenhum resultado encontrado para essa pesquisa"))
    
    return json.dumps(geraResponse("Busca bem sucedida", "Resultado encontrado", "linhas", linhas))

        
@app.route("/busca-atualizacoes/all", methods=["POST"])
def buscaTodasAtualizacoesPOST():
    body = request.get_json()
    linhas = base_teste.buscaTodas(body["id"])

    if(linhas == [] or "id" not in body):
        return json.dumps(geraResponse("Busca mal sucedida", "Nenhum resultado encontrado para essa pesquisa"))
    
    return json.dumps(geraResponse("Busca bem sucedida", "Resultado encontrado", "linhas", linhas))


@app.route("/busca-atualizacoes/last/<id>/", methods=["GET"])
def buscaUltimaAtualizacaoGET(id):
    linha = base_teste.buscaUltima(id)

    if(linha == []):
        return json.dumps(geraResponse("Busca mal sucedida", "Nenhum resultado encontrado para essa pesquisa"))

    return json.dumps(geraResponse("Busca bem sucedida", "Resultado encontrado", "linha", linha))

@app.route("/busca-atualizacoes/last", methods=["POST"])
def buscaUltimaAtualizacaoPOST():
    body = request.get_json()
    linha = base_teste.buscaUltima(body["id"])

    if(linha == [] or "id" not in body):
        return json.dumps(geraResponse("Busca mal sucedida", "Nenhum resultado encontrado para essa pesquisa"))

    return json.dumps(geraResponse("Busca bem sucedida", "Resultado encontrado", "linha", linha))

def geraResponse(status, mensagem, nome_do_conteudo=False, conteudo=False):
    response = {}
    response["status"] = status
    response["mensagem"] = mensagem

    if(nome_do_conteudo and conteudo):
        response[nome_do_conteudo] = conteudo
    
    return response

if __name__ == "__main__":
    app.run(debug=True)

