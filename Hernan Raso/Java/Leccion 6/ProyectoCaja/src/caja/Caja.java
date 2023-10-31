
package caja; //Package


public class Caja { //Clase publica caja
    //Atributos (Caracteristicas)
    int ancho;
    int alto;
    int profundo;
    //Metodos y constructores (acciones)
    public Caja(){ //Constructor 1 = Vacio
       
    }
    //Constructor con parametros
    public Caja(int ancho, int alto, int profundo) { //Constructor 2
       this.ancho = ancho;
       this.alto = alto;
       this.profundo = profundo;
       
    }
    
    public int calcularVolumen() { //Metodo para calcular
        return ancho * alto * profundo;
    }
    
}
