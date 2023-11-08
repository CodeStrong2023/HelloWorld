var nombre = 'Jose';
var apellido = ' Montes';
var nombreCompleto = nombre+ ' ' +apellido; //Primera concatenacion
console.log(nombreCompleto);
var nombreCompleto2 = 'Ariel' +' '+'Betancud';
console.log(nombreCompleto2); // Segunda concatenacion
var juntos = nombre + 219; //Lee de izq a der siguiendo la cadena lee el numero como str
console.log(juntos);
juntos = nombre + (78 + 17) //Aqui se puede diferencia a traves de los parentesis
console.log(juntos);
juntos = 78 + 17 + nombre;
console.log(juntos);

nombre += apellido; //Tercera Concatenacion usando el operador simplificado
console.log(nombre);
