//Ejercicio 5: crear y cargar una matriz de tamaño n x m,mostrar la suma de cada fila y de cada columna
package matriz_ejercicio_3;
import java.util.Scanner;
import javax.swing.JOptionPane;

public class Matriz_Ejercicio_3 {
    public static void main(String[] args) {
        Scanner entrada = new Scanner(System.in);
        int matriz[][], nFilas,nCol,sumarFilas,sumarCol;
        int posFila,posCol;
        
        nFilas = Integer.parseInt(JOptionPane.showInputDialog("a"));
        nCol = Integer.parseInt(JOptionPane.showInputDialog("b"));
        
        matriz = new int [nFilas][nCol];
        int filas[] = new int[nFilas];
        int columnas[] = new int [nCol];
        
        System.out.println("rellenando la matriz");
        for (int i = 0; i < nFilas; i++) {
            for (int j = 0; j < nCol; j++) {
                System.out.println("Matriz ["+i+"]["+j+"]: ");
                matriz[i][j] = entrada.nextInt();
            }
        }
        
    }
    
}
