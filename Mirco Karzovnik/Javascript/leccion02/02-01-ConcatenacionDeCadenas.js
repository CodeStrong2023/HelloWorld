var nombre = "Tonez";
var apellido = "Lopez";
var NombreCompleto = nombre+" "+apellido;
console.log(NombreCompleto);
var  nombreCompleto2  = "Mirco"+" "+"Karzovnik";
console.log(nombreCompleto2);

var juntos = nombre + 219; //Lee de izq a der siguiendo la cadena lee el numero string
console.log(juntos);
juntos = nombre + (78 + 17);  // se puede diferenciar a traves de parentesis
console.log(juntos);
juntos = 78 + 17 + nombre;
console.log(juntos);

nombre += apellido;
console.log(nombre);

// No se va a usar var , se utiliza let y const POR HOY
let nombre2 = "Pedro";
console.log(nombre2);

const apellido2 = "Awe"
//apellido2 = "Peres"; una constante no puede ser modificada
console.log(apellido2)

let x, y; // Se pueden crear varias variables dentro de una misma linea
x = 17,  y = 21; //Se puede hacer asignacion de variables dentro de una misma linea
let z = x + y; //Se asigna el valor de la operacion
console.log(z)

let _1num = 31; //No utilizar numero para iniciar el nombre de una variable
let rompiendo = "rompe"; //No utilizar palabras reservadas para variables

console.log(_1num)
console.log(rompiendo)
