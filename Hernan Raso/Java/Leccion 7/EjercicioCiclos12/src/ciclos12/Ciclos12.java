/*
Ejercicio 12: Pedir un numero y calcular su factorial, hacerlo con las dos clases, Scanner y JOptionPane
*/
package ciclos12;

import javax.swing.JOptionPane;


public class Ciclos12 {
    public static void main(String[] args) {
        //Scanner entrada = new Scanner(System.in);
        long factorial = 1;
        //System.out.println("Ingrese un numero: ")
        int numero = Integer.parseInt(JOptionPane.showInputDialog("Ingrese un  numero: "));
        for(int i=1; i<=numero;i++) {
            factorial *= i;
        }
        //System.out.println("\nEl factorialdel numero ingresado es: "+factorial);
        JOptionPane.showMessageDialog(null,"El factorial del numero ingresado es: "+factorial);
    }
            
}

