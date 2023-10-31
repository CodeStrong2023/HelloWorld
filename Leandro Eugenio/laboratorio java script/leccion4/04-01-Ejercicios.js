//Ejercicio 1 : calcular estacion del año
let mes = 4;
let estacion;
if (mes == 1 || mes == 2 || mes == 12) {
    estacion = "Vernao"
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
    mensaje = "Good night"
}
else {
    mensaje = "valor incorrecto"
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
        estacion = "valor incorrecto"
}
console.log("bienvenidos a la estacion de : "+estacion)