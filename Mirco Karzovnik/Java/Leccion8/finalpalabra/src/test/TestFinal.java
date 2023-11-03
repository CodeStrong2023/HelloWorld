
package test;
import domain.Persona;
public class TestFinal {
    public static void main(String[] args) {
        final int miDni = 41004708;
        System.out.println("miDni = " + miDni);

        System.out.println("mi atributo constante es = "+ Persona.CONSTANTE_AQUI);

        final Persona persona1 = new Persona();

        persona1.setNombre("Mirco");
        System.out.println("persona1 nombre: "+persona1.getNombre());
        persona1.setNombre("Elian");
        System.out.println("persona1 nombre: "+persona1.getNombre());
    }
    
}
