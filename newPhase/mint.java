import java.util.*;
public class mint {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int m = sc.nextInt(), n = sc.nextInt(), res = m;
        for(int i=0; i<n-1; i++){
            res += res-1;
        }
        System.out.println(res);
        sc.close();
    }
}
