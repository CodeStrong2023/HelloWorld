
package Ciclos09;

import java.util.Scanner;
import javax.swing.JOptionPane;

public class Ciclos09 {
    public static void main(String[] args) {
        Scanner entrada = new Scanner(System.in);
        int anio, mes, dia;
//        
//        System.out.println("Ingrese el dia: ");
//        dia = Integer.parseInt(entrada.nextLine());
//        System.out.println("Ingrese el mes: ");
//        mes = Integer.parseInt(entrada.nextLine());
//        System.out.println("Ingrese el año: ");
//        anio = Integer.parseInt(entrada.nextLine());
//        
//        if ((dia != 0)&&(dia <= 30)){
//            if ((mes != 0)&&(mes <=12)){
//                if ((anio !=0)&&(anio <=2023)){
//                    System.out.println("La fecha es: "+dia+"/"+mes+"/"+anio);
//                }
//                else{
//                    System.out.println("La fecha es incorrecta.");
//                }
//            }
//            else {
//                System.out.println("La fecha es incorrecta.");
//            }
//        }
//        else{
//            System.out.println("La fecha es incorrecta.");
//        }

        dia = Integer.parseInt(JOptionPane.showInputDialog("Ingrese el dia: "));
        mes = Integer.parseInt(JOptionPane.showInputDialog("Ingrese el mes: "));
        anio = Integer.parseInt(JOptionPane.showInputDialog("Ingrese el anio: "));
        
        if ((dia !=0)&&(dia <=30)){
            if ((mes !=0)&&(mes <= 12)){
                if ((anio !=0)&&(anio <= 2023)){
                    System.out.println("La fecha es: "+dia+"/"+mes+"/"+anio);
                }
                else{
                    System.out.println("La fecha es incorrecta");
                }
            }
            else{
                System.out.println("La fecha es incorrecta");
            }
        }
        else{
            System.out.println("La fecha es incorrecta");
        }       
    }
}
