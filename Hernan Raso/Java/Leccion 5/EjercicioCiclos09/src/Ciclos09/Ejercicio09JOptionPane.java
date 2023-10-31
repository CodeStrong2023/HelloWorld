/*
Ejercicio 9: Pedir el dia, mes y año der una fecha e indicar sila fecha es correcta. Suponiendo que todos los meses son de 30 dias.
*/
package Ciclos09;

import javax.swing.JOptionPane;


public class Ejercicio09JOptionPane {
    public static void main(String[] args) {
        
        int dia = Integer.parseInt(JOptionPane.showInputDialog("Ingrese el dia: "));
      
        int mes = Integer.parseInt(JOptionPane.showInputDialog("Ingrese el mes: "));
       
        int anio = Integer.parseInt(JOptionPane.showInputDialog("Ingrese el año: "));
        if((dia != 0)&&(dia <= 30)){
            if ((mes != 0)&&(mes <= 12)){
                if((anio != 0)&&(anio <= 2023)){
                    JOptionPane.showMessageDialog(null, "La fecha ingresada es: " + dia +"/"+mes+"/"+anio);
                }
                else{
                    JOptionPane.showMessageDialog(null, "Fecha incorrecta, anio imcorrecto");
                }
            }
            else{
                JOptionPane.showMessageDialog(null, "Fecha incorrecta, mes incorrecto");      
            }
        }
        else{
            JOptionPane.showMessageDialog(null, "Fecha incorrecta, dia incorrecto");
        } 
    } 
}
    

