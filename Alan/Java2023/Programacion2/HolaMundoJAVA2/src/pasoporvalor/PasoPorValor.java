
package pasoporvalor;


public class PasoPorValor {
    public static void main(String[] args) {
        var valorX = 20;
        System.out.println("ValorX = "+valorX);
        CambioValor(valorX);
        System.out.println("valorX = " + valorX);
    }
    
    public static void CambioValor(int arg1){
        System.out.println("arg1 = "+arg1);
        arg1 = 15;
    }
}
