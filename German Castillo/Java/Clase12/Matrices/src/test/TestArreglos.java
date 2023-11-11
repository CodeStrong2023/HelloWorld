
package test;


public class TestArreglos {
    public static void main(String[] args) { // El lado derecho instanciamos un objeto de tipo objet
        int edades [] = new int [3]; // El lado izq. declaramos la variable
        System.out.println("edades = " + edades);
        
        edades[0] = 17;
        System.out.println("edades 0 = " + edades [0]);
        
        //Tarea Modificar el indice 1 y 2
        edades[1] = 20;
        System.out.println("edades 1 = " + edades [1]);
        edades[2] = 34;
        System.out.println("edades 2 = " + edades [2]);
        
        for(int i = 0; i < edades.length; i++){
            System.out.println("edades y sus elementos "+i+": "+edades[i]);
        }
    }
}
