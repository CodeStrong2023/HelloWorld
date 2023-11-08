
package test;


public class TestArreglos {
    public static void main(String[] args) {
        int edades[] = new int [3]; //ind edades [] es una variable /=/ new int [3] es un objeto tipo object
        System.out.println("edades = " + edades);
        
        edades[0] = 17;
        System.out.println("edades 0= " + edades[0]);
        edades[1] = 18;
        System.out.println("edades 1 = " + edades[1]);
        edades[2] = 19;
        System.out.println("edades 2= " + edades[2]);
        
        //edades[3] = 7;//daria error en la ejecucion porque el arreglo no llega a 3
        
        for (int i=0; i<edades.length; i++ ){//length es una funcion que recorre el largo del arreglo
            System.out.println("Edades y sus elementos "+i+": "+edades[i]);
        }
    }
 
}
