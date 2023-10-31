// Tipos de datos en JavaScript
/*
LA SINTAXIS EN LOS COMENTARIOS ES
MUY SIMILAR A LA DE JAVA
REALMENTE DIRIAMOS QUE ES IDENTICA
*/

var nombre = 'German'; //Tipo str
console.log(nombre);
console.log(typeof nombre);
var numero = 3000; //Tipo numerico
console.log(numero);
nombre = 7;
console.log(typeof nombre);
nombre = 12.3;
console.log(typeof nombre);
console.log(nombre)
var objeto= {
    nombre : "German",
    apellido : "Castillo",
    telefono : "2604530553"
}


console.log(typeof objeto);

//Tipo de datos boolean
var bandera = true;
console.log(bandera);

//Tipo de datos funcion
function miFuncion(){

}
console.log(typeof miFuncion);

//Tipo de dato symbol
var symbol = symbol("Mi Simbolo");
console.log(typeof symbol);

//Tipo de datos clase
class Persona{
    constructor(nombre,apellido){
        this.nombre = nombre;
        this.apellido = apellido;
    }
}

console.log(typeof Persona);

//Tipo de dato undefined
var x;
console.log(typeof x)

//null: significa ausencia de valor
var y = null; //null no es un tipo de dato, pero su origen es Object
console.log(typeof y)

//Tipo de dato array y Empty String
var autos = ['Audi','Chevrolet','Bmw','Ford'];
console.log(autos)
console.log(typeof autos)//Pregutnamos tipo de dato

var z = '';
console.log(z)//esto hace referencia a una cadena vacia
console.log(typeof z)










