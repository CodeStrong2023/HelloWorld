
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
        
        int num1 = 5, num2 = 4;
        var solucion = num1 + num2;
        System.out.println("solucion de la suma = " + solucion );
        
        solucion = num1 - num2;
        System.out.println("solucion de la resta = " + solucion);
        
        solucion = num1 * num2;
        System.out.println("solucion de la multiplicacion = " + solucion);
        
        solucion = num1 / num2;
        System.out.println("solucion de la division = " + solucion);
        
        var solucion2 = 3.4 / num2;
        System.out.println("solucion2 resultado de la division = " + solucion2);
        
        solucion = num1 % num2; //guarda el residuo entero de la division
        System.out.println("solucion = " + solucion);
        
        if (num2 % 2 == 0)
            System.out.println("Es un numero par");
        else
            System.out.println("Es un numero impar");
        
        int varNum1 = 10, varNum2 = 40;
        int varNum3 = varNum1 + 6 - varNum2;
        System.out.println("varNum3 = " + varNum3);
        
        varNum1 += 1;
        System.out.println("varNum1 = " + varNum1);
        
        varNum1 -= 2;
        System.out.println("varNum1 = " + varNum1);
        
        varNum1 *= 5;
        System.out.println("varNum1 = " + varNum1);
        
        varNum1 /= 4;
        System.out.println("varNum1 = " + varNum1);
        
        varNum1 %= 6;
        System.out.println("varNum1 = " + varNum1);
        
        //Operadores unarios: Cambio de signo
        var varA = 7;
        var varB = -varA;
        System.out.println("varA = " + varA);
        System.out.println("varB = " + varB);//resultado negativo
        
        var varC = true;
        var varD = !varC;
        System.out.println("varC = " + varC);
        System.out.println("varD = " + varD);
        
        var varE = 9; //se va a modificar su valor
        var varF = ++varE; //simbolo antes de la variable
        //primero se incrementa la variable y despues se usa su valor
        System.out.println("varE = " + varE);
        System.out.println("varF = " + varF);//se suma uno
        
        //Postincremento (el simbolo va despues de la variable)
        var varG = 3;
        var varH = varG++;//primero el valor de la variable luego el incremento
        System.out.println("varG = " + varG);
        System.out.println("varH = " + varH);
        
        //operadores unarios de decremento: predecremento
        var varI = 4;
        var varJ = --varI;
        System.out.println("varI = " + varI);//la variable ya esta con decremento
        System.out.println("varJ = " + varJ);
        
        //postdecremento
        var varK = 8;
        var varL = varK--;
        System.out.println("varK = " + varK);// aqui decrementa en 1
        System.out.println("varL = " + varL);
        
        //operadores de igualdad relacionales
        var aNum = 5;
        var bNum = 4;
        var cNum = (aNum == bNum);
        System.out.println("cNum = " + cNum);
        
        var dNum = aNum != bNum;
        System.out.println("dNum = " + dNum);
        
        var cadenaA = "Hello";
        var cadenaB = "Hello";
        var cVar = cadenaA == cadenaB;
        System.out.println("cVar = " + cVar);
        
        var fVar = cadenaA.equals(cadenaB);
        System.out.println("fVar = " + fVar);
        
        var gVar = aNum >= bNum;// >=, <=, ==, !=
        System.out.println("gVar = " + gVar);
        
        if (aNum % 2 == 0){
            System.out.println("El numero es par");
        } else {
            System.out.println("El numero es impar");
        }
        
        var edad = 15;
        var adulto = 18;
        if (edad >= adulto){
            System.out.println("Es mayor de edad");
        } else {
            System.out.println("Es menor de edad");
        }       

        var valorA = 7;
        var valorMinimo = 0;
        var valorMaximo = 10;
        var respuesta = valorA >= 0 && valorA <= 10; //and= && esta condicion es falsa si uno de los dos es falso

        if (respuesta) {
            System.out.println("Esta dentro del rango establecido");
        } else {
            System.out.println("Esta fuera del rango establecido");
        }

        var vacaciones = false;
        var diaLibre = false;
        if (vacaciones || diaLibre) //or= || esta condicion es falsa si los 2 son falsos (vacaciones = false, diaLibre = false)
            System.out.println("Papá puede asistir al juego de su hijo");
        else
            System.out.println("Papá no puede asistir al juego de su hijo");
        
        //operador ternario
        var resultadoT = (5>4) ? "verdadero" : "falso";
        System.out.println("resultadoT = " + resultadoT);
        
        var numeroT = 7;
        resultadoT = (numeroT % 2 ==0) ? "es par" : "es impar";
        System.out.println("resultadoT = " + resultadoT);
        
        var x = 5;
        var y = 10;
        var z = ++x + y--; // se lee de izquierda a derecha, eso significa que el ++ de x no se aplica a la suma
        System.out.println("x = " + x);// 6
        System.out.println("y = " + y);// 9
        System.out.println("z = " + z);// 16
        
        var solucionAritmetica = 4 + 5 * 6 / 3;//4 + ((5 * 6) / 3) = 30 / 3 = 10 + 4 = 14
        System.out.println("solucionAritmetica = " + solucionAritmetica);
        
        solucionAritmetica = (4+5) * 6/3;//4+5 = 9 * 6 = 54 / 3 = 18
        System.out.println("solucionAritmetica = " + solucionAritmetica);
        
        //ejercicios: Area y Perimetro de un rectangulo.
        var Altura = 7;
        var Ancho = 12;
        var Perimetro = (2*Altura) + (2*Ancho);
        var Area = Altura*Ancho;
        System.out.println("Perimetro = " + Perimetro);
        System.out.println("Area = " + Area);
        
        //ejercicios: El mayor de dos números (Operador Ternario)
        int numUno = 10, numDos = 9;
        System.out.println("numero mayor: " + ((numUno>numDos)? "numUno es mayor": "numDos es mayor"));
        */
    }
}
