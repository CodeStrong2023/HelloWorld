
package test;


public class TestMatrices {
    public static void main(String[] args) {
        int edades[][] = new int[3][2];
        System.out.println("edades = " + edades);
        edades[0][0] = 5; //Llenado manual
        edades[0][1] = 7; //Es una diferente columna
        edades[1][0] = 8;
        edades[1][1] = 4;
        edades[2][0] = 2; //Tarea
        edades[2][1] = 9;
        
        System.out.println("edades 0-0 = " + edades [0] [0]);
        System.out.println("edades 0-1 = " + edades [0] [1]);
        System.out.println("edades 1-0 = " + edades [1] [0]);
        System.out.println("edades 1-1 = " + edades [1] [1]);
        System.out.println("edades 2-0 = " + edades [2] [0]);
        System.out.println("edades 2-1 = " + edades [2] [1]);
        System.out.println("Recorremos la matriz a traves del ciclo for");
        for (int fila = 0; fila < edades.length; fila++) {
            for (int col = 0; col < edades[fila].length; col++) {
                    System.out.println("Edades  " + fila+"-"+col+": "+edades[fila][col]);
            }
        }
        
        //Sintaxis clasica
        //String frutas[][] = new String[3][2];
        
        //Sintaxis simplificada
        String frutas[][] = {{"Limon", "Pomelo",},{"Ciruela", "Kiwi"},{"Manzana","Banana"}};
        
        for (int i = 0; i < frutas.length; i++) {
            for (int j = 0; j < frutas[i].length; j++) {
                    System.out.println("frutas  " + i+"-"+j+": "+frutas[i][j]);
            }
        }
    }
}
