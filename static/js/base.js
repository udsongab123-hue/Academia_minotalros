const botao = document.querySelector(".botao");
const lateral = document.querySelector(".lateral1");

botao.addEventListener("click", function() {
    lateral.classList.toggle("aberta");
    botao.classList.toggle("aberto");
});

function abrirPerfil() {
    const menu = document.getElementById("menuPerfil");

    if (menu.style.display === "block") {
        menu.style.display = "none";
    } else {
        menu.style.display = "block";
    }
}

/*-------------------*/

const btnContatos = document.getElementById("btnContatos");
const cartaoContatos = document.getElementById("cartaoContatos");

btnContatos.addEventListener("click", function () {

    if (cartaoContatos.style.display === "block") {
        cartaoContatos.style.display = "none";
    } else {
        cartaoContatos.style.display = "block";
    }

});