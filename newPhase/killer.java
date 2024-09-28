import java.util.*;

class killer{
    public static void main(String[] args){
        Scanner sc = new Scanner(System.in);

        int i = 1, n = sc.nextInt();

        while(i<=n){
            i *= 2;
        }

        i = ((n-(i/2)*2)+1);
        System.out.print(i);

        sc.close();
    }
}