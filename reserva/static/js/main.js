
document.getElementById('id_valorFinal').style.display = "none"
document.getElementById('id_nomeHospedagemReservada').style.display = "none"
document.getElementById('errorPessoas').style.display = "none"
document.getElementById("id_dataEntrada").setAttribute("input")


function calcularHospedagem() {
    maximoPessoas = parseInt(document.getElementById("maximoPessoas").innerHTML)
    numeroPessoas = parseInt(document.getElementById("id_numeroPessoas").value)
    preco = parseInt(document.getElementById('preco').innerHTML)
    dataEntrada = document.getElementById('id_dataEntrada').value // 17/02/2021
    numeroDias = document.getElementById('id_numeroDias').value // 21/02/2021

    precoFinal = preco * numeroDias
    if ( numeroPessoas > maximoPessoas) {
        document.getElementById("errorPessoas").style.display = "initial"
    }
    if (precoFinal > 0 && numeroPessoas <= maximoPessoas) {
        document.getElementById("errorPessoas").style.display = "none"
        nomeHospedagem = document.getElementById('nomeEstabelecimento').innerHTML
        console.log(nomeHospedagem);
        document.getElementById("id_nomeHospedagemReservada").value = nomeHospedagem
        document.getElementById('valorFinal').innerHTML = precoFinal
        document.getElementById('btnCalcular').style.display = "none"
        document.getElementById('btnFinalizar').style.display = "initial"
        document.getElementById('id_valorFinal').value = precoFinal
        document.getElementById('form').setAttribute("method","POST")
    }
}