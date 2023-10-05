package test;

import dominio.Persona;

public class PersonaPrueba {
    public static void main(String[] args) {
        Persona persona1 = new Persona("Flor", 16.000, false);
        System.out.println("persona1 su nombre es: "+persona1.getNombre());
        //Modificar a través de los métodos
        persona1.setNombre("Rufi Ru");
        //persona1.nombre = "Rufi Ru"; //Ya no se puede utilizar
        //System.out.println("Nombre es: "+persona1.nombre); //Error
        System.out.println("persona1 su nombre modificado es: "+persona1.getNombre());
        System.out.println("persona1 el resultado para su sieldo: "+persona1.getSueldo());
        System.out.println("persona1 para obtener el booleano: "+persona1.isEliminado());
       
        System.out.println("persona1 = " + persona1);
        //System.out.println("persona1: "+persona1.toString());
    }
 
}

class PersonaPrueba2 {
    public static void main(String[] args) {
        Persona persona2 = new Persona("Tini", 0, true);
        System.out.println("persona2 su nombre es: "+persona2.getNombre());
        persona2.setNombre("Regina Carballo");
        System.out.println("persona1 su nombre modificado es: "+persona2.getNombre());
        System.out.println("persona1 el resultado para su sieldo: "+persona2.getSueldo());
        System.out.println("persona1 para obtener el booleano: "+persona2.isEliminado());
    }
}
        