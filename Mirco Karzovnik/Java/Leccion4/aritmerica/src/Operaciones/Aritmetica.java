
package Operaciones;
public class Aritmetica {
    //Atributos
    int a;
    int b;
    public Aritmetica(){
            System.out.println("Se ejecuta el constructor N1");
    }
    //sobrecarga de constructores
    public Aritmetica(int a, int b){
        this.a = a;
        this.b = b;
        System.out.println("Se esta ejecutando el construcir N2");
    }

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
