
package Ciclos09;

import java.util.Scanner;

/*
Ejercicio 9: Pedir el dia, mes y año der una fecha e indicar sila fecha es correcta. Suponiendo que todos los meses son de 30 dias.
*/
public class Ciclos09 {
    public static void main(String[] args) {
        Scanner entrada = new Scanner(System.in);
                System.out.println("Ingrese el dia: ");
        int dia = Integer.parseInt(entrada.nextLine());
        System.out.println("Ingrese el mes: ");
        int mes = Integer.parseInt(entrada.nextLine());
        System.out.println("Ingrese el año: ");
        int anio = Integer.parseInt(entrada.nextLine());
        if((dia != 0)&&(dia <= 30)){
            if ((mes != 0)&&(mes <= 12)){
                if((anio != 0)&&(anio <= 2023)){
                    System.out.println("La fecha ingresada es: " + dia +"/"+mes+"/"+anio);
                   
                }
                else{
                    System.out.println("Fecha incorrecta, anio imcorrecto");
                
                }
            }
            else{
                System.out.println("Fecha incorrecta, mes incorrecto");
                    
            }
        
        }
        else{
            System.out.println("Fecha incorrecta, dia incorrecto");
        }
        
        
    }
    
}
