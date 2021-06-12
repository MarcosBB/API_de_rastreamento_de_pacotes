import requests



payload = {
    "id": "776d69dd876bf6ef5c284ee7fc2a1cc2"
}

t = requests.post("http://127.0.0.1:5000/busca_todas_atualizacoes", json=payload)
u = requests.post("http://127.0.0.1:5000/busca_ultima_atualizacao", json=payload)

print("-------------Todas as atualizações-------------")
print(t.text)

print("")
print("")

print("------------Ultima atualização---------")
print(u.text)
