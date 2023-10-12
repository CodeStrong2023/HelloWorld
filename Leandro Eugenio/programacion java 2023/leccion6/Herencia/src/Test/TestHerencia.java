
package Test;

import domain.Cliente;
import domain.Empleado;
import java.util.Date;

public class TestHerencia {
    public static void main(String[] args) {
        Empleado empleado1 = new Empleado("Leandro",200000.0);
        System.out.println("empleado1 = " + empleado1);
        
        Date fecha1 = new Date();
        Cliente cliente1 = new Cliente(fecha1,true,"Ezequiel",'M',25,"San Rafael");
        System.out.println("cliente1 = " + cliente1);
    }
}
