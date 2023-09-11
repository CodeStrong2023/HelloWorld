/*
Ejercicio 2: Leer un numero e indicar si es positivo o negativo. El proceso se repetira hasta que se ingrese un cero 0
*/
package ciclos_y_clases;

import java.util.Scanner;


public class EjercicioCiclos02 {
    public static void main(String[] args) {
        Scanner entrada = new Scanner(System.in);
        System.out.println("Ingrese un numero: ");
        var numero = Integer.parseInt(entrada.nextLine());
        while(numero != 0){
            if(numero > 0){
                System.out.println("El numero " +numero + " es positivo");
            }
            else{
                System.out.println("EL numero "+numero + " es Negativo");
            }
            System.out.println("Ingrese otro numero: ");
            numero = Integer.parseInt(entrada.nextLine());
        
        }
        System.out.println("El numero "+numero+ " Finaliza el programa");
    }
}
