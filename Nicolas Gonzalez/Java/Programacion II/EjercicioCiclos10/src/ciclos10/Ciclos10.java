
package ciclos10;

import java.util.Scanner;
import javax.swing.JOptionPane;

public class Ciclos10 {
    public static void main(String[] args) {
        Scanner entrada = new Scanner(System.in);
        int num, suma = 0;
        
//        for (int i = 1; i<=10; i++){
//            System.out.println("Ingrese el numero "+i+": ");
//            num = Integer.parseInt(entrada.nextLine());
//            suma += num;
//        }
//        System.out.println("La suma es: "+ suma);

          for (int i = 1; i<=10; i++){
              num = Integer.parseInt(JOptionPane.showInputDialog("Ingrese el numero "+i+": "));
              suma+=num;
          }
          System.out.println("La suma es: "+suma);
    }
}
