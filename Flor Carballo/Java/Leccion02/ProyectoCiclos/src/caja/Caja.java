
package caja;

public class Caja {
    //Atributos (características)
    int ancho;
    int alto;
    int profundo;
    //Métodos y constructores (acciones)
    public Caja() {
        
    }
    //Contructor con parámetros
    public Caja(int ancho, int alto, int profundo){
        this.ancho = ancho;
        this.alto = alto;
        this.profundo = profundo;
    }
    
    public int calcularVolumen(){ //Método para calcular
        return ancho * alto * profundo;
    }
}
