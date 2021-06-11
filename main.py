import pandas as pd

def buscaTodas(id):
    planilha = pd.read_excel (r'base_teste.xlsx')
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


print(buscaUltima("776d69dd876bf6ef5c284ee7fc2a1cc2"))