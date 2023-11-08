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

//Tipo de dato undefined
var x;
console.log(typeof x);

x = undefined
console.log(typeof x);

//null: Significa ausencia de valor

var y = null; //null no es un tipo de dato, pero su origen es objet
console.log(typeof y);

//Tipo de dato array u Empty String
var autos = ['Citroen', 'Audi', 'BMW', 'Ford']
console.log(autos);
console.log(typeof autos); //Preguntamos que tipo de dato es:

var z = ''; 
console.log(z); //Esto se refiere a que es una cadena vacia:
console.log(typeof z);