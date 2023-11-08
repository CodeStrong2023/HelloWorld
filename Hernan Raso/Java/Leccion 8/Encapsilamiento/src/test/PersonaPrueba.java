
package test;

import dominio.Persona;

public class PersonaPrueba {
    public static void main(String[] args) {
        Persona persona1 =  new Persona("Osvaldo", 57.00, false);
        
        //Modificar a traves de los metodos
        persona1.setNommbre("Juan Ignacio");
        //persona1.nombre = "Juan Ignacio"; //ya no se puede utilizar
        //System.outprintln("Nombre es: "+persona1.nombre); //error
        System.out.println("persona1 su nombre es: "+persona1.getNommbre());
        System.out.println("persona1 con su nombre modificado: "+persona1.getNommbre());
        System.out.println("persona1 el resultado para el sueldo: "+persona1.getSueldo());
        System.out.println("persona1 para obtener el boobleano: "+persona1.isEliminado());
        //Tarea: Crear otro objeto de tipo Persona, asignar valores de manera inicial
        //y imprimir, luego modificar sus valores y volver a imprimir
        System.out.println("persona1 = " + persona1);
    }
    
   
}
