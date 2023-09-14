
package Ciclos06;

import java.util.Scanner;

public class Ciclos06 {
    public static void main(String[] args) {
        int numero,suma = 0;
        Scanner entrada = new Scanner(System.in);
        do {
            System.out.println("Digite un numero");
            numero = Integer.parseInt(entrada.nextLine());
            suma+= numero;
        } while (numero != 0);
        System.out.println("\nLa suma de todos los numero ingresados es : " + suma);
        
    }
}
