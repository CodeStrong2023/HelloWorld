/*
uso de la palabra final
Esta palabra tien diferentes significcado dependiendo de donde 
se aplique:
    varaibles:Evita cambiar el valor quie almacena la variable
    metodos: Evita que se modifique la defincion o el comportamiento
        de un metodo desde una subcla(hija)
    clases: Evita 3ue se creen clases hijas
Otra caracterisitca es que normalmente , cuando trabajamos con variables
se combina con el modificador de acceso estatico para convertir una
varable en constante, es decir que no se puede modificar su valor
el ejemplo de esrto es la clase Math en la cual todos sus atributos
son de tio static y final, es por esotr que la variable pi* se conoce
como una constante
*/
package test;

import domain.Persona;

public class TestFinal {
    public static void main(String[] args) {
        final int miDni = 41004708;
        System.out.println("miDni = " + miDni);
        //miDni = 41005708; no0 se puede modificar
        //Persona.CONSTANTE_AQUI = 9 ; //no se puede  
        System.out.println("mi atributo constante es = "+ Persona.CONSTANTE_AQUI);
        
        final Persona persona1 = new Persona();
        //persona1 = new Persona();//no se puede asignar una nueva referencia
        persona1.setNombre("Leandro");
        System.out.println("persona1 nombre: "+persona1.getNombre());
        persona1.setNombre("Esteban");
        System.out.println("persona1 nombre: "+persona1.getNombre());
    }
    
}
