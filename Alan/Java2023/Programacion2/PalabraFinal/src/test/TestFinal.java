
//Uso de la palabra final
//Esta palabra tiene diferentes dignificados dependiendo donde se aplique:
//
//variables: evita cambiar el valor que almacena la variable
//metodos: evita que se modifique la definicion o el comportamiento de un metodo de una subclase (hija)
//clases: evita que se creen clases hijas
//
//otra caracteristica es que normalmente, cuando trabajamos con variables se combinan con el modificador de acceso
//estatico para convertir una variable en una constante, es decir que no se puede modificar su valor,
//el ejemplo de esto es la clase Math en la cual todos sus atributos son de tipo static al final, es por esto que la
//variable pi* se conoce como una constante.

package test;

import domain.Persona;

public class TestFinal {
    public static void main(String[] args) {
        final int miDni = 44662275;
        System.out.println("miDni = " + miDni);
        //miDni = 45692436; no se puede modificar porque es final
        //Persona.CONSTANTE_AQUI = 9;//no se modifica porque es final
        System.out.println("mi atributo constante es: " + Persona.CONSTANTE_AQUI);
        
        final Persona persona1 = new Persona();
        //persona1 = new Persona();//no se puede modificar porque es final
        persona1.setNombre("Ariel Betancud");
        System.out.println("persona1 nombre: "+persona1.getNombre());
        persona1.setNombre("Liliana");
        System.out.println("persona1 nombre: "+persona1.getNombre());
    }
}
