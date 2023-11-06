
package ejerciciociclos03;

import java.util.Scanner;
import javax.swing.JOptionPane;

public class EjercicioCiclos03 {

    public static void main(String[] args) {
        Scanner entrada = new Scanner (System.in);
        int num;
        
//        System.out.println("Ingrese un numero");
//        num = Integer.parseInt(entrada.nextLine());
//        
//        while (num != 0){
//            if (num % 2 == 0){
//                System.out.println("Numero par");
//            }
//            else{
//                System.out.println("Numero impar");
//            }
//            System.out.println("Ingrese un numero nuevo, si desea salir ingrese 0");
//            num = Integer.parseInt(entrada.nextLine());
//        }

        num = Integer.parseInt(JOptionPane.showInputDialog("Digite un numero"));
        while (num !=0){
            if (num % 2 == 0){
                System.out.println("El numero es par");
            }
            else{
                System.out.println("El numero es impar");
            }
            num = Integer.parseInt(JOptionPane.showInputDialog("Digite un numero otra vez, si desea salir ingrese 0. "));
        }
    }
    
}
