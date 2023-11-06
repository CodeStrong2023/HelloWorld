
package arreglos_ejercicio_1;

import java.util.Scanner;


public class Arreglos_Ejercicio_1 {
    public static void main(String[] args) {
        Scanner entrada = new Scanner(System.in);
        float[] numeros = new float[5];
        
        System.out.println("guarfamos datos en arreglo");
        for (int i = 0; i < 5; i++) {
            System.out.println((i+1)+". Digite un numero: ");
            numeros[i] = entrada.nextFloat();
        }
        
        for (float i:numeros){
            System.out.println(i+ " ");
            
        }
        System.out.println("\n");
    }

}
