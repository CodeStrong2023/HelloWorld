
package Operaciones;

public class PruebaAritmetica {
    public static void main(String[] args) {
        var a = 10;//variables locales
        int b = 7; //memoria stack
        miMetodo(); //LLAMAMOS AL METODO NUEVO
        Aritmetica aritmetica1 = new Aritmetica();
        aritmetica1.a = 3;
        aritmetica1.b = 7; 
        
        aritmetica1.sumarNumeros();
        
        int resultado = aritmetica1.sumarConRetorno();
        System.out.println("resultado = " + resultado);
        
       
        resultado = aritmetica1.sumarConArgumentos(a, b);
        System.out.println("resultado usando argumentos = " + resultado);
        
        System.out.println("artimetica1 a: +"+aritmetica1.a);
        System.out.println("artimetica1 a: +"+aritmetica1.b);
        
        Aritmetica aritmetica2 = new Aritmetica(5,8);
        System.out.println("aritmetica2 = " + aritmetica2.a);
        System.out.println("aritmetica2 = " + aritmetica2.b);
        //aritmetica1 = null //nunca utoilizar estok, no se debe hacer
        System.gc();
    }
    public static void miMetodo(){
        //int a = 10;//una variable esta lñimitada
        System.out.println("Aqui hay otro metodo");
    }
}
