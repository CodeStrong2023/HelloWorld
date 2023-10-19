
package test;

import domain.Cliente;
import domain.Empleado;
import java.util.Date;

public class TestHerencia {
    public static void main(String[] args) {
        Empleado empleado1 = new Empleado("Flor", 2000.00);
        System.out.println("empleado1 = " + empleado1);
        
        Date fecha1 = new Date();
        
        Cliente cliente1 = new Cliente(fecha1, true, "Rufi", 'F', 23, "9 de julio 2000");
        System.out.println("cliente1 = " + cliente1);
        
        
    }
}
