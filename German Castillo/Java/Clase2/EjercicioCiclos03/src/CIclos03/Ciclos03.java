/*
Ejerciio 03 : leer numeros hasta que se introduzca un cero
para cad auno identificar si es par o impar
primero con la clase scanner 
luego con joptionpane
*/
package CIclos03;

import java.util.Scanner;

public class Ciclos03 {
    public static void main(String[] args) {
        Scanner entrada = new Scanner(System.in);
        int numero;
        System.out.println("digite un numero");
        numero = Integer.parseInt(entrada.nextLine());
        while (numero != 0) {            
            if(numero % 2 == 0){
                System.out.println("el numero ingresado "+numero+" es PAR");
            }
            else{
                System.out.println("el numero ingresao "+ numero + " es IMPAR");
            }
            System.out.println("digite OTRO numero");
            numero = Integer.parseInt(entrada.nextLine());
        }
        System.out.println("el numero ingresado es " +numero+ " finaliza el programa");
        
    }
}
