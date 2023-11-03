
package operaciones;
public class PruebaAritmetica {
    public static void main(String[] args) {
        var a = 10;
        int b = 7;
        miMetodo();
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

        Persona persona = new Persona("Leandro","Eugenio");
        System.out.println("persona = " + persona);
        System.out.println("persona nombre = "+persona.nombre);
        System.out.println("persona apellido = "+persona.apellido);
    }
    //Creamos un nuevo metodo
    public static void miMetodo(){
        //int a = 10;//una variable esta limitada
        System.out.println("Aqui hay otro metodo");
    }
}
//Nueva clase
class Persona{
    String nombre;
    String apellido;
    Persona(String nombre, String apellido){

        new Imprimir().imprimir(this);
        this.nombre = nombre;
        this.apellido = apellido;
        System.out.println("Objeto persona usando this: "+this);
    }
}
class Imprimir{
    public Imprimir(){
        super();
    }
    public void imprimir(Persona persona){
        System.out.println("Persona desde la clase imprimir: "+persona);
        System.out.println("Impresion del objeto actual (this): "+ this);
    }
}
