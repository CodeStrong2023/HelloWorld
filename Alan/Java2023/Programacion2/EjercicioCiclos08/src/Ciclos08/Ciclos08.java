
package Ciclos08;

import java.util.Scanner;
import javax.swing.JOptionPane;

public class Ciclos08 {
    public static void main(String[] args) {       
        Scanner entrada = new Scanner (System.in);
        int num, conteo = 0;
        
//        System.out.println("Ingrese un numero, se mostrara desde el 1 hasta su numero.");
//        num = Integer.parseInt(entrada.nextLine());
//        System.out.println("---------------------");
//        
//        while (conteo < num){
//            conteo++;
//            System.out.println(conteo);
//        }
        
        num = Integer.parseInt(JOptionPane.showInputDialog("Ingrese un numero, se mostrara desde el 1 hasta su numero."));
        
        while (conteo < num){
            conteo++;
            System.out.println(conteo);
        }
    }
}
