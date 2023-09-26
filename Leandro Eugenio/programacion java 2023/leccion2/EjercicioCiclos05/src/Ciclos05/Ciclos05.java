/*
 Ejercicio 05: Realizar un juego apra adivinar un unmero,
para ello generar un numero aleatoprio entre 0-100, y
luego ir pidiendo numeros indicando " es mayor" o "es menor"
segun sea mayor o menor con respecto a N
El proceso termina cuando eñ usuario acierta y mostramos
el numero de intentos hechos
 */
package Ciclos05;

import java.util.Scanner;

public class Ciclos05 {
    public static void main(String[] args) {
        Scanner entrada = new Scanner(System.in);
        int numero, aleatorio, conteo =0;
        aleatorio = (int)(Math.random()*100);
        System.out.println("Digite un numero: " );
        do {            
            numero = Integer.parseInt(entrada.nextLine());
            if (numero < aleatorio) {
                System.out.println("Digite un numero mayor");
            }else{
                System.out.println("Digite un numero menor");
            }
            conteo ++;
        } while (aleatorio != numero);
        System.out.println("Adivinaste el numero");
        System.out.println("la cantidad de intentos fue: "+conteo);
    }
}
