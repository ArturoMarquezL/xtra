function registro (){
    var email = document.querySelector("[id=correo]").value;
    var password = document.querySelector("[id=password]").value;

    var request = new XMLHttpRequest();
    request.open("POST","https://8000-arturomarquezl-xtra-wldn92tjpqe.ws-us62.gitpod.io/registro/"+email+"/"+password);
    request.setRequestHeader('Content-Type', 'application/');

    request.onload = function () {
        const data = JSON.parse(request.response);
        console.log(data);
    }
    request.send();
}