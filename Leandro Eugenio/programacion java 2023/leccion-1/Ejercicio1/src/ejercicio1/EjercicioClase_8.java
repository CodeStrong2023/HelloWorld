
package ejercicio1;

import java.util.Scanner;


public class EjercicioClase_8 {
    public static void main(String[] args) {
        var scanner = new Scanner(System.in);
        
        //Ejercicio 1= sacar area y perimetro de un rectangulo
        
        System.out.println("a continuación digite la altura del rectangulo");
        var altura= scanner.nextInt();
        System.out.println("por favor ingrese el ancho del rectangulo");
        var ancho = scanner.nextInt();
        
        var perimetro = altura * 2 + ancho *2;
        System.out.println("perimetro = " + perimetro);
        
        var area = altura * ancho;
        System.out.println("area = " + area);
        
        //Ejercicio2=el mayor de dos numeros (Operador ternario)
        System.out.println("a continuacion ingrese el primer número");
        var num1 = scanner.nextInt();
        System.out.println("a continuacion ingrese el segundo numero");
        var num2 = scanner.nextInt();
        var mayor = (num1 > num2) ? num1 : num2;
        System.out.println("el mayor es : " + mayor);
        
        
        
        
    }
}
