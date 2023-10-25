package ejercicio1;

import java.util.Scanner;

public class Ejercicio1 {

    public static void main(String[] args) {
        Scanner entrada = new Scanner(System.in);
        System.out.println("Digite el mes del anio");
        var mes = Integer.parseInt(entrada.nextLine());
        var estacion = "estacion desconocida.";

        if (mes == 1 || mes == 2 || mes == 3) {
            estacion = "verano";
        } else if (mes == 4 || mes == 5 || mes == 6) {
            estacion = "otonio";
        } else if (mes == 7 || mes == 8 || mes == 9) {
            estacion = "invierno";
        } else if (mes == 10 || mes == 11 || mes == 12){
            estacion = "primavera";
        }
        System.out.println("estacion = " + estacion);
    }

}
