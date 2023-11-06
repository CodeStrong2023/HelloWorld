
package dominio;


public class Persona {
    //Atributos
    private String nommbre;
    private double sueldo;
    private boolean eliminado;
    
    //Constructor
    public Persona(String nombre, double sueldo, boolean eliminado){
        this.nommbre = nombre;
        this.sueldo = sueldo;
        this.eliminado = eliminado;
        
    }

    public String getNommbre() {
        return nommbre;
    }

    public void setNommbre(String nommbre) {
        this.nommbre = nommbre;
    }

    public double getSueldo() {
        return sueldo;
    }

    public void setSueldo(double sueldo) {
        this.sueldo = sueldo;
    }

    public boolean isEliminado() {
        return eliminado;
    }

    public void setEliminado(boolean eliminado) {
        this.eliminado = eliminado;
    }
    
   public String toString(){
       return "Persona [ nombre: "+this.nommbre+
               ",sueldo: "+this.sueldo+
               ", eliminado: "+this.eliminado+"]";
   
   }
   
    
}
