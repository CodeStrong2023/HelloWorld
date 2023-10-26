
package test;

import dominio.Persona; //si ponemos import dominio.*; eso llama a todas las clases a la vez.
public class PersonaPrueba {
    public static void main(String[] args) {
        Persona persona1 = new Persona("Osvaldo", 57000, false);
        System.out.println("persona1 = " + persona1);
        System.out.println("persona1 su nombre es: "+persona1.getNombre());
        
        //modificar a traves de los metodos
        persona1.setNombre("Juan Ignacio");
        System.out.println("persona1 su nombre modificado es: "+persona1.getNombre());
        System.out.println("persona1 el sueldo es: "+persona1.getSueldo());
        System.out.println("persona1 para el booleano: "+persona1.isEliminado());
        
        //actividad: crear otro objeto, asignar valores, imprimir luego reasignar valores nuevos e imprimir de vuelta
        Persona persona2 = new Persona("Alan Garrido",16000,true);
        System.out.println("persona2 es: "+persona2.getNombre());
        System.out.println("persona2 sueldo: "+persona2.getSueldo());
        System.out.println("persona2 boolean: "+persona2.isEliminado());
        
        //modificacion
        persona2.setNombre("Sebastian Garrido");
        System.out.println("persona2 es: " + persona2.getNombre());
        persona2.setSueldo(30000);
        System.out.println("persona2 sueldo: " + persona2.getSueldo());
        persona2.setEliminado(false);
        System.out.println("persona2 boolean: " + persona2.isEliminado());
        
        System.out.println("persona1 = " + persona1);
    }
}
