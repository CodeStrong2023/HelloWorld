package Clases;

public class PruebaPersona {
    public static void main(String[] args) {
        Persona persona1;
        persona1 = new Persona();//Llamamos al contructor
        persona1.nombre = "Leandro";
        persona1.apellido = "Eugenio";
        persona1.ObtenerInformacion();
        
        Persona persona2 = new Persona();
        System.out.println("persona2 = " + persona2);
        System.out.println("persona1 = " + persona1);
        persona2.ObtenerInformacion();
        persona2.nombre = "Ezequiel";
        persona2.apellido = "Eugenio";
        persona2.ObtenerInformacion();
        
        
    }
}
