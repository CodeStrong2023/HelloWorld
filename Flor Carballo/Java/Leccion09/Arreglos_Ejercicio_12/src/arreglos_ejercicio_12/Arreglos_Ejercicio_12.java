/*
Ejercicio 12: Leer por teclado una tabla de 10 elementos númericos enteros y una posición(entre 0 y 9).
Eliminar el elemento situado en la posición dada sin dejar hueco
 */
package arreglos_ejercicio_12;

import java.util.Scanner;

public class Arreglos_Ejercicio_12 {
    public static void main(String[] args) {
        Scanner entrada = new Scanner(System.in);
        int arreglo[] = new int[10];
        int posicion, j=0;
        
        System.out.println("Llenar el arreglo: ");
        for (int i = 0; i < 10; i++) {
            System.out.println(i+". Digite un número: ");
            arreglo[i] = entrada.nextInt();
        }
        System.out.println();
        do{
            System.out.println("Digite una posición a eliminar entre (0-9): ");
            posicion = entrada.nextInt();
        }while(posicion < 0 || posicion > 9);
        
        //Eliminando el elemento de posición indicada
        for(int i= posicion; i<9;i++){
            arreglo[i] = arreglo[i+1];
        }
        System.out.println("\nEl arreglo queda: ");
        for(int i=0; i<9;i++){
            System.out.println(arreglo[i]+" - ");
        }
        System.out.println();
    }
}
