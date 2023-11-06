
package ciclos12;

import java.util.Scanner;
import javax.swing.JOptionPane;


public class Ciclos12 {
    public static void main(String[] args) {
        int num;
        long factorial=1;
        Scanner entrada = new Scanner(System.in);
               
//        System.out.println("Ingrese un numero: ");
//        num = Integer.parseInt(entrada.nextLine());
//        
//        for (int i =1; i<=num;i++){
//            factorial*=i;
//        }
//        System.out.println("El factorial del numero es: "+factorial);


        num = Integer.parseInt(JOptionPane.showInputDialog("Ingrese un numero: "));
        
        for (int i = 1; i <= num; i++){
            factorial *=i;
        }
        JOptionPane.showInputDialog("El factorial del numero es: "+factorial);
    }
}
