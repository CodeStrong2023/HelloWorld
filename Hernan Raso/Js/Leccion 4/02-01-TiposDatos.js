// Tipos de datos en JavaScript
/*
La sinstaxis en lo que es comentarios es muy similar a la de java realmente diriamos que es identica
*/

// Tipo Strin
var nombre = "Hernan"; //Tipo str
console.log(typeof nombre);

//Tipo Numerico
var numero = 3000; //tipo numerico
console.log(numero);
nombre = 7;
console.log(nombre);
nombre = 12.3;
console.log(typeof nombre);

//Tipo Object
var objeto = {
    nombre : "Hernan",
    apellido: "Raso",
    telefono: "2343554234"

}

console.log(objeto);

//Tipo de dato booleano
var bandera = true;
console.log(bandera);

//Tipo de dato funcion
function miFuncion(){}
console.log(typeof miFuncion);

//Tipo de dato symbol
var simbolo = Symbol("Mi simbolo");
console.log(typeof simbolo);

//Tipo de dato clase
class Persona{
    constructor(nombre,apellido){
        this.nombre = nombre;
        this.apellido = apellido;
    }
}

console.log(typeof Persona);