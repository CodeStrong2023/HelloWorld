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
let dentroRango = 5; //Aqui vamos a ir cabiando el valor
let valMin =0, valMax = 10;
if(dentroRango >= valMin && dentroRango <= valMax){
    console.log("Esta dentro del rango establecido")
}else{
    console.log("Esta dentor del rango establecido")
}

//Ejercicio si el padre puede asistir al juego de su hijo
let vacaciones = false,diaDescanso = false;
if(vacaciones || diaDescanso){
    console.log("El padre puede asistir")}
else{
    console.log('el padre no puede asistir')

}

//Operador ternario
let resultado = 3 > 2 ? "VERDADERO" : "FALSO";

console.log(resultado);
let numero = 8;
resultado= numero % 2 == 0 ? "Par" : "Impar";

//Convertir string a numero
let miNumero = "10"
console.log(typeof miNumero);
let edad2 = Number(miNumero);
console.log(typeof edad2);
if(isNaN(edad2)){
    console.log("Esta variable no contiene numeros")
}

if(edad2 >= 18){
    console.log("Puede votar")
}else{
    console.log("No puede votar")
}

let resultado3 = edad2 >= 18 ? "Puede votar" : "No puede votar";
console.log(resultado3)
 
//convertir string a numbre
