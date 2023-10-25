
package Operaciones;


public class Aritmetica {
    //atributos de la clase
    int a;
    int b;
    
    //El constructor es un metodo especial
    public Aritmetica(){ //Constructor 1
        System.out.println("Se esta ejecutando este constructor numero uno");
    }
    
    //Estamos viendo lo que se llama sobrecarga de constructores
    public Aritmetica(int a, int b){ //Constructor 2
        this.a = a;
        this.b = b;
        System.out.println("Se esta ejecutando este constructor numero dos");
    }
    
    //metodo
    public void sumarNumeros(){ //void = vacio
        int resultado = a + b;
        System.out.println("resultado = " + resultado);
    }
    
    public int sumarConRetorno(){
        //int resultado = a + b;
        return a + b;
    }
    
    public int sumarConArgumentos(int arg1, int arg2){
        this.a = arg1;//el argumento a se asigna al atributo this.a (no es necesario usarlo en este caso)
        this.b = arg2;
        //return a + b;
        return sumarConRetorno();
    }
}
