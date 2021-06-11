from flask import Flask, request
from planilha import Planilha
import json
import subprocess

subprocess.run("python atualizaTabela.py ", shell=True)


app = Flask("Rastreamento")
base_teste = Planilha('base_teste.xlsx')

@app.route("/busca_todas_atualizacoes", methods=["POST"])
def buscaTodasAtualizacoes():
    body = request.get_json()
    
    if("id" not in body):
        return geraResponse(400, "O parametro id e obrigatorio")

    linhas = base_teste.buscaTodas(body["id"])

    return json.dumps(geraResponse(200, "Sucesso!!!", "linhas", linhas))


@app.route("/busca_ultima_atualizacao", methods=["POST"])
def buscaUltimaAtualizacao():
    body = request.get_json()
    
    if("id" not in body):
        return geraResponse(400, "O parametro id e obrigatorio")

    linha = base_teste.buscaUltima(body["id"])

    return json.dumps(geraResponse(200, "Sucesso!!!", "linha", linha))

def geraResponse(status, mensagem, nome_do_conteudo=False, conteudo=False):
    response = {}
    response["status"] = status
    response["mensagem"] = mensagem

    if(nome_do_conteudo and conteudo):
        response[nome_do_conteudo] = conteudo
    
    return response

app.run()
