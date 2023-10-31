/*
Ejercicio 2:Leer 5 numeros, guardarlos en un arreglo y 
mostrarlos en el orden inverso introducidos
*/
package arreglos_ejercicio_2;

import java.util.Scanner;

public class Arreglos_Ejercicio_2 {
    public static void main(String[] args) {
        Scanner entrada = new Scanner(System.in);
        float[] arreglo = new float[5];
        
        System.out.println("Guardando los datos del arreglo");
        for (int i = 0; i < 5; i++) {
            System.out.println((i+1)+". Digite un numero: ");
            arreglo[i] = entrada.nextFloat();
        }
        
        System.out.println("\nImprimir los elementos del arreglo");
        for (int i = arreglo.length-1; i >= 0; i--) {
            System.out.println(arreglo[i]+" ");
            
        }
        
        System.out.println("\n");
    }
}
