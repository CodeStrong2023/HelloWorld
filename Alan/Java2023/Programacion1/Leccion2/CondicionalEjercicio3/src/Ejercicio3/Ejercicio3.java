package Ejercicio3;

import java.util.Scanner;

public class Ejercicio3 {

    public static void main(String[] args) {
        Scanner entrada = new Scanner(System.in);
        System.out.println("Ingrese una nota entre 0 y 10: ");
        var nota = Integer.parseInt(entrada.nextLine());

//        if (nota <= 10 && nota >= 9){
//            System.out.println("Calificacion: A");
//        }
//        else if(nota >= 8 && nota <9){
//            System.out.println("Calificacion: B");
//        }
//        else if (nota >=7 && nota < 8){
//            System.out.println("Calificacion: C");
//        }
//        else if (nota >=6 && nota <7){
//            System.out.println("Calificacion: D");
//        }
//        else if (nota >=0 && nota <6){
//            System.out.println("Calificacion: F");
//        }
//        else{
//            System.out.println("Nota incorrecta");
//        }
    
    switch(nota){
        case 10: case 9:
            System.out.println("Calificacion: A");
            break;
        case 8:
            System.out.println("Calificacion: B");
            break;
        case 7:
            System.out.println("Calificacion: C");
            break;
        case 6:
            System.out.println("Calificacion: D");
            break;
        case 5: case 4: case 3: case 2: case 1: case 0:
            System.out.println("Calificacion: F");
            break;
        default: 
            System.out.println("Nota incorrecta.");
    }
    }
}
