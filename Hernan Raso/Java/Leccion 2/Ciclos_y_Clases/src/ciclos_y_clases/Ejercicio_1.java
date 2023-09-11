/*
Ejercicio 1: Leer un numero y mostrar su cuadrado, repetir el procesos hasya que se introduzca un numero negativo
*/
package ciclos_y_clases;

import javax.swing.JOptionPane;

public class Ejercicio_1 {
    public static void main(String[] args) {
        int numero, cuadrado;
  
        numero = Integer.parseInt(JOptionPane.showInputDialog("Ingrese un numero: "));
        while(numero >= 0) {
            cuadrado = (int)Math.pow(numero, 2);
            System.out.println("El numero " +numero+ "elevado al cuadrado es: "+cuadrado);
            System.out.println("Ingrese otro numero: ");
            numero = Integer.parseInt(JOptionPane.showInputDialog("Ingrese otro numero: "));
            
        
        }
        System.out.println("El Programa a Finalizado por un numero Negativo");
    }
}
