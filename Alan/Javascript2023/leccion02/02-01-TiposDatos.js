// tipos de datos en javascript
/*
sintaxis similar a java
casi identica
*/
var nombre = "Ariel"; //tipo string
console.log(typeof nombre);
nombre = 7
console.log(typeof nombre);
nombre = 12.3;
console.log(typeof nombre);

var numero= 3000; //tipo int
console.log(numero);

var objeto = { //objeto
    nombre: "Ariel",
    apellido: "Betancud",
    telefono: 261654654
}
console.log(typeof objeto);

//tipo de dato booleano (true o false)
var bandera = true;
console.log(bandera);

//tipo de dato funcion (funcion: nos permite reutilizar lineas de codigo con solo llamarla)
function miFuncion(){}
console.log(typeof miFuncion);

//tipo de dato symbol
var simbolo = Symbol("Mi simbolo");
console.log(typeof simbolo);

//tipo de dato clase
class Persona{
    constructor(nombre, apellido){
        this.nombre = nombre;
        this.apellido = apellido;
    }
}
console.log(typeof Persona);

//tipo de dato undefined (indefinida)
var x;
console.log(typeof x);

x = undefined;
console.log(typeof x);

//null: significa ausencia de valor
var y = null; //null no es un tipo de dato, pero su origen es de tipo object
console.log(typeof y);

//tipo de dato array y empty string
var autos = ["citroen", "audi", "bmw", "ford"]; //puede contener cualquier tipo de dato
console.log(autos); 
console.log(typeof autos); //preguntamos el tipo de dato

var z = "";
console.log(z); //variable cadena vacia
console.log(typeof z);