
package ciclos_y_clases;

import javax.swing.JOptionPane;


public class EjercicioCiclos02ConOptionPane {
    public static void main(String[] args) {
        var numero = Integer.parseInt(JOptionPane.showInputDialog("Ingrese un numero: "));
        while(numero != 0){
            if(numero > 0){
                System.out.println("El numero " +numero + " es positivo");
            }
            else{
                System.out.println("EL numero "+numero + " es Negativo");
            }
            numero = Integer.parseInt(JOptionPane.showInputDialog("Ingrese otro numero: "));
        
        }
        System.out.println("El numero "+numero+ " Finaliza el programa");
    }
}