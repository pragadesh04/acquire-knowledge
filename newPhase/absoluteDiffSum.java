import java.util.*;
public class absoluteDiffSum{
    public static void main(String[] args){
        Scanner sc = new Scanner(System.in);
        int v = sc.nextInt(), res = 0, i;
        int arr[] = new int[v];
        for(i=0; i<v; i++){
            arr[i] = sc.nextInt();
        }
        sc.close();
        for(i=1; i<v; i++){
            res += Math.abs(arr[i]-arr[i-1]);
        }
        res += Math.abs(arr[0] - arr[i-1]);
        System.out.printf("%d", res);
    }
}