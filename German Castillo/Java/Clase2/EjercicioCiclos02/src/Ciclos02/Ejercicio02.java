/*
Ejercicio 2: Leer un numero e indicar si es positivo o negativo.El proceso 
se repetira hasta que se introduzca un 0

*/
package Ciclos02;

import javax.swing.JOptionPane;

public class Ejercicio02 {
    public static void main(String[] args) {
        int numero;
        numero = Integer.parseInt(JOptionPane.showInputDialog("DIGITE UN NUMERO"));
        while (numero != 0) {            
            if (numero > 0) {
                System.out.println("Es positivo");
            }else if(numero < 0){
                System.out.println("Es negativo");
            }
            numero = Integer.parseInt(JOptionPane.showInputDialog("DIGITE UN NUMERO"));
            
            
        }
    }
}
