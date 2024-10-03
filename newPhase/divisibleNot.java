import java.util.*;

public class divisibleNot {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int d = sc.nextInt();
        int n = sc.nextInt(), res = 0;

        for(int i=1; i<n+1; i++){
            if(i%d == 0){
                res += i;
            }
            else{
                res -= i;
            }
        }
        System.out.println(Math.abs(res));

        sc.close();
    }
}
