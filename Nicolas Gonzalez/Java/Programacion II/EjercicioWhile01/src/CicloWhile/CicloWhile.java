package CicloWhile;

public class CicloWhile {

    public static void main(String[] args) {
        //While = ciclo mientras hacer
        var conteo = 0; //inferencia de tipos
        while (conteo <= 7) {
            System.out.println("conteo = " + conteo);
            conteo++; //aumenta en 1 la variable
        }
        System.out.println("-------------------------");

        //Do While = ciclo repetir hasta que
        var contador = 0;
        do {
            System.out.println("contador = " + contador);
            contador++;
        } while (contador <= 7);
        System.out.println("-----------------------------------");

        //For = ciclo para
        for (var contando = 0; contando < 7; contando++) {
            if (contando % 2 == 0) {
                System.out.println("contando = " + contando);
            }
        }
        System.out.println("---------------------------");
        
        for (var contando = 0; contando < 7; contando++) { //(inicio = ?; finalcondicional < ?; contador++)
            if (contando % 2 != 0) {
                continue; //vamos a la siguiente iteracion              
            }
            System.out.println("contando = " + contando);
        }
        System.out.println("-----------------------------");
        
        //etiquetas label
        for (var contando = 0; contando < 7; contando++) {
            if (contando % 2 == 0) {
                System.out.println("contando = " + contando);
            }
        }
        System.out.println("------------------------");
        
        //uso de las etiquetas break y continue junto a las etiquetas(labels)
        inicio:
        for (var contando = 0; contando < 7; contando++) {
            if (contando % 2 == 0) {
                System.out.println("contando = " + contando);
                break inicio;
            }
        }
    }
}
