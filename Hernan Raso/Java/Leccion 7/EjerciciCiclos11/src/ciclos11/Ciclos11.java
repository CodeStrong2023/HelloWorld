/*
Ejercicio 11: Diseñar un programa que muestre el producto de los 10 primeros numero impares, Hacerlo con
JOptionpane
*/
package ciclos11;

import javax.swing.JOptionPane;


public class Ciclos11 {
    public static void main(String[] args) {
        long producto = 1;
        for(int i = 1; i<=20 ;i+=2){ //El aumento apunta solo a ir por los impares
            producto *= i;
        }
        JOptionPane.showMessageDialog(null, "El producto de los primeros impares es: " +producto);
    }
}
