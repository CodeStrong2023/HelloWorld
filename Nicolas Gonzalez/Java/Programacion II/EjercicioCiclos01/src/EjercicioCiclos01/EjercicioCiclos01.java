
package EjercicioCiclos01;

import java.util.Scanner;


public class EjercicioCiclos01 {
    public static void main(String[] args) {
        Scanner entrada = new Scanner(System.in);
        
        System.out.println("Ingrese un numero para mostrar su cuadrado: ");
        Integer num = Integer.parseInt(entrada.nextLine());
        Integer resultado;
        
        while (num >= 0) {
            resultado = (int)Math.pow(num, 2);
            System.out.println("El numero "+num+" elevado al cuadrado es: "+resultado);
            System.out.println("Digite otro numero: ");
            num = Integer.parseInt(entrada.nextLine());
        }
    }
}
