//seleccionando los datos del cliente
const clientName = document.getElementById("name-input");
const clientPassword = document.getElementById("password-input");
const companyName = document.getElementById("company-name");
const logoImage = document.getElementById("fileName");
//seleccionando el boton
const confirmButton = document.getElementById("Create-account-button");

//añadiendo la funcion de enviar los datos al backend

confirmButton.addEventListener("click",(e)=>{
    e.preventDefault()
    if (clientName.value.length >= 5 && 
        clientPassword.value.length >= 4 && 
        companyName.value.length >= 5 && 
        logoImage.value.length >= 1){
            axios.post("http://127.0.0.1:8000/autentication",
                {
                    "username": clientName.value,
                    "company_name": companyName.value,
                    "logo": logoImage.value,
                    "password": clientPassword.value
                }   
            )
        }
})