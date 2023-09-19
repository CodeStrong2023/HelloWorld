
import java.util.Scanner;


public class TiposPrimitivos {
    public static void main(String[] args) {
        /*
        byte numeroEntero = 10;
        System.out.println("valor minimo del Byte" + Byte.MIN_VALUE );
        System.out.println("valor maximo del Byte" + Byte.MAX_VALUE );
        
        short numeroEnteroShort = 10;
        System.out.println("numeroEnteroShort : " + numeroEnteroShort);
        System.out.println("valor minimo del short :" + Short.MIN_VALUE);
        System.out.println("valor maximo del short :" + Short.MAX_VALUE);
        
        int numEnteroInt = 2147483647; //le ponemos la L cuando nos pasamos en el maximo de numeros
        System.out.println("valor del int: " + numEnteroInt );
        System.out.println("valor minimo del int: "+ Integer.MIN_VALUE);
        System.out.println("valor minimo del int: "+ Integer.MAX_VALUE);
        
        long numEnteroLong = 10;
        System.out.println("numEnteroLog :"+ numEnteroLong);
        System.out.println("numero minimo long: "+ Long.MIN_VALUE);
        System.out.println("numero maximo long: "+ Long.MAX_VALUE);
        
        */
        /*
        float numFloat = 10.0F;
        System.out.println("numFloat = " + numFloat);
        System.out.println("el valor minimo de float = " + Float.MIN_VALUE );
        System.out.println("el valor maximo de float = " + Float.MAX_VALUE);
        
        double numDouble = 10;
        System.out.println("numDouble = " + numDouble);
        System.out.println("el valor minimo de double es = " + Double.MIN_VALUE);
        System.out.println("el valor maximo de double es = " + Double.MAX_VALUE);
        */
        /*
        //inferencia de tipos var y datos primitivos
        var numEntero = 20; //loas lineas literalsi sin punto automaticamente son int
        System.out.println("numero = " + numEntero);
        var numFloat = 10.0F;//autoamticamente con el numero se transfdorma en un tipo double
        System.out.println("numFloat = "+numFloat);
        var numDouble = 10.0;
        System.out.println("numDouble = " + numDouble);
        */
        /*
        //tipos primitivos char
        char miVariableChar = 'a';
        
        System.out.println("char = " + miVariableChar);
        char varCaracter = '\u0024'; //Indicamos a Java la asignacion con le valor Unicode
        System.out.println("varCaracter = " + varCaracter);
        char caracterDecimal = 36; //valor decimal del juego de caracteres unicode
        System.out.println("caracter Decimal = " + caracterDecimal);  
        char CaracterSimbolo = '$'; //este seria directamente el caracter
        System.out.println("caracter Symbolo = " + CaracterSimbolo);
        
        
        var varCaracter1 = '\u0024'; //Indicamos a Java la asignacion con le valor Unicode
        System.out.println("varCaracter = " + varCaracter1);
        var caracterDecimal1 = (char)36; //valor decimal del juego de caracteres unicode
        System.out.println("caracter Decimal = " + caracterDecimal1);    
        var CaracterSimbolo1 = '$'; //este seria directamente el caracter
        System.out.println("caracter Symbolo = " + CaracterSimbolo1);
        
        var enteroChar = '$';
        System.out.println("Entero char =" + enteroChar);
        
        //conversion de tipos primitivos
        var edad = Integer.parseInt("20");
        System.out.println("edad = " + (edad + 1));
        var valorPI = Double.parseDouble("3.1416");
        System.out.println("valorPi = " + valorPI);
        
        //PEDIR UN VALOR
        var entrada = new Scanner(System.in);
        System.out.println("Digite su edad");
        edad = Integer.parseInt(entrada.nextLine());
        System.out.println("edad = " + edad);
        */
        
        //CONVERSION DE TIPOS PRIMITOVOS a STRING
        /*
        var edadTexto = String.valueOf(10);
        System.out.println("edadTexto = " + edadTexto);
        
        var fraseChar = "programadores".charAt(0);
        System.out.println("fraseChar = " + fraseChar);
        
        System.out.println("Digite un caracter : ");
        Scanner entrada = new Scanner(System.in);
        fraseChar = entrada.nextLine().charAt(0);
        */
        /*
        int num1 = 5, num2 = 4;
        var solucion = num1 + num2;
        System.out.println("solucion suma = " + solucion);
        
        solucion = num1 -num2 ;
        System.out.println("soliucion de resta = " + solucion);
        
        solucion = num1 * num2;
        System.out.println("solucion multipliacion = " + solucion);
        
        solucion = num1 / num2;
        System.out.println("solucion division = " + solucion);
        
        var solucion2 = 3.4D / num2;
        System.out.println("solucion2 resultado de la division = " + solucion);
        
        solucion = num1 % num2;
        System.out.println("solucion = " + solucion);
        
        if (num1 % 2 ==0)
            System.out.println("Es un numero Par");
        else
            System.out.println("Es un numero inPar");
       
        */
        
        int varNum1 =1, varNum2 = 4;
        int varNum3 = varNum1 + 6 - varNum2;
        System.out.println("varNum3 = " + varNum3);
        
        varNum1 += 1;
        System.out.println("varNum1 = " + varNum1);
        
        
        
        
        
    }
}
