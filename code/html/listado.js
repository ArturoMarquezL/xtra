const API_URL = "https://8000-arturomarquezl-xtra-wldn92tjpqe.ws-us62.gitpod.io/clientes";
const xhr = new XMLHttpRequest();
var token = sessionStorage.getItem("Usuario");
console.log(token);
function onRequestHandler() {
    if (xhr.readyState == 4 && xhr.status == 202) {
        console.log("*")

        const data = JSON.parse(this.response);
        console.log(data);
        const HttpResponse = document.querySelector("#clientes");

        const list = data.map((user) => `<tr><td>${user.id_cliente}</td><td>${user.nombre}</td><td>${user.email}</td></tr>`);
        HttpResponse.innerHTML = list;
    }
}
xhr.addEventListener('load', onRequestHandler);
xhr.open("GET", API_URL);
xhr.setRequestHeader("Authorization", "Bearer " + token);
xhr.setRequestHeader("Accept","application/json");
xhr.send();
