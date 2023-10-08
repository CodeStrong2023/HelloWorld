
package Leccion2;

import java.util.Scanner;

public class Leccion2 {
    public static void main(String[] args) {
//        var condicion = true;
//        if (condicion){
//            System.out.println("Condicion verdadera");//condicional simple
//        }
//        else{
//            System.out.println("Condicion falsa");//condicional doble 
//        }
//        
//        
//        var numero = 2;
//        var numeroTexto = "Numero desconocido";
//        if (numero == 1){
//            numeroTexto = "Numero uno";
//        }
//        else if (numero == 2){
//            numeroTexto = "Numero dos";
//        }
//        else if (numero == 3){
//            numeroTexto = "Numero tres";
//        }
//        else if (numero == 4){
//            numeroTexto = "Numero cuatro";
//        }
//        else{
//            numeroTexto = "Numero no encontrado";
//        }
//        System.out.println("El numero es: "+numeroTexto);  

//Switch
    Scanner entrada = new Scanner(System.in);
        System.out.println("Ingrese un numero");
    var numero = Integer.parseInt(entrada.nextLine());
    var numerotexto = "valor desconocido";
    switch (numero){
        case 1:
            numerotexto = "Numero uno";
            break;
        case 2:
            numerotexto = "Numero dos";
            break;
        case 3:
            numerotexto = "Numero tres";
            break;
        case 4:
            numerotexto = "Numero cuatro";
            break;
        default:
            numerotexto = "Caso no encontrado";
    }
        System.out.println("Numero texto = " + numerotexto);
    }
}
