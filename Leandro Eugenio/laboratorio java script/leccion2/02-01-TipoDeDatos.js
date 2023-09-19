// Tipos de datos en JavaScript
/*
LA SINTAXIS EN LOS COMENTARIOS ES
MUY SIMILAR A LA DE JAVA
REALMENTE DIRIAMOS QUE ES IDENTICA
*/

var nombre = 'Leandro'; //Tipo str
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
    nombre : "Leandro",
    apellido : "Eugenio",
    telefono : "2625500165"
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
var symbol = symbol("mi simbolo");
console.log(typeof symbol);

//Tipo de datos clase
class Persona{
    constructor(nombre,apellido){
        this.nombre = nombre;
        this.apellido = apellido;
    }
}

console.log(typeof Persona);




