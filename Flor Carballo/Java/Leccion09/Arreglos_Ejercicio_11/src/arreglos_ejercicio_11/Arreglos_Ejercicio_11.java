/*
Ejercicio 11: Leer 5 elementos numéricos que se introducirán ordenados de forma creciente. Estos los guardaremos en una table
de tamaño 10. Leer un numero N e insertarlo en el lugar adecuado para que la tabla continue ordenada.
 */
package arreglos_ejercicio_11;

import java.util.Scanner;

public class Arreglos_Ejercicio_11 {
    public static void main(String[] args) {
        Scanner entrada = new Scanner(System.in);
        int arreglo[] = new int[10];
        boolean creciente = true;
        int numero, sitio_num=0, j=0;
        
        System.out.println("Llenar el arreglo: ");
        do{
            //Llenando el arreglo
            for (int i = 0; i < 5; i++) {
                System.out.println((i+1)+". Digite un numero: ");
                arreglo[i] = entrada.nextInt();
            }
            //Comprobar si el arreglo esta ordenado en forma creciente
            for (int i = 0; i < 4; i++) {
                if(arreglo[i] < arreglo[i+1]){
                    creciente = true;
                }
                if(arreglo[i] > arreglo[i+1]){
                    creciente = false;
                    break;
                }
            }
            if(creciente == false){
                System.out.println("\nEl arreglo no esta ordenado en forma creciente, vuelva a digitar\n");
            }
        }while(creciente == false);
        
        System.out.println("Digite un número a insertar: ");
        numero = entrada.nextInt();
        
        //Esto es para darnos cuenta en que posición va el número
        while(arreglo[j]<numero && j<5){
            sitio_num++;
            j++;
        }
        //Por último, trasladamos una posición en el arreglo a los elementos que van detrás de número
        for(int i=4; i>=sitio_num;i--){
            arreglo[i+1] = arreglo[i];
        }
        //Insertamos el número
        arreglo[sitio_num] = numero;
        
        System.out.println("\nEl arreglo queda: ");
        for(int i=0;i<6;i++){
            System.out.println(arreglo[i]+" - ");
        }
        System.out.println();
    }
}
