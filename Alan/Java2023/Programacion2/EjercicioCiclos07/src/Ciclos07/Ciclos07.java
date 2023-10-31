package Ciclos07;

import java.util.Scanner;
import javax.swing.JOptionPane;

public class Ciclos07 {

    public static void main(String[] args) {
        Scanner entrada = new Scanner(System.in);
        int num, media = 0, sumaNum = 0;
        float resultado;

//        System.out.println("Ingrese un numero: ");
//        num = Integer.parseInt(entrada.nextLine());
//        while (num >= 0) {
//            media++;
//            sumaNum += num;
//            System.out.println("Introduce otro numero, para salir ingrese un numero negativo.");
//            num = Integer.parseInt(entrada.nextLine());
//        }
//        resultado = (float) sumaNum / media;
//        System.out.println("El promedio es: " + resultado);

        num = Integer.parseInt(JOptionPane.showInputDialog("Ingrese un numero: "));
        while (num >= 0){
            media++;
            sumaNum += num;
            num = Integer.parseInt(JOptionPane.showInputDialog("Ingrese otro numero, para salir ingrese un numero negativo."));
        }
        resultado = (float) sumaNum/media;
        System.out.println("El promedio es: "+resultado);       
    }
}
