//ejercicio 2: 
package matriz_ejercicio_2;

import java.util.Scanner;

public class Matriz_Ejercicio_2 {
    public static void main(String[] args) {
        Scanner entrada = new Scanner(System.in);
        int matriz[][] = new int [7][7];
        
        //llenando matriz
        for (int i = 0; i < 7; i++) {
            for (int j = 0; j < 7; j++) {
                if(i==j){
                    matriz[i][j] =1;
                }
                else{
                    matriz[i][j] = 0;
                }
            }
        }
        
        System.out.println("\nMostramos matriz completa: ");
        for (int i = 0; i < 7; i++) {
            for (int j = 0; j < 7; j++) {
                System.out.println(matriz[i][j]+" ");
            }
            System.out.println("");
        }
        System.out.println("");
    }
}
