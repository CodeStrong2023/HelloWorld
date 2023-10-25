
package CicloWhile;

public class CicloWhile {
    public static void main(String[] args) {
        //While = ciclo mientras hacer
        var conteo = 0; //inferencia de tipos
        while(conteo <=7){
            System.out.println("conteo = " + conteo);
            conteo++; //aumenta en 1 la variable
        }
        System.out.println("-------------------------");
        
        //Do While = ciclo repetir hasta que
        var contador = 0;
        do{
            System.out.println("contador = " + contador);
            contador++;
        }while (contador <=7);
        System.out.println("-----------------------------------");
        
        //For = ciclo para
        for (var contando = 0; contando < 7; contando++){
            System.out.println("contando = " + contando);
        }
        
        
    }
}
