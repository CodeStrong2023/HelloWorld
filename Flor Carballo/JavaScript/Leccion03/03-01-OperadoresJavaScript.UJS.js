//Ejercicio para encontrar números pares
let parInpar = 10;
if(parInpar % 2 == 0){
    console.log("Es un número PAR");
}
else{
    console.log("Es un número IMPAR");
}

//Ejercicio: es mayor de edad
let edad = 20, adulto = 18;
if( edad >= adulto ){
	console.log("Es una persona adulta");
}
else{
	console.log("Es una persona menor de edad")
}
//Ejercicio: Dentro de un rango
let dentroRango = 5; //Aqui vamos a ir cambiando el valor
let valMin = 0, valMax = 10;
if( dentroRango >= valMin && dentroRango <= valMax){
    console.log("Esta dentro del rango establecido")
}
else{
    console.log("Esta fuera del rango establecido")
}

//Ejercicio: Si el padre puede asistir al juego de su hijo
let vacaciones = false, diaDescanso = false;
if(vacaciones || diaDescanso){
	console.log("El padre puede asistir al juego de su hijo")
}
else{
	console.log("El padre NO puede asistir al juego de su hijo")
}

//Operador ternario
let resultado2 = 3 > 2 ? "Verdadero" : "Falso";
console.log(resultado2)
let numero = 12;
resultado2 = numero % 2 == 0 ? "Es un número PAR" : "Es un número IMPAR";
console.log(resultado2)

//Convertir String a Number
let miNumero = "21"; //Es una cadena
console.log(typeof miNumero);
let edad2 = Number(miNumero); //Esta es una función
console.log(typeof edad2);
//Función isNaN
if(isNaN(edad2)){ //No es un número = is Not a Number(devuelve un booleano)
    console.log("Esta variable no contiene solo números")
}
else{
    if(edad2 >= 18){
    console.log("Puede votar");
    }
    else{
    console.log("Muy joven para votar");
    }
}

let resultado3 = edad2 >= 18 ? "Puede votar" : "Muy joven para votar";
console.log(resultado3);

