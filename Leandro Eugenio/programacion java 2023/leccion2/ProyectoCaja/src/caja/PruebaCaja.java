/*
proyecto caja:
Ejercicio 1: crear un proyecto, segun las especificaciones
mostradas a continuacion
la formula es: volumen = ancho * alto * profundidad

*/
package caja;

public class PruebaCaja {
     public static void main(String[] args) {
        //Variables locales
        int medidaAncho = 3; //valores ingresado en codigo duro
        int medidaAlto = 2;
        int medidaProf = 6;
        
        Caja caja1 = new Caja(); //instanciamos el objeto
        caja1.ancho = medidaAncho;
        caja1.alto = medidaAlto;
        caja1.profundo = medidaProf;
        int resultado = caja1.calcularVolumen(); //llamamos al metodo
         System.out.println("resultado volumen de caja 1: " + resultado);
         
         Caja caja2 = new Caja(2, 4, 5); //llamamos al constructor 2 con nuevos argumentos
         //llamamos con el nuevo objeto al metodo para un nuevo calculo
         System.out.println("resultado volumen de caja 2: " + caja2.calcularVolumen());
        
        
    }
}
