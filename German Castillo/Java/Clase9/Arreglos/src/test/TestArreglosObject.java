
package test;

import domain.Persona;



public class TestArreglosObject {
    public static void main(String[] args) {
        Persona personas[] = new Persona[2];
        personas[0] = new Persona("Leandro");
        personas[1] = new Persona("Euenio");
        System.out.println("personas 0= " + personas[0]);
        System.out.println("personas 1= " + personas[1]);
    }
}
