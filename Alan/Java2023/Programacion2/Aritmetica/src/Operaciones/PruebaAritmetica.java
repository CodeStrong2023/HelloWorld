
package Operaciones;


public class PruebaAritmetica {
    public static void main(String[] args) {
        var a = 10;//variables locales
        int b = 7;//memoria stack
        miMetodo();//llamamos el metodo nuevo
        
        Aritmetica aritmetica1 = new Aritmetica();
        aritmetica1.a = 3;
        aritmetica1.b = 7;
        aritmetica1.sumarNumeros();
        
        //para almacenar un objeto o los atributos se utiliza la memoria heap
        int resultado = aritmetica1.sumarConRetorno();
        System.out.println("resultado = " + resultado);
        
        resultado = aritmetica1.sumarConArgumentos(12,26);
        System.out.println("El resultado usando argumentos = "+ resultado);
        
        System.out.println("aritmetica1 a: "+aritmetica1.a);
        System.out.println("aritmetica1 b: "+aritmetica1.b);
        
        Aritmetica aritmetica2 = new Aritmetica(5,8);
        System.out.println("aritmetica2 = " + aritmetica2.a);
        System.out.println("aritmetica2 = " + aritmetica2.b);
        //aritemetica1 = null; nunca utilizar, no se debe hacer
        //System.gc(); metodo para limpiar residuos, es pesado, no utilizar
    }
    
    public static void miMetodo(){
        //a = 10;
        System.out.println("Aqui hay otro metodo");
    }
}
