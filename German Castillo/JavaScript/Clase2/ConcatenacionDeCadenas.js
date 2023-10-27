var nombre = 'German';
var apellido = 'Castillo';
var nombreCompleto = nombre +' '+  apellido;
console.log(nombreCompleto)
var nombreCompleto2 = 'Lionel'+' '+'Messi';
console.log(nombreCompleto2);
var juntos = nombre + 219;//leee de izquierda a dere siguiendo la cadena lee el numero con str
console.log(juntos)
juntos = nombre + 78 + 17;//
console.log(juntos);
juntos = 78 + 17 + nombre;
console.log(juntos)

nombre += apellido;//Tercera concatenacion usando el operador simplificado
console.log(nombre)

//hoy ya no hay que usar var, se utiliza let y const

let nombre2 = "Carina";
console.log(nombre2)

const apellido2 = "Carrion";
//apellido2 = "Perez" una constante no puede ser modificada
console.log(apellido2);
