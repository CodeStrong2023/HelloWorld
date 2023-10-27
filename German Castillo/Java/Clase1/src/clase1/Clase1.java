package clase1;

public class Clase1 {
    public static void main(String[] args) {
        var conteo = 0; //Inferencia de tipos
        while(conteo <= 7){
            System.out.println("conteo = " + conteo);
            conteo++; //Vamos aumentando en 1 la variable
        }
        
        var contador = 0;
        do{
            System.out.println("contador = " + contador);
            contador++;
        // Uso de las palabaras break y continue junto a las etiquetas (labels)
        }while(contador <= 7);
        for(var contando = 0; contando < 7; contando++){
            if(contando % 2 != 0){
                System.out.println("contando" + contando);
                break; //Vamos a la siguiente iteracion
        }
        inicio:
        for(contando = 0; contando < 7; contando++){
            if(contando % 2 != 0){
                continue inicio; //Vamos a la siguiente iteracion
            }
            System.out.println("contando" + contando); 
        }
    }
}