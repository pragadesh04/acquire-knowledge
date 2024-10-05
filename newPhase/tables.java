import java.util.*;

public class tables {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int tab = sc.nextInt(), range = sc.nextInt(), sum = 0;

        for(int i=1; i<=range; i++){
            System.out.printf("%d x %d = %d\n",i,tab,i*tab);
            sum += i*tab;
        }
        System.out.println(sum);
        sc.close();
    }
}
