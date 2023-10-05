
package Operaciones;

public class PruebaAritmetica1 {
    public static void main(String[] args) {
        int a = 10; //Variables locales
        int b = 7; //Memoria Stack
        miMetodo(); //Llamamos el método nuevo
        Aritmeticas aritmeticas1 = new Aritmeticas();
        aritmeticas1.a = 3;
        aritmeticas1.b = 7;
        aritmeticas1.sumarNumeros();
        //Para almacenar un objeto o los atributos se utiliza la memoria heap
        int resultado = aritmeticas1.sumarConRetorno();
        System.out.println("resultado = " + resultado);
        
        resultado = aritmeticas1.sumarConArgumentos(12, 26);
        System.out.println("Resultado usando argumentos = "+resultado);
        
        System.out.println("aritmeticas1 a: "+aritmeticas1.a);
        System.out.println("aritmeticas1 b: "+aritmeticas1.b);
        
        Aritmeticas aritmeticas2 = new Aritmeticas(5, 8);
        System.out.println("aritmeticas2 = "+ aritmeticas2.a);
        System.out.println("aritmeticas2 = "+ aritmeticas2.b);
        //aritmeticas1= null; nunca utilizar esto, no se debe de hacer
        //System.gc(); método para limpiar residuos, es pesado, no utilizar
        Persona persona = new Persona("Flor", "Carballo");
        System.out.println("persona = " + persona);
        System.out.println("Persona nombre: "+persona.nombre);
        System.out.println("Persona apellido: "+persona.apellido);
    }   
    
    public static void miMetodo(){
        // a = 10; //Una variable esta limitada
        System.out.println("Aquí hay otro método");
    }
}
//Creamos una nueva clase
class Persona{
    String nombre;
    String apellido;
    
    Persona(String nombre, String apellido){ //Constructor
        super(); //Llamada al constructor de la clase Padre object
        //Imprimir imprimir = new Imprimir();
        new Imprimir().imprimir(this);
        this.nombre = nombre;
        this.apellido = apellido;
        System.out.println("Objeto persona usando this: "+this);
    }
}
class Imprimir{
    public Imprimir(){
        super(); //el constructor de la clase padre, para reservar la memoria
    }
    public void imprimir(Persona persona){
        System.out.println("Persona desde la clase imprimir: "+persona);
        System.out.println("Impresión del objeto actual (this): "+this);
    }
}


