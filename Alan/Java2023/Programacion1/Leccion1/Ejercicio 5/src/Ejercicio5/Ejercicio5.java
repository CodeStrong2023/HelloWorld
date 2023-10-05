
package Ejercicio5;

import java.util.Scanner;

public class Ejercicio5 {
    public static void main(String[] args) {
        Scanner entrada = new Scanner(System.in);
        float nota1,nota2,nota3,suma;
        
        System.out.println("Ingrese la primer nota: ");
        nota1 = Float.parseFloat(entrada.nextLine());
        System.out.println("Ingrese la segunda nota: ");
        nota2 = Float.parseFloat(entrada.nextLine());
        System.out.println("Ingrese la tercer nota: ");
        nota3 = Float.parseFloat(entrada.nextLine());
        
        suma = nota1 + nota2 + nota3;
        System.out.println("La suma de las notas es: " + suma);
    }
}
