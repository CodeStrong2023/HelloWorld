
package Operaciones;

public class Aritmeticas {
    //Atributos de la clase
    int a;
    int b;
    
    //El constructor es un método especial
    public Aritmeticas(){
            System.out.println("Se esta ejecutando este constructor número uno");
    }
    //Estamos viendo lo que se llama sobrecarga de constructores
    public Aritmeticas(int a, int b){
        this.a = a;
        this.b = b;
        System.out.println("Se esta ejecutando este constructor número dos");
        
    }
    //Metodo
    public void sumarNumeros(){
        int resultado = a + b;
        System.out.println("resultado = " + resultado);
    }
    
    public int sumarConRetorno(){
        //int resultado = a + b;
        return this.a + this.b; 
    }   
    public int sumarConArgumentos(int arg1, int arg2){
            this.a = a;
            this.b = b; 
            //return a + b;
            return this.sumarConRetorno();
            
        }
}
