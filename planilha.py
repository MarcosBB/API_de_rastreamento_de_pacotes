import pandas as pd

class Planilha:
    def __init__(self, arquivo):
        self.arquivo = arquivo
        self.data =  pd.read_excel (rf'{self.arquivo}')

    def buscaTodas(self, id):
        self.linhas = self.data.query("id==@id")
        self.linhas = self.linhas.drop('Unnamed: 0',axis=1)
        self.linhas.reset_index()

        retorno = []
        for coluna, linha in self.linhas.iterrows():
            retorno.append(linha.to_dict())

        return retorno

    def buscaUltima(self, id):
        ultimaAtualizacao = self.buscaTodas(id)
        if ultimaAtualizacao != []:
            ultimaAtualizacao = ultimaAtualizacao[len(ultimaAtualizacao)-1]

        return ultimaAtualizacao

    def atualizar(self):
        atualizacao = pd.read_excel (rf'{self.arquivo}')
        if atualizacao.shape != self.data.shape:
            self.data = atualizacao
            print("Update de " +  self.arquivo + " concluido com sucesso!!!")
        else:
            print("Não há atualizações pendentes")
