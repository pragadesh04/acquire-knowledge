import java.util.*;
public class palindrome {
    public static Boolean isPali(String str) {
        StringBuilder s = new StringBuilder(str);
        return ((s.toString()).equals((s.reverse().toString())));
    }
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);

        int st = sc.nextInt(), en = sc.nextInt();
        for(int i=st; i<en; i++){
            if(isPali(Integer.toString(i))){
                System.out.println(i);
            }
        }
        sc.close();
    }
}
