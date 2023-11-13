//Ejercicio 1 : calcular estacion del año
let mes = 4;
let estacion;
if (mes == 1 || mes == 2 || mes == 12) {
    estacion = "Verano"
}
else if (mes == 3 || mes == 4 || mes == 5) {
    estacion = "Otoño"
}
else if (mes == 6 || mes == 7 || mes == 8) {
    estacion = "Invierno"
}
else if (mes == 9 || mes == 10 || mes == 11) {
    estacion = "Primavera"
}
else {
    estacion = "valor incorrecto"
}
console.log("El valor corresponde a la estacion: " + estacion)
//Ejercicio 2 : Hora del dia
/*
de 6 a 11 nos saluda: Good Morning
de 12 a 16 nos saluda: Good Afternoom
de 17 a 19 nos saluda: Good Evening
de 20 a 23 nos saluda: Good night
Trabajremos con 24 horas
*/
let horaDia = 9;
let mensaje;
if (horaDia >= 6 && horaDia <= 11) {
    mensaje = "Good Morning"
}
else if (horaDia >= 12 && horaDia <= 16) {
    mensaje = "Good Afternoom"
}
else if (horaDia >= 17 && horaDia <= 19) {
    mensaje = "Good Evening"
}
else if (horaDia >= 20 && horaDia <= 23) {
    mensaje = "Good Night"
}
else {
    mensaje = "Valor incorrecto"
}
console.log(mensaje)



//Estructura switch(LA SINTAXIS ES IGUAL A JAVA)
switch (mes) {
    case 1: case 2: case 12:
        estacion = "Verano"
        break;
    case 3: case 4: case 5:
        estacion = "Otoño"
        break;
    case 6: case 7: case 8:
        estacion = "Invierno"
        break;
    case 9: case 10: case 11:
        estacion = "Primavera" 
        break;
    default:
        estacion = "Valor incorrecto"
}
console.log("Bienvenidos a la estacion de : "+estacion)

/*
    const se utiliza para valores constantes que no pueden ser reasignados
*/

const fechaDeNacimiento = 2003;
console.log(fechaDeNacimiento)

//EVITAR REPETIR TU CODIGO
//Dry don`t repeat yourself

let days = 'Lunes'


switch (days) {
    case 'Lunes':
        console.log('hoy es' + days)
        break;
    case 'Martes':
        console.log('hoy es' + days)
        break;
    case 'Miercoles':
        console.log('hoy es' + days)
        break;
    case 'Jueves':
        console.log('hoy es' + days)
        break;
    case 'Viernes':
        console.log('hoy es' + days)
        break;
    case 'Sabado':
        console.log('hoy es' + days)
        break;
    case 'Domingo':
        console.log('hoy es' + days)
        break;

    default:
        console.log('Error en el ingreso del dia de la semana')
        break;
}

//ESTA ES LA OPCION MEJORADA

let days2 = ['Lunes', 'Martes', 'Mieroles', 'Jueves', 'Vierenes', 'Sabado', 'Domingo'];

function getDay(n) {
    if (n < 1 || n > 7) {
        throw new Error('out of range');
    }
    return days2[n - 1]
}

console.log(getDay(5))


/// Hacer un ejercicio simial al quie esta hechoi, pero ahora con 
//los meses del año, deben hacerlo con la estructura switch y luego
//con la funcion en la opcion mejorada
mes = 'Enero'
switch (mes) {
    case 'Enero':
        console.log('estamos en el mes de: ' + mes)
        break;
    case 'Febrero':
        console.log('estamos en el mes de: ' + mes)
        break;
    case 'Marzo':
        console.log('estamos en el mes de: ' + mes)
        break;
    case 'Abril':
        console.log('estamos en el mes de: ' + mes)
        break;
    case 'Mayo':
        console.log('estamos en el mes de: ' + mes)
        break;
    case 'Junio':
        console.log('estamos en el mes de: ' + mes)
        break;
    case 'Julio':
        console.log('estamos en el mes de: ' + mes)
        break;
    case 'Agosto':
        console.log('estamos en el mes de: ' + mes)
        break;
    case 'Septiembre':
        console.log('estamos en el mes de: ' + mes)
        break;
    case 'Octubre':
        console.log('estamos en el mes de: ' + mes)
        break;
    case 'Noviembre':
        console.log('estamos en el mes de: ' + mes)
        break;
    case 'Diciembre':
        console.log('estamos en el mes de: ' + mes)
        break;

    default:
        console.log('Error no corresponde a un mes')
        break;
}

//OPCION MEJORADA
let mes2 = ['Enero','Febrero','Marzo','Abril','Mayo','Junio','Julio','Agosto','Septiembre','Octubre','Noviembre','Diciembre']

function getMes(mes) {
    if(mes<1 || mes >12){
        throw new Error('out of range')
    }
    return mes2[mes-1]
}

console.log(getMes(5))