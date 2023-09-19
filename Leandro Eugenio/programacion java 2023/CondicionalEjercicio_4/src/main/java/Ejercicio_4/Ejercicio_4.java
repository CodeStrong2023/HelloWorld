
package Ejercicio_4;

import java.util.Scanner;

public class Ejercicio_4 {
    public static void main(String[] args) {
        Scanner entrada = new Scanner(System.in);
        System.out.println("Digite un numero entre 0 y 10: ");
        var calificacion = Integer.parseInt(entrada.nextLine());
        switch(calificacion){
            case 1 : case 2 : case 3 : case 4 : case 5 :
                System.out.println("F");
                break;
            case 6 :
                System.out.println("D");
                break;
            case 7 :
                System.out.println("C");
                break;
            case 8 :
                System.out.println("B");
                break;
            case 9 : case 10 :
                System.out.println("A");
                break;
        }
        
    }
          
}
