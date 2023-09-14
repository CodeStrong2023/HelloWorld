
import java.util.Scanner;


public class EjercicioLibro {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        System.out.println("Proporciona el titulo del libro");
        String libro = scanner.nextLine();
        System.out.println("Proporciona el autor");
        String autor = scanner.nextLine();
        System.out.println(libro+" fue escrito por: "+autor);   
    }
    
    
}
