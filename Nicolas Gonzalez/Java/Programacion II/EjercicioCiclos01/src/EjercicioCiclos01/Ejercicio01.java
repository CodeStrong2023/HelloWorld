package EjercicioCiclos01;

import javax.swing.JOptionPane;

public class Ejercicio01 {

    public static void main(String[] args) {

        System.out.println("Ingrese un numero para mostrar su cuadrado: ");
        Integer num = Integer.parseInt(JOptionPane.showInputDialog("Digite un numero: "));
        Integer resultado;

        while (num >= 0) {
            resultado = (int) Math.pow(num, 2);
            System.out.println("El numero " + num + " elevado al cuadrado es: " + resultado);
            num = Integer.parseInt(JOptionPane.showInputDialog("Digite un numero: "));
        }

    }
}
