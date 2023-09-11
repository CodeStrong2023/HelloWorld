
package Ciclos03;

import javax.swing.JOptionPane;


public class Ciclos03ConJOpcionPane {
    public static void main(String[] args) {
    int numero;
        numero = Integer.parseInt(JOptionPane.showInputDialog("Ingrese un numero"));
        while(numero != 0){
            if(numero % 2 == 0){
                JOptionPane.showMessageDialog(null, "El numero ingresado "+numero+" es Par");
            }
            else {
               JOptionPane.showMessageDialog(null, "El numero ingresado "+numero+" es Impar");;
            
            }
            numero = Integer.parseInt(JOptionPane.showInputDialog("Ingrese otro numero"));;
        }
        JOptionPane.showMessageDialog(null, "El numero Ingresado es "+numero+" finaliza el programa");
    }
}