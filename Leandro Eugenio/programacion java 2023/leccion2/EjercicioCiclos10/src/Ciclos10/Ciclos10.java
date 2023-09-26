/*
 Ejercicio 10 : Pedir 10 numeros y escrinir lña suma
 total
Hacerlo con la clase Scanner y JOptionPane
*/
package Ciclos10;

import java.util.Scanner;

public class Ciclos10 {
    public static void main(String[] args) {
        Scanner entrada = new Scanner(System.in);
        int numero,suma = 0;
        for (int i = 0; i <= 10; i++) {
            System.out.println("Digite un numero");
            numero= Integer.parseInt(entrada.nextLine());
            suma += numero;
        }
        System.out.println("\nla suma de todos los numeros es: "+suma);
    }
}
    
