package Ejericicio02;

import java.util.Scanner;
import javax.swing.JOptionPane;

public class Ejericicio02 {

    public static void main(String[] args) {
//        Scanner entrada = new Scanner(System.in);
//        System.out.println("Ingrese un numero: ");
//        Integer num = Integer.parseInt(entrada.nextLine());
//
//        while (num != 0) {
//            if (num < 0) {
//                System.out.println("Su numero es negativo.");
//            } else {
//                System.out.println("Su numero es positivo.");
//            }
//            System.out.println("Ingrese el siguiente numero, si quiere parar, ingrese 0.");
//            num = Integer.parseInt(entrada.nextLine());
//        }
        Integer num = Integer.parseInt(JOptionPane.showInputDialog("Ingrese un numero: "));
        
        while (num != 0){
            if (num < 0){
                System.out.println("El numero es negativo.");
            }
            else {
                System.out.println("El numero es positivo.");
            }
            num = Integer.parseInt(JOptionPane.showInputDialog("Para salir ingrese 0, si desea continuar, ingrese otro numero: "));
        }
    }
}
