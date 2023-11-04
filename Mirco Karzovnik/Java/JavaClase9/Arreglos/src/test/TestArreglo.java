
package test;

public class TestArreglo {
    public static void main(String[] args) {
        int edades[] = new int [3];
        System.out.println("edades = " + edades);
        
        edades[0] = 22;
        System.out.println("edades 0 = " + edades[0]);
        
        edades[1] = 23;
        System.out.println("edades 1 = " + edades[1]);
        
        edades[2] = 24;
        System.out.println("edades 2 = " + edades[2]);
        
        for (int i = 0; i < edades.length; i++) {
            System.out.println("edades y sus elementos "+i+": "+edades[i]);
        }
        
    }
}
