//Ampliando el uso de var let y const
/*
Con var puedes resignar en cualquiero momento
este forma parte del ambito global
Un error es que se sobreescriba
*/
var nombre = "Ariel";
nombre = "Flor";
console.log(nombre);

function saludar(){
    var nombre3 = "Natalia";
    console.log(nombre3);
}
//console.log(nombre3); //Aquí no lee el dato en la función

if (true){
    var edad = 34;
    console.log(edad);
}
console.log(edad); //En la función funciono correctamente, en la estructura if fallo

/*
let: esta puede ser reasignada en cualquier momento
la diferencia es que su ambito es de bloque,
solo disponible dentro de un bloque de llaves
o dentro de una función
*/
function saludar2(){
    let nombre2 = "Ariel";
    console.log(nombre2);
}
//console.log(nombre2);

if(true){
    let edad = 33;
    //console.log(edad2);
}
//console.log(edad2);

/*
const se utiliza para valores constantes que no pueden ser reasignadas
*/
const fechaNacimiento = 2006;
console.log(fechaNacimiento);
//fechaNacimiento = 2003;
//console.log(fechaNacimiento); //solo se ejecuta el console anterior

