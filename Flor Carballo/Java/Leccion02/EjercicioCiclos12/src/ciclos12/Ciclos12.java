/*
Ejercicio 12: Pedir un número y calcular su factorial. Hacerlo con las dos clases.
 */
package ciclos12;

import java.util.Scanner;

public class Ciclos12 {
    public static void main(String[] args) {
        Scanner entrada = new Scanner(System.in);
        long factorial = 1;
        System.out.println("Digite un número: ");
        int numero = Integer.parseInt(entrada.nextLine());
        for(int i=1; i<=numero;i++){
            factorial *= i;
        }
        System.out.println("\nEl factorial del número ingresado es: "+factorial);
    }
}
