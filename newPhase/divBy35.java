import java.util.*;
public class divBy35                            {
    public static void main(String[] args)      {
        Scanner sc = new Scanner(System.in);
        int m = sc.nextInt(), n = sc.nextInt(), sum = 0;
        for(int i=m; i<n; i++)                  {
            if(i%15 == 0)                       {
                sum += i;                       }}
        System.out.print(sum);                  
    sc.close();                                 }}