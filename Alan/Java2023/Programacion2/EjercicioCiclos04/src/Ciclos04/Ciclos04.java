package Ciclos04;

import java.util.Scanner;
import javax.swing.JOptionPane;

public class Ciclos04 {

    public static void main(String[] args) {
        int num, conteo = 0;

//        Scanner entrada = new Scanner(System.in);
//        
//        System.out.println("Ingrese un numero");
//        num = Integer.parseInt(entrada.nextLine());
//        
//        while (num >0){
//            conteo ++;
//            num = Integer.parseInt(entrada.nextLine());
//        }
//        System.out.println("La cantidad de numeros que ingreso son: "+ conteo);
        num = Integer.parseInt(JOptionPane.showInputDialog("Digite un numero"));
        while (num > 0) {
            conteo++;
            num = Integer.parseInt(JOptionPane.showInputDialog("Digite un numero nuevamente, si desea salir ingrese un numero negativo."));
        }
        System.out.println("La cantidad de numeros ingresados son: " + conteo);
    }
}
