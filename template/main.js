function fazPost(url){
    let request = new XMLHttpRequest()
    request.open("POST", url, false)
    request.send()
    return request.responseText
}

function criaLinha(usuario){

}

function PegarUltimaAtualizacao(){
    payload = {
        "id": "776d69dd876bf6ef5c284ee7fc2a1cc2"
    }


    let data = fazPost("http://127.0.0.1:5000/busca_ultima_atualizacao")
    let linha = JSON.parse(data)
    console.log(linha)
}

PegarUltimaAtualizacao()