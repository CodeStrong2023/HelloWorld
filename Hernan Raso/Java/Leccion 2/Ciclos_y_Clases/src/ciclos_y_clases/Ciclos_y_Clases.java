/*
Ejercicio 1: Leer un numero y mostrar su cuadrado, repetir el procesos hasya que se introduzca un numero negativo
*/
package ciclos_y_clases;

import java.util.Scanner;


public class Ciclos_y_Clases {

   
    public static void main(String[] args) {
        Scanner entrada = new Scanner(System.in);
        int numero, cuadrado;
        System.out.println("Ingrese un numero:");
        numero = Integer.parseInt(entrada.nextLine());
        while(numero >= 0) {
            cuadrado = (int)Math.pow(numero, 2);
            System.out.println("El numero " +numero+ "elevado al cuadrado es: "+cuadrado);
            System.out.println("Ingrese otro numero: ");
            numero = Integer.parseInt(entrada.nextLine());
            
        
        }
        System.out.println("El Programa a Finalizado por un numero Negativo");
    }
    
}
