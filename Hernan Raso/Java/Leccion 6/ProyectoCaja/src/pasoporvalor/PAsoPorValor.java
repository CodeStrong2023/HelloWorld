
package pasoporvalor;

public class PAsoPorValor {
    public static void main(String[] args) {
        var valorX = 20;
        System.out.println("valorX = " + valorX);
        cambioValor(valorX); // solo le enviamos una copia
        System.out.println("valorX = " + valorX);
    }
    
    public static void cambioValor(int arg1){
        System.out.println("asrg1 = " + arg1);
        arg1 = 15;
    }
}
