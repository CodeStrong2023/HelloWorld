/*
Ejercicio 3: Leer números hasta que se introduzca un cero
Para cada uno indicar si es par o impar,
Primero con clase Scanner y luego JOptionPane
*/
package Ciclos03;

import javax.swing.JOptionPane;

public class Ejercicio03 {
     public static void main(String[] args) {
        int numero;
        numero = Integer.parseInt(JOptionPane.showInputDialog("Digite un numero: "));
        while(numero != 0){
            if(numero % 2 == 0){
                JOptionPane.showMessageDialog(null, "El número ingresado "+numero+" es PAR");
            }
            else{
                JOptionPane.showMessageDialog(null, "El número ingresado "+numero+" es IMPAR");
            }
             numero = Integer.parseInt(JOptionPane.showInputDialog("Digite otro numero: "));
        }
        JOptionPane.showMessageDialog(null, "El numero ingresado es "+numero+" finaliza el programa");
    }
}
