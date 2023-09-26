
package Operaciones;

public class Aritmetica {
    //Atributos de la clase
    int a;
    int b;
    
    //el contructor es un metodo especial
    public Aritmetica(){ //Constructor 1
            System.out.println("Se esta ejecutando el constructor numero uno");
    }
    //Estamos viendo lo que se llama sobrecarga de constructores
    public Aritmetica(int a, int b){
        this.a = a;
        this.b = b;
        System.out.println("Se esta ejecutandoe el constructor numero dos");
    }
    
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
