/*
Ejerciio 03 : leer numeros hasta que se introduzca un cero
para cad auno identificar si es par o impar
primero con la clase scanner 
luego con joptionpane
*/
package CIclos03;

import javax.swing.JOptionPane;



public class Ejercicio03 {
    public static void main(String[] args) {

        int numero = Integer.parseInt(JOptionPane.showInputDialog("DIGITE UN NUMERO"));
        while (numero != 0) {            
            if(numero % 2 == 0){
                JOptionPane.showMessageDialog(null,"el numero ingresado "+numero+" es PAR");
            }
            else{
                JOptionPane.showMessageDialog(null,"el numero ingresao "+ numero + " es IMPAR");
            }
            numero = Integer.parseInt(JOptionPane.showInputDialog("DIGITE OTRO NUMERO"));
        }
        JOptionPane.showMessageDialog(null,"el numero ingresado es " +numero+ " finaliza el programa");
        
        
    }
}
