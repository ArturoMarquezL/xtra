var token = sessionStorage.getItem("Usuario");
var form = document.querySelector("form");
form.onsubmit = e => {
    var id = document.querySelector("[id=id_cliente]").value;
    var nombre = document.querySelector("[id=nombre]").value;
    var email = document.querySelector("[id=correo]").value;
    e.preventDefault();
    var request = new XMLHttpRequest();
    request.open("PUT","https://8000-arturomarquezl-xtra-wldn92tjpqe.ws-us62.gitpod.io/actulizar/"+id+"/"+nombre+"/"+email);
    request.setRequestHeader("Authorization", "Bearer " + token);
    request.setRequestHeader("Accept","application/json");
    request.setRequestHeader("Content-Type","application/x-www-form-urlencoded");

    request.onload = function() {
        const data = JSON.parse(request.response);
        console.log(data);
    };
    request.send();
}