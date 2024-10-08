import java.util.*;
public class revStrWithSpace {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);

        String str = sc.nextLine();

        System.out.println(str);

        String str2 = str.replace(" ", "");
        System.out.println(str2);
        
        int j = str2.length()-1;

        for(int i=0; i<str.length(); i++){
            if(str.charAt(i) == ' '){
                System.out.print(" ");
            }
            else{
                System.out.print(str2.charAt(j));
                j--;
            }
        }

        sc.close();
    }
}
