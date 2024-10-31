function suma() {
    let num1 = 5;
    let num2 = 7;
    let resultado = num1 + num2;
    console.log("El resultado de la suma es " + resultado)

}

function resta() {
    let num1 = prompt("Ingrese un número entero: ");
    let num2 = prompt("Ingrese otro número entero: ");
    let resultado = num1 - num2;
    console.log("El resultado de la resta es " + resultado)

}

function multiplicacion() {
    let num1 = prompt("Ingrese un número entero: ");
    let num2 = prompt("Ingrese otro número entero: ");
    let resultado = num1 * num2;
    console.log("El resultado del producto es " + resultado)

}

function division() {
    let num1 = prompt("Ingrese un número entero: ");
    let num2 = prompt("Ingrese otro número entero: ");
    let resultado = num1 / num2;
    console.log("El resultado de la división es " + resultado)

}
function modulo() {
    let num1 = prompt("Ingrese un número entero: ");
    let num2 = prompt("Ingrese otro número entero: ");
    let resultado = num1 % num2;
    console.log("El resultado del módulo/residuo es " + resultado)

}

function mayorQue() {
    let num1 = prompt("Ingrese un número entero: ");
    let num2 = prompt("Ingrese otro número entero: ");
    let resultado = num1 > num2;
    console.log(num1 + " mayor que " + num2 + " = " + resultado)

}

function menorQue() {
    let num1 = prompt("Ingrese un número entero: ");
    let num2 = prompt("Ingrese otro número entero: ");
    let resultado = num1 < num2;
    console.log(num1 + " menor que " + num2 + " = " + resultado)

}

function menorIgualQue() {
    let num1 = prompt("Ingrese un número entero: ");
    let num2 = prompt("Ingrese otro número entero: ");
    let resultado = num1 <= num2;
    console.log(num1 + " mayor o igual que " + num2 + " = " + resultado)

}

function mayorIgualQue() {
    let num1 = prompt("Ingrese un número entero: ");
    let num2 = prompt("Ingrese otro número entero: ");
    let resultado = num1 >= num2;
    console.log(num1 + " mayor o igual que " + num2 + " = " + resultado)

}

function igualQueNoEstricto() {
    let num1 = prompt("Ingrese un número entero: ");
    let num2 = prompt("Ingrese otro número entero: ");
    let resultado = num1 == num2;
    console.log(num1 + " mayor o igual que " + num2 + " = " + resultado)
}

function convertirAMayusculas(){
    let texto = prompt("Ingrese el texto")
    console.log(texto.toUpperCase)
}

function validadNaNAndNull() {
    console.log(null === undefined)
}

function operadorNot() {
    let var1 = true
    let var2 = false

    console.log(!var1)
    console.log(!var2)
}

function operadorY() {
    let num1 = Number(prompt("Ingrese un número entero: "));
    let num2 = Number(prompt("Ingrese otro número entero: "));
    let num3 = Number(prompt("Ingrese un número entero: "));
    let num4 = Number(prompt("Ingrese otro número entero: "));

    let comparacion = num1 > num2 && num3 < num4
    console.log(comparacion)
}

function operadorO() {
    let num1 = Number(prompt("Ingrese un número entero: "));
    let num2 = Number(prompt("Ingrese otro número entero: "));
    let num3 = Number(prompt("Ingrese un número entero: "));
    let num4 = Number(prompt("Ingrese otro número entero: "));

    let comparacion = num1 > num2 || num3 < num4
    console.log(comparacion)
}

function operadorO2() {
    let var1 = true;
    let var2 = false;
    let var3 = false;

    let comparacion = var1 || var2 || var3
    console.log(comparacion)
}

function operadorNot() {
    let var1 = true
    let var2 = false

    console.log(!var1)
    console.log(!var2)
}
