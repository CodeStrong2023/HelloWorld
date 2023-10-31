package ejercicio.pkg7;

import java.util.Scanner;

public class Ejercicio7 {

    public static void main(String[] args) {
        Scanner entrada = new Scanner(System.in);
        float salarioMen, Comision, Comision2, CarroP, Porcentaje, Total;
                
        salarioMen = 1000;
        System.out.println("Salario mensual: "+salarioMen+"$");
        System.out.println("Ingrese la cantidad de autos vendidos: ");
        Comision = Float.parseFloat(entrada.nextLine());
        Comision2 = 150*Comision;
        System.out.println("Comisión por autos vendidos: " + Comision2+"$");
        System.out.println("Ingrese el precio de un auto: ");
        CarroP = Integer.parseInt(entrada.nextLine());
        Porcentaje = CarroP * 0.05f;
        System.out.println("Porcentaje auto= " + Porcentaje);
        
        Total = salarioMen + Comision2 + Porcentaje;
        System.out.println("El salario mensual es: " + Total);
    }

}
