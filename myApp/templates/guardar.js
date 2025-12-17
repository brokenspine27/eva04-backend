
const formPersona = document.querySelector('#personaPOST')
const urlPersona = "http://localhost:8000/api/guardar_persona/" // Endpoint para guardar a las personas


/**
 * Guarda el JSON de la persona y lo envía a el backend para ser guardado en la BD
 * @param {string} token 
 * @param {JSON} persona
 */
async function GuardarPersona(token,persona){
    try{
        const response = await fetch(urlPersona, {
            method : 'POST',
            headers :{
                'Content-Type':'application/json',
                'Authorization': `Bearer ${token}`
            },
            body:JSON.stringify(persona)
        })
        return response

    }catch(error){
        console.log(error)
    }
}






formPersona.addEventListener('submit', async function(event) {
    event.preventDefault()
    const nombre = document.querySelector('#nombre').value
    const apellido = document.querySelector('#apellido').value

    try{
        const token = localStorage.getItem('jwtToken')
        if (token == null){
            window.alert("Tiene que tener un token primero")
            return
        }
        const persona = {
            "nombre":nombre,
            "apellido":apellido
        }
        const enviarPost = await GuardarPersona(token,persona)
        if (enviarPost.status == 401){
            window.alert("Tienes que tener un token primero!")
        }else if (enviarPost.status == 200){
            window.alert("Persona guardada en la BD")
            const area = document.querySelector("#respuesta")
            area.textContent = ""        
            area.textContent = JSON.stringify(persona,null,2)
        }

    }catch(error){
        console.log(error)
    }
})