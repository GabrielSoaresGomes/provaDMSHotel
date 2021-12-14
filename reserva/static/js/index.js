function reservarHospedagem(idHospedagem) {
    disponibilidade = document.getElementById("disponibilidade"+idHospedagem).innerHTML
    if (disponibilidade == "Sim") {
        console.log("entrou");
        window.location.href= `reservar/${idHospedagem}`
    }
    else {
        document.querySelector("#naoDisponivel"+idHospedagem).style.display = "initial"
    }
}