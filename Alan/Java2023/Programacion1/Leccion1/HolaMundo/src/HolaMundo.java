
import java.util.Scanner;

public class HolaMundo {

    public static void main(String[] args) {
        //para comentar una linea(//), para comentar muchas(/* al principio,*/ al final)
        /*System.out.println("Hola Mundo desde java");
        
        int miVariable = 10;
        System.out.println(miVariable);
        miVariable = 5;
        System.out.println(miVariable);
        //Tipo String
        String miVariableCadena = "bienvenidos";
        System.out.println(miVariableCadena);
        miVariableCadena = "sigamos creciendo en programacion";
        System.out.println(miVariableCadena);
         

        //Var - Inferencia de tipos java
        var miVariableEntera2 = 10;
        var miVariableCadena2 = "Seguimos estudiando";
        System.out.println("miVariableEntera2 = " + miVariableEntera2);
        System.out.println("miVariableCadena2 = " + miVariableCadena2);
        //soutv + tab

        var usuario = "osvaldo";
        var titulo = "ingeniero";
        var union = titulo + " " + usuario;
        System.out.println("union = " + union);
        
        var a = 8;
        var b = 4;
        System.out.println(usuario+(a+b));

        //ejercicio: Caracteres especiales con Java
        var nombre = "natalia";
        System.out.println("Nueva linea: \n" + nombre); //diagonal inversa y letra n = salto de linea
        System.out.println("tabulador \t" + nombre); //diagonal inversa y letra t = salto con tabulador
        System.out.println("\t .:Menu:.");
        System.out.println("Retroceso: \b\b"+nombre); //diagonal inversa y letra b = borra el caracter anterior
        System.out.println("comillas simples: \'"+nombre+"\'"); //diagonal inversa y '= 'palabra'
        System.out.println("comillas dobles: \""+nombre+"\""); ////diagonal inversa y " = "palabra" 

        //Clase Scanner
        Scanner entrada = new Scanner (System. in);
        System.out.println("digite su nombre: ");
        var usuario2 = entrada.nextLine();
        System.out.println("usuario2 = " + usuario2);
        System.out.println("Escriba el Profeción: ");
        var titulo2 = entrada.nextLine();
        System.out.println("resultado: "+titulo2+" "+usuario2);
        

        byte numEnteroByte = 127;
        System.out.println("numEnteroByte = "+ numEnteroByte);
        System.out.println("Valor minimo del byte: "+ Byte.MIN_VALUE);
        System.out.println("Valor maximo del byte: "+ Byte.MAX_VALUE);
        
        short numEnteroShort = 32767;
        System.out.println("numEnteroShort = "+ numEnteroShort);
        System.out.println("Valor minimo del short: "+ Short.MIN_VALUE);
        System.out.println("Valor maximo del short: "+ Short.MAX_VALUE);
        
        int numEnteroInt = 2147483647;
        System.out.println("numEnteroInt = "+ numEnteroInt);
        System.out.println("Valor minimo del int: "+ Integer.MIN_VALUE);
        System.out.println("Valor maximo del int: "+ Integer.MAX_VALUE);
        
        long numEnteroLong = 9223372036854775807L;
        System.out.println("numEnteroLong = "+ numEnteroLong);
        System.out.println("Valor minimo del long: "+ Long.MIN_VALUE);
        System.out.println("Valor maximo del long: "+ Long.MAX_VALUE);
        
        float numFloat = 3.4028235E38F;
        System.out.println("numFloat = "+ numFloat);
        System.out.println("Valor minimo del float: "+ Float.MIN_VALUE);
        System.out.println("Valor maximo del float: "+ Float.MAX_VALUE);
        
        double numDouble = 1.7976931348623157E308D;
        System.out.println("numDouble = "+ numDouble);
        System.out.println("Valor minimo del double: "+ Double.MIN_VALUE);
        System.out.println("Valor maximo del double: "+ Double.MAX_VALUE);
        
        //inferencia de tipos var y tipos primitivos
        var numEntero = 20;
        System.out.println("numEntero = " + numEntero);
        var numFloat = 10.0F;
        System.out.println("numFloat = " + numFloat);
        var numDouble = 10.0;
        System.out.println("numDouble = " + numDouble);
        
        
        //tipos primitivos char
        char miVariableChar = 'a';
        System.out.println("miVariableChar = " + miVariableChar);
        
        char varCaracter = '\u0024';//indicamos a java la asignacion con el codigo unicode
        System.out.println("miVariableChar = " + varCaracter);
        char varCaracterDecimal = 36;//valor decimal del juego de carateres unicode
        System.out.println("varCaracterDecimal = " + varCaracterDecimal);
        char varCaracterSimbolo = '$';//un caracter especial, podemos copiar y pegar desde unicode
        System.out.println("varCaracterSimbolo = " + varCaracterSimbolo);
        
        var varCaracter1 = '\u0024';
        System.out.println("miVariableChar = " + varCaracter1);
        var varCaracterDecimal1 = 36;
        System.out.println("varCaracterDecimal = " + varCaracterDecimal1);
        var varCaracterSimbolo1 = '$';
        System.out.println("varCaracterSimbolo = " + varCaracterSimbolo1);
        
        int varEnteroChar = '$';
        System.out.println("varEnteroChar = " + varEnteroChar);
        int CaracterChar = 'b';
        System.out.println("CaracterChar = " + CaracterChar);
        
        
        //tipos primitivos tipos booleanos
        boolean varBool = true;
        System.out.println("varBool = " + varBool);
        
        if(varBool){
        System.out.println("la bandera es verde");
        }
        else{
            System.out.println("la bandera es roja");
        }
        
        //algoritmo: ¿es mayor de edad?
        var edad = 20;
        //var mayor = edad >= 18;
        if(edad >=18){
            System.out.println("es mayor de edad");
        }
        else{
            System.out.println("es menor de edad");
        }
        
        //conversion de tipos primitivos
        var edad = Integer.parseInt("20");
        System.out.println("edad = " + (edad + 1));
        var valorPI = Double.parseDouble("3.1416");
        System.out.println("valorPI = " + valorPI);
        
        //pedir un valor 
        var entrada = new Scanner(System.in);
        System.out.println("Digite su edad");
        edad = Integer.parseInt(entrada.nextLine());
        System.out.println("edad = " + edad);
        
        
        //conversion de tipos primitivos en java parte 2
        var edadTexto = String.valueOf(10);
        System.out.println("edadTexto = " + edadTexto);
        
        var fraseChar = "programadores".charAt(12);
        System.out.println("fraseChar = " + fraseChar);
        
        var entrada = new Scanner(System.in);
        System.out.println("digite un caracter: ");
        fraseChar = entrada.nextLine().charAt(0);
        System.out.println("fraseChar = " + fraseChar);
        */
    }
}
