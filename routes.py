from flask import Flask, request
from planilha import Planilha
import json


app = Flask(__name__)
base_teste = Planilha('base_teste.xlsx')


@app.route("/busca-atualizacoes/all/<id>/", methods=["GET"])
def buscaTodasAtualizacoesGET(id):
    
    #if("id" not in body):
        #return json.dumps(geraResponse(400, "O parametro id e obrigatorio"))
    linhas = base_teste.buscaTodas(id)
    return json.dumps(geraResponse(200, "Sucesso!!!", "linhas", linhas))

        
@app.route("/busca-atualizacoes/all", methods=["POST"])
def buscaTodasAtualizacoesPOST():

    body = request.get_json()
    if("id" not in body):
        return json.dumps(geraResponse(400, "O parametro id e obrigatorio"))

    linhas = base_teste.buscaTodas(body["id"])
    return json.dumps(geraResponse(200, "Sucesso!!!", "linhas", linhas))


@app.route("/busca-atualizacoes/last/<id>/", methods=["GET"])
def buscaUltimaAtualizacaoGET(id):
    #if("id" not in body):
        #return json.dumps(geraResponse(400, "O parametro id e obrigatorio"))

    linha = base_teste.buscaUltima(id)
    return json.dumps(geraResponse(200, "Sucesso!!!", "linha", linha))

@app.route("/busca-atualizacoes/last", methods=["POST"])
def buscaUltimaAtualizacaoPOST():
    body = request.get_json()
    
    if("id" not in body):
        return json.dumps(geraResponse(400, "O parametro id e obrigatorio"))

    linha = base_teste.buscaUltima(body["id"])

    return json.dumps(geraResponse(200, "Sucesso!!!", "linha", linha))

def geraResponse(status, mensagem, nome_do_conteudo=False, conteudo=False):
    response = {}
    response["status"] = status
    response["mensagem"] = mensagem

    if(nome_do_conteudo and conteudo):
        response[nome_do_conteudo] = conteudo
    
    return response

if __name__ == "__main__":
    app.run(debug=True)

