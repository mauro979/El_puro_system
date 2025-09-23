//seleccionando los datos del cliente
const clientName = document.getElementById("name-input");
const clientPassword = document.getElementById("password-input");
const companyName = document.getElementById("company-name");
const logoImage = document.getElementById("fileName");
const email = document.getElementById("email")
//seleccionando el boton y el archivo del logo
const confirmButton = document.getElementById("Create-account-button");

//añadiendo la funcion de enviar los datos al backend

let encriptLogo = null;

// axios.get("http://127.0.0.1:8000/cookies",{
//     withCredentials : true
// })

confirmButton.addEventListener("click",(e)=>{
    e.preventDefault()
    if (clientName.value.length >= 5 && 
        clientPassword.value.length >= 4 && 
        companyName.value.length >= 5 &&
        email.value.includes("@")){
            axios.post("http://127.0.0.1:8000/CreateAccountAdmin",
                {
                    "username": clientName.value,
                    "email" : email.value,
                    "admin" : true,
                    "password": clientPassword.value,
                    "company_name": companyName.value,
                    "logo": encriptLogo
                },
                { withCredentials: true }
            ).then(() => {
                console.log({"status":"ok"})
                location.reload();
            })
            .catch(()=>{
                alert("Por favor revice la informacion introducida")
            })
        }else{
            alert("verifica la informacion enviada")
            location.reload()
        }
});

document.getElementById('fileInput').addEventListener('change', function(event) {
    const file = event.target.files[0];
    if (!file) return;

    const reader = new FileReader();

    reader.onload = function(e) {
        const base64String = e.target.result.split(',')[1]; // Elimina el encabezado data:image/...

        encriptLogo = base64String
};

      reader.readAsDataURL(file); // Convierte a base64 automáticamente
    });