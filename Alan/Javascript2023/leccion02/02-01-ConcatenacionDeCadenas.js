var nombre = "Jose";
var apellido = "Montes";
var nombreCompleto = nombre + " " + apellido; //primera concatenacion
console.log(nombreCompleto);
var nombreCompleto2 = "Ariel" + " " + "Betancud"; //segunda concatenacion
console.log(nombreCompleto2);
var juntos = nombre + 219; //lee de izquierda a derecha siguiendo la cadena lee el numero como str
console.log(juntos);
juntos = nombre + (78 + 17); //aqui suma por los parentesis
console.log(juntos);
juntos = 78 + 17 + nombre; //primero sumo los numeros, despues sumo el nombre
console.log(juntos);

nombre += apellido; //tercera concatenacion usando el operador simplificado
console.log(nombre);

//Hoy ya no se usa var, se usa let (para variables) y const (para constantes)
nombre2 = "Pedro";
console.log(nombre2);

const apellido2 = "Lepes";
//apellido2 = "Peres"; una constante no puede ser modificada
console.log(apellido2);

let x, t; //se pueden crear varias variables dentro de una misma linea
x=17, y=21; //se pueden hacer asignaciones de varias variables dentro de la misma linea
let z = x + y; //se asigna un valor de la operacion
console.log(z);

let _1num = 31; //no utilizar numeros para iniciar el nombre de una variables
let rompiendo = "Rompe"; //no utilizar palabras reservadas para variables

console.log(_1num);
console.log(rompiendo);