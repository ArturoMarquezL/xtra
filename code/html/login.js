function inicio () {
    var email = document.querySelector("[id=correo]").value;
    var password = document.querySelector("[id=password]").value;

    var request = new XMLHttpRequest();
    request.open("GET","https://8000-arturomarquezl-xtra-wldn92tjpqe.ws-us62.gitpod.io/user/token_value/",true);
    request.setRequestHeader("Authorization", "Basic " +btoa(email + ":" + password));
    request.setRequestHeader("Content-Type", "application/json");
    request.setRequestHeader("Accept","application/json");

    request.onload = () => {
        const token_parse = request.responseText;
        const status = request.status;
        const final_token = JSON.parse(token_parse);

        if (status == 202) {
            sessionStorage.setItem("Usuario", final_token.token)
            window.location.replace("lista.html");
        }else{
            alert("Error");
            console.log("Error");
        }
    };
    request.send();
}