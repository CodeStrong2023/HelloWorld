//Ejercicio 1: crear y cargar una matriz 3x3, transponerla y mostrarla

package Matriz_Ejercicio_1;

import java.util.Scanner;

public class Matriz_Ejercicio_1 {
    public static void main(String[] args) {
        Scanner entrada = new Scanner(System.in);
        int matriz[][] = new int [3][3];
        
        System.out.println("Rellenar matriz: ");
        for (int i = 0; i < 3; i++) {
            for (int j = 0; j < 3; j++) {
                System.out.println("Matriz ["+i+"]["+j+"]: ");
                matriz[i][j] = entrada.nextInt();              
            }
        }
        System.out.println("");
        
        System.out.println("Matriz original: ");
        for (int i = 0; i < 3; i++) {
            for (int j = 0; j < 3; j++) {
                System.out.println(matriz [i][j]+" ");
            }
            System.out.println();
            
        }
        System.out.println();
    }
}
