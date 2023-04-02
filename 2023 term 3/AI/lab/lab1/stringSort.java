import java.util.Scanner; 
import java.util.ArrayList;


class Maina {
  public static void main(String[] args) {
    Scanner scan = new Scanner(System.in);
    ArrayList<String> words = new ArrayList<String>();

    System.out.println("Enter number of strings");
    String a = scan.nextLine();
    int loop = Integer.parseInt(a);
    
    for (int i = 0; i < loop; i++) {

    System.out.println("Enter string");
    String word = scan.nextLine();
    words.add(word);
    }
    
    for (int i = 0; i < words.size()-1; i++) {
        for (int j = i+1; j < words.size(); j++) {
            if (words.get(i).compareToIgnoreCase(words.get(j))>0)
            {
              String temp = words.get(i);  
	            words.set(i,words.get(j));
              words.set(j,temp);    
            }

    }

  }
  System.out.println(words);
}}