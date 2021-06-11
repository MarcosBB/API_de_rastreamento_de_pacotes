import pandas as pd

planilha = pd.read_excel (r'base_teste.xlsx')

def buscaTodas(id):
    
    linhas = planilha.query("id==@id")
    linhas = linhas.drop('Unnamed: 0',axis=1)

    linhas.reset_index()

    retorno = []
    for coluna, linha in linhas.iterrows():
        retorno.append(linha.to_dict())

    return retorno

def buscaUltima(id):
    ultimaAtualizacao = buscaTodas(id)
    ultimaAtualizacao = ultimaAtualizacao[len(ultimaAtualizacao)-1]

    return ultimaAtualizacao