/*
Ejercicio 5: Realizar un juego para adivinar un numero, para ello generar un numero aleatorio entre 0-100, y luego ir 
pidiendo numeros indicando "es mayor" o "es menor" segun sea mayor o menor con respecto a N
El proceso termina cuando el usuario acierta y mostramos el numero de intentos hechos.
 */
package Ciclos03;

import javax.swing.JOptionPane;

public class Ejercicio05ConJOptionPane {
    public static void main(String[] args) {
    int numero, aleatorio, conteo = 0;
        aleatorio = (int)(Math.random()*100); // Esto genera un numero aleatorio
        do{
            numero = Integer.parseInt(JOptionPane.showInputDialog("Ingrese un numero: "));
            if(numero < aleatorio) {
                JOptionPane.showMessageDialog(null, "Ingrese un numero Mayor");
            }
            else if(numero > aleatorio){
                JOptionPane.showMessageDialog(null, "Ingrese un numero Menor");
            }
            else{
                JOptionPane.showMessageDialog(null, "¡¡¡Felicidades!!! Has adivinado el numero");
            }
            conteo++;
        }while(numero != aleatorio);
        JOptionPane.showInternalMessageDialog(null, "Adivinaste el numero en: "+conteo+" intentos");
    }
}
