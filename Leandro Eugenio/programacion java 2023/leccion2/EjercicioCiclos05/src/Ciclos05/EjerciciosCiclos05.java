/*
 Ejercicio 05: Realizar un juego apra adivinar un unmero,
para ello generar un numero aleatoprio entre 0-100, y
luego ir pidiendo numeros indicando " es mayor" o "es menor"
segun sea mayor o menor con respecto a N
El proceso termina cuando eñ usuario acierta y mostramos
el numero de intentos hechos
 */
package Ciclos05;

import javax.swing.JOptionPane;

public class EjerciciosCiclos05 {
    public static void main(String[] args) {
        int numero, aleatorio, conteo =0;
        aleatorio = (int)(Math.random()*100);
        numero = Integer.parseInt(JOptionPane.showInputDialog(null, "Digite un numero"));
        do {            
            
            if (numero < aleatorio) {
                numero = Integer.parseInt(JOptionPane.showInputDialog(null, "Digite un numero mayor"));
               
            }else{
                numero = Integer.parseInt(JOptionPane.showInputDialog(null,"Digite un numero menor"));
            }
            conteo ++;
        } while (aleatorio != numero);
        JOptionPane.showMessageDialog(null,"Adivinaste el numero");
        JOptionPane.showMessageDialog(null,"la cantidad de intentos fue: "+conteo);
    }
}
