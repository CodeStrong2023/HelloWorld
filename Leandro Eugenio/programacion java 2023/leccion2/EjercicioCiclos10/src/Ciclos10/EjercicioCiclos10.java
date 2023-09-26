/*
 Ejercicio 10 : Pedir 10 numeros y escrinir lña suma
 total
Hacerlo con la clase Scanner y JOptionPane
*/
package Ciclos10;

import javax.swing.JOptionPane;


public class EjercicioCiclos10 {
    public static void main(String[] args) {
        int numero,suma = 0;
        for (int i = 0; i <= 10; i++) {
            numero = Integer.parseInt(JOptionPane.showInputDialog("Digite un numero"));
            suma += numero;
        }
        JOptionPane.showMessageDialog(null,"\nla suma de todos los numeros es: "+suma);
    }
}
