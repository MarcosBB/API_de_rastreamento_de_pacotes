from flask import Flask, request
from flask_restful import Resource, Api
from planilha import Planilha

app = Flask(__name__)
api = Api(app)

base_teste = Planilha('base_teste.xlsx')

class BuscaTodasAtualizacoesGET(Resource):
    def get(self, id):
        linhas = base_teste.buscaTodas(id)

        if linhas == []:
            return geraResponse("Busca mal sucedida", "Nenhum resultado encontrado para essa pesquisa")
        
        return geraResponse("Busca bem sucedida", "Resultado encontrado", "Resultado", linhas)

class BuscaUltimaAtualizacaoGET(Resource):
    def get(self, id):
        linha = base_teste.buscaUltima(id)

        if(linha == []):
            return geraResponse("Busca mal sucedida", "Nenhum resultado encontrado para essa pesquisa")

        return geraResponse("Busca bem sucedida", "Resultado encontrado", "Resultado", linha)

class buscaTodasAtualizacoesPOST(Resource):
    def post(self):
        body = request.get_json()
        

        if  "id" not in body:
            return geraResponse("Busca mal sucedida", "Deve conter o ID.")
        else:
            linhas = base_teste.buscaTodas(body["id"])
        
            if linhas == []:
                return geraResponse("Busca mal sucedida", "Nenhum resultado encontrado para essa pesquisa")
            
            return geraResponse("Busca bem sucedida", "Resultado encontrado", "Resultado", linhas)

class buscaUltimaAtualizacaoPOST(Resource):
    def post(self):
        body = request.get_json()

        if  "id" not in body:
            return geraResponse("Busca mal sucedida", "Deve conter o ID.")
        else:
            linha = base_teste.buscaUltima(body["id"])
            
            if linha == []:
                return geraResponse("Busca mal sucedida", "Nenhum resultado encontrado para essa pesquisa")

            return geraResponse("Busca bem sucedida", "Resultado encontrado", "Resultado", linha)


def geraResponse(status, mensagem, nome_do_conteudo=False, conteudo=False):
    response = {}
    response["status"] = status
    response["mensagem"] = mensagem

    if(nome_do_conteudo and conteudo):
        response[nome_do_conteudo] = conteudo
    
    response = app.make_response(response)
    response.headers['Access-Control-Allow-Origin'] = '*'
    response.headers['Access-Control-Allow-Methods'] = 'POST, GET'
    response.headers['Access-Control-Allow-Headers'] = '*'
    
    return response


api.add_resource(BuscaTodasAtualizacoesGET, '/busca-atualizacoes/all/<id>/')
api.add_resource(BuscaUltimaAtualizacaoGET, '/busca-atualizacoes/last/<id>/')
api.add_resource(buscaTodasAtualizacoesPOST, '/busca-atualizacoes/all/')
api.add_resource(buscaUltimaAtualizacaoPOST, '/busca-atualizacoes/last/')


if __name__ == '__main__':
    app.run()