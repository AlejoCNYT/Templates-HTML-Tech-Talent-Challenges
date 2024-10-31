function contar() {
    let contador = Number(prompt("Ingrese el número a contar"))
    let numero = 0

    while(numero <= contador) {
        console.log(numero)
        numero = numero + 1; // numero++
    }

}
function validarPassword() {
    let password = prompt("Introduce la contraseña: ")
    while(password != "secreto"){
        password = prompt("Contraseña incorrecta. Introduce la contraseña.")        
    }
    console.log("Usuario autenticado")
}

function obtenerFrutas() {
    let frutas = ["manzana", "pera", "banano", "naranja", "uvas"]
    console.log(frutas[0])
    console.log(frutas[1])
    console.log(frutas[2])
    console.log(frutas[3])
    console.log(frutas[4])
    console.log(frutas)
    frutas.push("melocoton")
    console.log(frutas)
    frutas.pop()
    console.log(frutas)
}

function obtenerFrutasConFor() {
    let frutas = ["manzana", "pera", "banano", "naranja", "uvas"]
    for (let i = 0; i < frutas.length; i++) {
        if (frutas[i] == "uvas" ){
            console.log(i)
        } else {
            console.log("La fruta no es una uva")
        }
    }

    for (let fruta of frutas){
        console.log(fruta)
    }
}
