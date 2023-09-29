//Tienda de libros
package Ejercicio1;

import java.util.Scanner;

public class Ejercicio1 {
    public static void main(String[] args) {
        Scanner entrada = new Scanner(System.in);
        System.out.println("Digite el nombre del libro: ");
        String nombreLibro = entrada.nextLine();
        System.out.println("Digite el id del libro: ");
        int idLibro = Integer.parseInt(entrada.nextLine());
        System.out.println("Ingrese el precio del libro: ");
        Double precioLibro = Double.parseDouble(entrada.nextLine());
        System.out.println("¿El envio es gratuito?");
        boolean envioGratuito = Boolean.parseBoolean(entrada.nextLine());
        
        System.out.println(nombreLibro+" #"+idLibro);
        System.out.println("Precio: $"+precioLibro);
        System.out.println("El envio del libro es gratuito: "+envioGratuito);
    }
}
