
package Ciclos06;

import java.util.Scanner;
import javax.swing.JOptionPane;

public class Ejercicios06 {
     public static void main(String[] args) {
        int numero,suma = 0;
        do {
            numero = Integer.parseInt(JOptionPane.showInputDialog("Digite un numero: "));
            suma+= numero;
        } while (numero != 0);
        JOptionPane.showMessageDialog(null, "\nLa suma de todos los numero ingresados es : " + suma);
        
    }
}
