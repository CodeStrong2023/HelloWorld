
package caja;


public class PruebaCaja {
    public static void main(String[] args) {
        //variables locales
        int medidaAncho = 3;//valores ingresados en codigo duro
        int medidaAlto = 2;
        int medidaProfundo = 6;
        
        Caja caja1 = new Caja();//Instanciamos el objeto, constructor vacio
        caja1.ancho = medidaAncho;
        caja1.alto = medidaAlto;
        caja1.profundo = medidaProfundo;
        int resultado = caja1.calcularVolumen();//llamamos al metodo
        //primer resultado
        System.out.println("El resultado volumen de caja 1: "+ resultado);
        
        Caja caja2 = new Caja(2,4,6);//llamamos al constructor 2 con nuevos argumentos
        //llamamos con el nuevo argumento al metodo para un nuevo calculo
        System.out.println("El resultado volumen de caja 2: "+ caja2.calcularVolumen());
    }
}
