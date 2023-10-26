
package ciclos11;

import javax.swing.JOptionPane;


public class Ciclos11 {
    public static void main(String[] args) {
        long producto = 1;
        
        for(int i = 1; i<=20;i+=2){//el aumento apunta a solo ir por los impares
            producto *=i;
        }
        JOptionPane.showInputDialog(null, "El producto de numero impares es: "+ producto);
    }
}
