function esMayorQue() {
    let num1 = Number(prompt("Ingrese un número"))
    let num2 = Number(prompt("Ingrese un número"))

    if(!(num1>num2)){
        console.log("El número 1 es mayor que el número 2")
    } else {
        console.log("El número 2 es mayor que el número 1")
    }
}

function juego(){
    let num1 = Number(prompt("Ingrese un número"))
    let num2 = Number(prompt("Ingrese un número"))    
    let num3 = Number(prompt("Ingrese un número"))

    if(num1 === 1) {
        console.log("Ganaste, el número es igual a 1")
    } else if(num2 === 2){
        console.log("Pediste, el número es igual a 2")
    } else {
        console.log("El número no es 1 ni 2")
    }
}

function pasasteLaMateria() {
    let nota = Number(prompt("Tu nota fue muy buena"))

    if (nota >= 4.5){
        console.log("Tu nota fue muy buena")
    } else if( nota >= 4.0 ) {
        console.log("Tu nota fue buena")
    } else if( nota >= 3.5 ) {
        console.log("pasaste y puedes mejorar")
    } else if (nota >= 3) {
        console.log("Paso raspando")
    } else {
        console.log("Te rajaste, ya valiste!")
    }
}

function mesesDelAnio(){
    let mes = prompt("Ingresa el número del mes del año")

    switch (mes) {
        case "1":
            console.log("Enero");
            break;

        case "2":
            console.log("Febrero");
            break;

        case "3":
            console.log("Marzo");
            break;
        default:
            console.log("El mes ingresado no es válido")

    }

}