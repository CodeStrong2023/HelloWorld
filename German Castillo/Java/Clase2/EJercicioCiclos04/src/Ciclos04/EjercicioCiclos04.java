/*
    Ejercicio 04: pedir numeros hasta que se teclee uno negativo,+
    y mostrar cuantos numeros se han introducido.
    Lo hacemos primero con clase Scanner
    Luego lo hacemos con la clase joption
*/
package Ciclos04;

import javax.swing.JOptionPane;

public class EjercicioCiclos04 {
    public static void main(String[] args) {
        int numero, conteo = 0;

        numero = Integer.parseInt(JOptionPane.showInputDialog("Digite un numero: "));
        while (numero >= 0) {
            JOptionPane.showMessageDialog(null, "el numero "+numero+" es POSITIVO");
            conteo ++;
            numero = Integer.parseInt(JOptionPane.showInputDialog("Digite otro numero: "));
        }
        JOptionPane.showMessageDialog(null, "a ingresado"+conteo+" numeros que no son negativos");
             
        
    }
}
