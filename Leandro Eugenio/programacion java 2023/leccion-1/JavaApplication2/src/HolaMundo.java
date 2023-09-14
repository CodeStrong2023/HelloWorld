
import java.util.Scanner;


public class HolaMundo {
    public static void main(String[] args) {
        System.out.println("hola mundo desde java");
        
        
        int miVariable = 10;
        System.out.println(miVariable);
        miVariable = 5;
        System.out.println(miVariable);
        
        //Tipo String
        /* String miVariableCadena="bienvenidos";
        System.out.println(miVariableCadena);
        miVariableCadena="sigamos creciendo en programacion";
        System.out.println(miVariableCadena);
        */
        
        //var - inferencia en tipos en Java
        
        var miVariableEntera2 = 10;
        var miVariableCadena2 = "seguimos estudiando";
        System.out.println("mi variable entera 2 = " + miVariableEntera2);
        System.out.println("mi variable cadena 2 = " + miVariableCadena2);
        
        var usuario = "Leandro";
        var titulo = "tecnico";
        var union = titulo +" "+ usuario;
        System.out.println("union =" +union);
        
        //ordenar el codigo=click derecho format
        
        var a = 8;
        var b = 4;
        System.out.println(usuario + (a + b));
        
        //Ejercicio caracteres especiales con Java
        var nombre= "Natalia";
        System.out.println("Nueva linea: \n"+nombre);//salto de linea
        System.out.println("Tabulador: \t"+ nombre);//tabulador
        System.out.println("\t\t. :MENU:.");
        System.out.println("Retroceso: \b\b"+nombre);//Caracter de retroceso
        System.out.println("Comillas simples: \'"+nombre+"\'");
        System.out.println("Comillas dobles: \""+nombre+"\"");
        
        //Clase Scanner
        Scanner entrada = new Scanner(System.in);
        System.out.println("digite su nombre");
        var usuario2= entrada.nextLine();
        System.out.println("usuario2 =" + usuario2);
        System.out.println("escriba el titulo 2");
        var titulo2 = entrada.nextLine();
        System.out.println("Titulo 2 = "+titulo2+" "+usuario2);
        
        
        
        
        
    }
}
