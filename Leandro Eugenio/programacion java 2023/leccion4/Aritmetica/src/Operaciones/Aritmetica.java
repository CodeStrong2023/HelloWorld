
package Operaciones;

public class Aritmetica {
    //Atributos de la clase
    int a;
    int b;
    
    //Metodo
    public void sumarNumeros(){
        int resultado = a + b;
        System.out.println("el resultado es = " + resultado);
    }
    
    public int sumarConRetorno(){
        //int resultado = a + b;
        return this.a + this.b;
    }
    
    public int sumarConArgumentos(int arg1,int arg2){
        this.a = a;//El argumento a se adigna al atributo this.a
        this.b = b;
        // return a + b;
        return sumarConRetorno();
    
    }
}
