
package caja;


public class Caja {
    //atributos y caracteristicas
    int ancho;
    int alto;
    int profundo;
    //metodos y constructores(acciones)
    
    public Caja() {//constructor 1 = vacio       
    }
    
    //constructor con parametros
    public Caja(int ancho, int alto, int profundo) { //Constructor 2
        this.ancho = ancho;
        this.alto = alto;
        this.profundo = profundo;
    }
    
    public int calcularVolumen() {//Metodo que calcula
        return ancho * alto * profundo;
    }
}
