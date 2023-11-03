// Tipos de datos en JavaScript
/*
La sintaxis en lo que es comentarios
es muy siomilar a la de java
realmente diriamos que es identica
*/
var nombre = "Mirco"; //Tipo String
console.log(typeof nombre);
nombre = 21.3;
console.log(typeof  nombre);
nombre = 4;
console.log(typeof nombre);

var numero = 300; //Tipo numerico
console.log(numero);

var objeto = {
    nombre : "Mirco",
    apellido : "Karzovnik", 
    telefono : "2604864864"
}

console.log(objeto);

//Tipo de dato Boolean
var bandera = true;
console.log(bandera);

//Tipo de dato funcion
function miFuncion(){}
console.log(miFuncion);

//Tipo de dato symbol
var simbolo = Symbol("Mi simbolo");
console.log(simbolo);

//Tipo de dato array y Empty String
var autos = ["Citroene", "Audi","Ford"];
console.log(autos);
console.log(typeof autos); //Preguntamos que tipo de dato es

//Hago una cadena vacia
var z = "";
console.log(z); //Esto se refiere a una cadena vacia:
console.log(typeof z);