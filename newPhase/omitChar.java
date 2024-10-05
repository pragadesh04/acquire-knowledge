import java.util.*;
public class omitChar {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);

        String str = sc.nextLine();

        for(int i=0; i<str.length(); i++){
            // String val = "";
            if(str.charAt(i) >= '0' && str.charAt(i) <= '9'){
                while(i < str.length() && str.charAt(i)   >= '0' && str.charAt(i) <= '9'){
                    System.out.print(str.charAt(i));
                    i++;
                }
                System.out.print("\n");
            }
        }
        sc.close();
    }
}