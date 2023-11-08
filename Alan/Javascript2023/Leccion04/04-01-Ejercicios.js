//Ejercicio1: Calcular estacion del año
let mes = 4;
let estacion;
if(mes ==  1 || mes == 2 || mes == 12 ) {
    estacion = "Verano";
}
else if(mes ==  3 || mes == 4 || mes == 5 ) {
    estacion = "Otoño";
}
else if(mes ==  6 || mes == 7 || mes == 8 ) {
    estacion = "Invierno";
}
else if(mes ==  9 || mes == 10 || mes == 11 ) {
    estacion = "Primavera";
}
else{
    estacion = "Valor Incorrecto";
}
console.log("El valor corresponde a la estacion de: "+estacion);

//Ejercicio2: Hora del dia
let horaDia = 9;
let mensaje;
if(horaDia >= 6 && horaDia <= 11){
    mensaje = "Buenos dias";
}
else if(horaDia >= 12 && horaDia <= 16){
    mensaje = "Buen media tarde";
}
else if(horaDia >= 17 && horaDia <= 19){
    mensaje = "Buenas tardes";
}
else if(horaDia >= 20 && horaDia <= 23){
    mensaje = "Buenas noches";
}
else{
    mensaje = "Valor incorrecto"
}
console.log(mensaje);

//Estructura switch
switch(mes){
    case 1: case 2: case 12:
        estacion = "Verano";
        break;
    case 3: case 4: case 5:
        estacion = "Otoño";
        break;
    case 6: case 7: case 8:
        estacion = "Invierno";
        break;
    case 9: case 10: case 11:
         estacion = "Primavera";
         break;
    default: 
    estacion = "Valor incorrecto";
}





var nombre = "Alan"
nombre = "Garrido"
console.log(nombre);

function saludar(){
    var  nombre = "Oscar";
    console.log(nombre);
} 
console.log(nombre); //Aca no lee el dato de la funcion
if(true){
    var edad = 22;
    console.log(edad);
}
console.log(edad);

/*
Let puede ser asignada en cualquier momento
la diferencia es que su ambito es de bloque,
solo disponible  dentro de un bloquye de llaves
o dentro de una funcion
*/
function saludar2(){
    let nombre2 = "Alan";
    console.log(nombre2);
}

//console.log(nombre2);
if(true){
    let edad2 = 20;
    console.log(edad2);
}

const fechaNacimiento = 2000;
console.log(fechaNacimiento);
//fechaNacimiento = 2000;
//console.log(fechaNacimiento);

//evita repetir tu codigo
//try don't repeat yourself
//let days = ["Lunes", "Martes", "Miercoles", "Jueves", "Viernes", "Sabado", "Domingo"];

let days = 1;
switch(days) {
    case 1:
        console.log("Hoy es: Lunes")
        break;
    case 2:
        console.log("Hoy es: Martes")
        break;
    case 3:
        console.log("Hoy es: Miercoles")
        break;
    case 4:
        console.log("Hoy es: Jueves")
        break;
    case 5:
        console.log("Hoy es: Viernes")
        break;
    case 6:
        console.log("Hoy es: Sabado")
        break;
    case 7:
        console.log("Hoy es: Domingo")
        break;
    default:
        console.log("Error al ingresar el dia de la semana")
        break;
}

//esta es la opcion mejorada
let days2 = ["Lunes", "Martes", "Miercoles","Jueves", "Viernes", "Sabado", "Domingo"];
function getDay(n){
    if(n<1 || n>7){
        throw new Error("Out of range");
    }
    return days2(n-1);
}
console.log(getDay(5));

//hacer un ejercicio similar al que esta hecho, pero ahora con los meses del año
//debes hacerlo con la estructura switch y luego con la funcion
//en la opcion mejorada

let month = 3;
switch(month) {
    case 1:
        console.log("este mes es: Enero")
        break;
    case 2:
        console.log("este mes es: Febrero")
        break;
    case 3:
        console.log("este mes es: Marzo")
        break;
    case 4:
        console.log("este mes es: Abril")
        break;
    case 5:
        console.log("este mes es: Mayo")
        break;
    case 6:
        console.log("este mes es: Junio")
        break;
    case 7:
        console.log("este mes es: Julio")
        break;
    case 8:
        console.log("Este mes es: Agosto")
        break;
    case 9:
        console.log("este mes es: Septiembre")
        break;
    case 10:
        console.log("este mes es: Octubre")
        break;
    case 11:
        console.log("este mes es: Noviembre")
        break;
    case 12:
        console.log("este mes es: Diciembre")
        break;   
    default:
        console.log("Error al ingresar el mes")
        break;
}


let month2 = ["Enero", "Febrero", "Marzo","Abril", "Mayo", "Junio", "Julio","Agosto","Septiembre","Octubre","Noviembre","Diciembre"];
function getMonth(n){
    if(n<1 || n>12){
        throw new Error("Out of range");
    }
    return month2(n-1);
}
console.log(getMonth(3));