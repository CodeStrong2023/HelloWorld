// Tipos de Datos en JavaScript
/*
La sintesis en lo que es comentarios
es muy similar a la de Java
realmente diríamos que es idéntica
*/
var nombre = "Flor"; //Tipo Str
console.log(nombre);
nombre = 7;
console.log(nombre);
nombre = 12.3;
console.log(nombre);

var numero = 7467; //Tipo numérico
console.log(numero);

var objeto = {
    nombre : "Flor",
    apellido : "Carballo",
    teléfono: "2604048615"

}
console.log(objeto);

//Tipos de dato boolean
var bandera = true;
console.log(typeof bandera);

//Tipo de dato funcion
function miFuncion(){}
console.log(typeof miFuncion);

//Tipo de dato symbol
var simbolo = Symbol("Mi simbolo");
console.log(typeof simbolo);

//Tipo de dato clase
class Persona{
	constructor(nombre, apellido){
		this.nombre = nombre;
		this.apellido = apellido;
	}
}
console.log(typeof Persona);

//Tipo de dato undefined
var x;
console.log(typeof x);

x = undefined;
console.log(typeof x);

//null: significa ausencia de valor
var y = null; //null no es un tipo de dato, pero su origen es object
console.log(typeof y);

//Tipo de dato array  y Empy String
var autos = ["Citroen", "Audi", "BMW", "Ford"];
console.log(autos);
console.log(typeof autos);

var z = "";
console.log(z); //Cadena vacia
console.log(typeof z);

