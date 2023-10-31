
package pasoPorReferencia;

import Clases.Persona;

public class PasoPorReferencia {
    public static void main(String[] args) {
        Persona persona1 = new Persona();
        persona1.nombre = "ester";
        System.out.println("persona1 nombre = " + persona1.nombre);
        cambiarValor(persona1);
        System.out.println("el cambio que hicimos en el nombre es = " + persona1.nombre);
        persona1 = cambiarElValor(persona1);
        //Persona persona2 = null;
        Persona persona2 = new Persona();
        persona2 = cambiarElValor(persona2);
        System.out.println("persona2 = " + persona2.nombre);
    }
    public static void cambiarValor(Persona persona) { //paso por referencia
        persona.nombre = "Maria";
    }
    public static Persona cambiarElValor(Persona persona) {
        if(persona == null){
            System.out.println("valor de persona invalido = null");
            return null;
        }else{
            persona.nombre = "Monica";
            return persona;
        }
        
    }
}
