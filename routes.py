from flask import Flask, request
from main import buscaTodas, buscaUltima
import pandas as pd
import json

app = Flask("Rastreamento")

@app.route("/busca_todas_atualizacoes", methods=["POST"])
def buscaTodasAtualizacoes():
    body = request.get_json()
    
    if("id" not in body):
        return geraResponse(400, "O parametro id e obrigatorio")

    linhas = buscaTodas(body["id"])

    return json.dumps(geraResponse(200, "Sucesso!!!", "linhas", linhas))
    #return geraResponse(200, "Sucesso!!!", "linhas", linhas)


@app.route("/busca_ultima_atualizacao", methods=["POST"])
def buscaUltimaAtualizacao():
    body = request.get_json()
    
    if("id" not in body):
        return geraResponse(400, "O parametro id e obrigatorio")

    linha = buscaUltima(body["id"])

    return json.dumps(geraResponse(200, "Sucesso!!!", "linha", linha))
    #return geraResponse(200, "Sucesso!!!", "linha", linha)

def geraResponse(status, mensagem, nome_do_conteudo=False, conteudo=False):
    response = {}
    response["status"] = status
    response["mensagem"] = mensagem

    if(nome_do_conteudo and conteudo):
        response[nome_do_conteudo] = conteudo
    
    return response

app.run()
