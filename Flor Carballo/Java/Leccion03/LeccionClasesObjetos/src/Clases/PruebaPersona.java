
package Clases;

public class PruebaPersona {
    public static void main(String[] args) {
        Persona persona1;
        persona1 = new Persona();
        persona1.nombre= "Flor";
        persona1.apellido = "Carballo";
        persona1.obtenerInformacion();
        
        Persona persona2 = new Persona();
        System.out.println("persona2 = "+ persona2);
        System.out.println("persona1 = "+ persona1);
        persona2.obtenerInformacion();
        persona2.nombre = "Rufina";
        persona2.apellido = "Carballo";
        persona2.obtenerInformacion();
    }
}
