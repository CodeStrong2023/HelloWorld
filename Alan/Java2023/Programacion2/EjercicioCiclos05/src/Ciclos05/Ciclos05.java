
package Ciclos05;

import java.util.Scanner;


public class Ciclos05 {
    public static void main(String[] args) {
        Scanner entrada = new Scanner(System.in);
        int num, conteo = 0, numRandom;
        numRandom = (int)(Math.random()*100);//esto hace un numero aleatorio
        
        System.out.println("Adivine el numero. Ingrese un numero del 1 al 100: ");
        num = Integer.parseInt(entrada.nextLine());
        while (num != numRandom && num != numRandom){
            if (numRandom < num){
                System.out.println("El numeres menor a: "+ num);
            }
            else if(numRandom > num){
                System.out.println("El numeroes mayor a: "+ num);
            }
            conteo++;
            System.out.println("Ingrese un numero nuevo: ");
            num = Integer.parseInt(entrada.nextLine());
        }
        System.out.println("Felicidades, acerto, el numero era: "+ numRandom);
        System.out.println("La cantidad de intentos fueron: "+conteo);
    }
}
