
public class clase_8 {
    public static void main(String[] args) {
        /* 
        int num1 = 5,num2 = 4;
        var solucion = num1 +num2 ;
        System.out.println("solucion de la suma = " + solucion);
        
        solucion = num1 - num2;
        System.out.println("solucion de la resta = " + solucion);
        
        solucion = num1 * num2;
        System.out.println("solucion de la multiplicacion = " + solucion);
        
        solucion = num1 / num2;
        System.out.println("solucion de la division = "+solucion);
        
        var solucion2 = 3.4 / num2;
        System.out.println("solucion2 resultado de la division = " + solucion2);
        
        solucion = num1 % num2;
        System.out.println("solucion del resto de entre la division de dos numeros = " + solucion);
        
        if (num1 % 2 == 0)
            System.out.println("Es un numero par");
        else
            System.out.println("Es un numero Inpar");
        
        */
        /*
        int varNum1 = 1, varNum2 = 4;
        int varNum3 = varNum1 + 6 - varNum1;
        System.out.println("varNum3 = " + varNum3);
        
        varNum1 +=1; //varNum1 = varNum1 + 1
        System.out.println("varNum1 = " + varNum1);
        
        varNum2 -= 2;
        System.out.println("varNum2 = " + varNum2);
        
        varNum1 *= 5;
        System.out.println("varNum1 = " + varNum1);
        
        varNum3 /= 4;
        System.out.println("varNum3 = " + varNum3);
        
        varNum1 %=6;
        System.out.println("varNum1 = " + varNum1);
        
        */
        /*
        //Operadores Unarios
        
        var varA = 7;
        var varB = -varA;
        System.out.println("varA = " + varA);
        System.out.println("varB =" + varB);
        
        //Operadores de negacion
        var varC = true;
        var varD = !varC;
        System.out.println("varC = " + varC);
        System.out.println("varD = " + varD);
        
        //Operadores unarios de incremento:Peincremento
        var varE = 9;//se va a modificar su valor
        var varF = ++varE; //simbolo antes de la variable
        //Primero se incrementa la variable y luego se usa su valor
        System.out.println("varE = " +varE);
        System.out.println("varF = "+ varF);
        
        //Postincremento (el simbolo va despues de la variable)
        var varG = 3;
        var varH = varG ++;
        System.out.println("varG = " + varG);
        System.out.println("varH = " + varH);
        
        //Operadores unarios de decremento
        var varI = 4;
        var varJ = --varI;
        System.out.println("varI = " + varI);
        System.out.println("varJ = " + varJ);
        
        //Postdecremento
        var varK = 9;
        var varL = varK--;
        System.out.println("varK = " + varK);
        System.out.println("varL = " + varL);
        
        */
        /*
        //Operadore de igualdad y relacionales
        var aNum = 5;
        var bNum = 4;
        var cNum =(aNum == bNum);
        System.out.println("cNum = " + cNum);
        
        var dNum = aNum != bNum;
        System.out.println("dNum = " + dNum);
        
        var cadenaA = "Hello";
        var cadenaB = "bye bye";
        var cVar = cadenaA == cadenaB;
        System.out.println("cVar = " + cVar);
        
        var fVar = cadenaA.equals(cadenaB);
        System.out.println("fVar = " + fVar);
        
        var gVar = aNum != bNum;
        System.out.println("gVar = " + gVar);
        
        if (aNum % 2 == 0){
            System.out.println("es numero Par");
        }else{ 
            System.out.println("es numero inPar");
        }
        
        var edad = 30;
        var adulto = 18;
        if (edad >= adulto){
            System.out.println("es mayor de edad");
        }else{
            System.out.println("es menor de edad");
        }
        }
        */
        /*
        var valorA = 7;
        var valorMinimo = 0;
        var valorMaximo = 10;
        var respuesta = valorA >= 0 && valorA >= 10;
        
        if(respuesta)
            System.out.println("esta dentro del rango contable");
        else
            System.out.println("esta fuera dle rango establecido");
        
        var vacaciones = false;
        var diaLibre = false;
        if(vacaciones)
            System.out.println("papa puede asistir al juego de su hijo");
        else
            System.out.println("papa no puede asistir al juego de su hijo");
        
        */
        /*
        //Operador ternario
        var resultadoT = (5>4) ? "verdadero" : "falso";
        
        
        var numeroT = 7;
        resultadoT = (numeroT % 2 == 0) ? "Es par" : "Es impar";
        
        */
        
        
        var x = 5;
        var y = 10;
        var z = ++x + y--;
        System.out.println("x = " + x);
        System.out.println("y = " + y);
        System.out.println("z = " + z);
        
        var solucionAritmetica = 4 + 5 * 6 / 3;
        System.out.println("solucionAritmetica = " + solucionAritmetica);
        
        solucionAritmetica = (4 + 5) * 6 / 3;
        System.out.println("solucion Aritmetica = " + solucionAritmetica);
        
        
        
        
    }
}
