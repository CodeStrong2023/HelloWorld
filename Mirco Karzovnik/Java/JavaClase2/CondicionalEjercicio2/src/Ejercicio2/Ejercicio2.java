
package Ejercicio2;

import java.util.Scanner;

public class Ejercicio2 {
    public static void main(String[] args) {
        
        Scanner entrada = new Scanner(System.in);
        System.out.println("Ingrese el numero de mes: ");
        var numeromes = Integer.parseInt(entrada.nextLine());
        
    switch(numeromes){
        case 1: case 2: case 3:
            System.out.println("Verano");
            break;
        case 4: case 5: case 6:
            System.out.println("Otonio");
            break;
        case 7: case 8: case 9:
            System.out.println("Invierno");
            break;
        case 10: case 11: case 12:
            System.out.println("Primavera");
            break;
        default:
            System.out.println("Numero de mes incorrecto");
            
    }  
        
    }
}
