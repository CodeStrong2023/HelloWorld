package Ciclos06;
import java.util.Scanner;
import javax.swing.JOptionPane;
public class Ciclos06 {

    public static void main(String[] args) {
        Scanner entrada = new Scanner(System.in);
        int num, suma = 0;

//        do {
//            System.out.println("Ingrese un numero, si desea salir ingrese 0.");
//            num = Integer.parseInt(entrada.nextLine());
//            suma += num;
//        }while(num != 0);
//        System.out.println("La suma es: "+suma);

        do{
            num = Integer.parseInt(JOptionPane.showInputDialog("Ingrese un numero: "));
            suma+= num;
        }while(num != 0);
        JOptionPane.showMessageDialog(null, "La suma de los numero es: "+ suma);
    }
}
