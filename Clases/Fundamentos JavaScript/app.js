function saludar() {
    alert("Te estoy saludando")
}

function tiposDeDatos() {
    // Este es un comentario de una linea
    /*
        Esto es un comentario en bloque
    */
   console.log("Esto es un texto...")
   console.log('Esto también es un texto')
   console.log(20) //Esto es un number (Entero o int)
   console.log(1.2) //Esto es otro number (double o decimal)
   console.log(true); // boolean
   console.log(false); // boolean   
}

function variables() {

        var nombre = "Cristian"; // Alcance global
        let apellido = "Castro"; // Alcance de scope
        const edad = 25; // Alcance de scope y es inmutable

        console.log(nombre)
        console.log(apellido)
        console.log(edad)

}

function capturarDatos() {
    let nombre = prompt("Ingrese su nombre: ");
    let apellido = prompt("ingrese su apellido: ");
    let edad = prompt("Ingrese su edad: ");
    const edadPension = 65;

    console.log("Hola, tu nombre es " + nombre + " y tu apellido es " + apellido + " y tu edad es " + edad + ".")

    console.log(typeof nombre);
    console.log(typeof apellido);
    console.log(typeof edad);
    console.log(typeof edadPension);
}

function parsear() {
    let edadComoTexto = '23';
    let edadComoNumero = parseInt(edadComoTexto);
    console.log("Edad como texto " + edadComoTexto);
    console.log("Edad como numero" + edadComoNumero);
    console.log(typeof edadComoTexto);
    console.log(typeof edadComoNumero);
    console.log(edadComoTexto);
    console.log(edadComoNumero);
}

function parsearDecimales() {
    let edadComoTexto = '23.78976123456789';
    let edadComoNumero = parseFloat(edadComoTexto)
    console.log("Edad como texto " + edadComoTexto)
    console.log("Edad como número " + edadComoNumero)
    console.log(typeof edadComoTexto);
    console.log(typeof edadComoNumero)
    console.log(edadComoTexto)
    console.log(edadComoNumero)
    edadComoTexto = 'lara';
    console.log(edadComoNumero)
}


