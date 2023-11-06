
package arreglos_ejercicio_3;

import java.util.Scanner;

public class Arreglos_Ejercicio_3 {
    public static void main(String[] args) {
        Scanner entrada = new Scanner(System.in);
        float numeros[] = new float[5];
        float negativos =0, positivos=0, mediaNegativos=0, mediaPositivos=0;
        int conteo0 = 0, conteo_negativos = 0, conteo_positivos = 0;
        
        System.out.println("Ingresamos los valores al arreglo");
        for (int i = 0; i < 5; i++) {
            System.out.println((i+1)+" Ingrese el numero =");
            numeros[i] = entrada.nextInt();
            if(numeros[i]>0){
                positivos += numeros[i];
                conteo_positivos++;
            }
            else if (numeros[i] <0){
                negativos += numeros[i];
                conteo_negativos++;
            }
            else {
                conteo0++; 
            }
        }
        
        if (conteo_positivos == 0){
            System.out.println("No hay numeros positivos"); 
        }
        else{
            mediaPositivos = positivos/conteo_positivos;
            System.out.println("La media de los numeros Positivos es: "+mediaPositivos);
        }
        
        if (conteo_negativos ==0){
            System.out.println("No hay numeros negativos");
        }
        else{
            mediaNegativos = negativos/conteo_negativos;
            System.out.println("La media de los numeros Negativos es: "+mediaNegativos);
        }
        
        System.out.println("Los ceros son: "+conteo0);

    }
}
