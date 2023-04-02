import java.util.Scanner; 
import java.util.ArrayList;


class Main {
  public static void main(String[] args) {
    Scanner scan = new Scanner(System.in);
    ArrayList<Integer> div = new ArrayList<Integer>();

    System.out.println("Enter number");
    int number = scan.nextInt(); 
    int j = 0;
    for (int i = 1; i < number; i++) {
    if (number % i == 0){
        div.add(i);
    }
    }
    System.out.println(div);

  }
}

