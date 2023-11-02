//Ejercicio para encontrar numeros pares
let parInpar  = 10;
if(parInpar % 2 == 0){
    console.log("Es un numero PAR");
}
else{
    console.log("Es  un numero IMPAR");
}

//Ejercicio: es mayor de edad
let edad = 14, adulto =18;
if( edad >= adulto ){
    console.log("Es una persona adulta");
}
else{
    console.log("Es una persona menor de edad");
}


//Ejercicio: Dentro de un rango
let dentroRango = 5; //aqui vamos cambiando valor
let valMin = 0, valMax = 10;
if ( dentroRango >= valMin && dentroRango <= valMax){
    console.log("Esta dentro del rango establecido");
}
else{
    console.log("Esta fuera del rango establecido");
}

//Ejercicio: Si el padre puede asistir al juego de su hijo
let vacaciones = false, diaDescanso = false;
if(vacaciones || diaDescanso){
    console.log("El padre puede asistir al juego de su hijo")
}
else{
    console.log("El padre no puede asistir al juego de su hijo")
}
//Operador ternario
let resultado2 = 3 > 2 ? "Verdadero" : "Falso";
console.log(resultado2) 
let numero = 12;
resultado2 = numero % 2 == 0 ? "Es un numero PAR" : "Es un numero IMPAR";
console.log(resultado2)

//Convertir String a Numer
let miNumero = "10"; //Es una cadena
console.log(typeof miNumero);
let edad2 = Numer(miNumero); //Esta es una funcion 
console.log(typeof edad2);
//Funcion isNaN
if(isNaN(edad2)){
    console.log("La variable no contiene solo numeros");
}
    if(edad2 >= 18){
        console.log("Puede votar");
}
    else{
        console.log("Demaciado joven para votar");
}
let resultado3 = edad2 >= 18 ? "Puede votar" : "Muy joven para votar";
console.log(resultado3);

