
package Operaciones;

public class PruebaAritmetica {
    public static void main(String[] args) {
        Aritmetica aritmetica1 = new Aritmetica();
        aritmetica1.a = 3;
        aritmetica1.b = 7; 
        aritmetica1.sumarNumeros();
        
        int resultado = aritmetica1.sumarConRetorno();
        System.out.println("resultado = " + resultado);
        
        int a = 5;
        int b =10;
        resultado = aritmetica1.sumarConArgumentos(a, b);
        System.out.println("resultado usando argumentos = " + resultado);
        
        
            
    }
}
