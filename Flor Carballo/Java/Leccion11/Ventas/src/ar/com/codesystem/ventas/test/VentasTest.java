
package ar.com.codesystem.ventas.test;

import ar.com.codesystem.ventas.Orden;
import ar.com.codesystem.ventas.Producto;


public class VentasTest {
    public static void main(String[] args) {
        Producto producto1 = new Producto("Pantalón", 12000.00);
        Producto producto2 = new Producto("Campera", 25000.00);
        Producto producto3 = new Producto("Remera", 6000.00);
        Producto producto4 = new Producto("Zapatos", 30000.00);
        Producto producto5 = new Producto("Camisa", 15000.00);
        
        Orden orden1 = new Orden();
        //Agregamos productos al arreglo
        orden1.agregarProducto(producto1);
        orden1.agregarProducto(producto2);
        orden1.agregarProducto(producto3);
        orden1.agregarProducto(producto4);
        orden1.agregarProducto(producto5);
        orden1.mostrarOrden();
        
        //Tarea: Crear más objetos de tipo Producto 
        //Crear más objetos de tipo Orden
    }
}
