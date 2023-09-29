
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
        //Para almacenar un objeto o los atributos se utiliza
        
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
        //System.gc();
        Persona persona = new Persona("Leandro","Eugenio");
        System.out.println("persona = " + persona);
        System.out.println("persona nombre = "+persona.nombre);
        System.out.println("persona apellido = "+persona.apellido);
    }
    //Modularidad creamos un nuevo metodo
    public static void miMetodo(){
        //int a = 10;//una variable esta lñimitada
        System.out.println("Aqui hay otro metodo");
    }
}
//Creamos una nueva clase
class Persona{
    String nombre;
    String apellido;
    
    Persona(String nombre, String apellido){ //constructo
        //super(); //Llamada al constructor de la clase Padre Object
        //Imprimir imprimir = new Imprimir();
        new Imprimir().imprimir(this);
        this.nombre = nombre;
        this.apellido = apellido;
        System.out.println("Objeto persona usando this: "+this);
    }
}
class Imprimir{
    public Imprimir(){
        super(); //EL constructor de la clase padre
    }
    public void imprimir(Persona persona){
        System.out.println("Persona desde la clase imprimir: "+persona);
        System.out.println("Impresion del objeto actual (this): "+ this);
    }
}
