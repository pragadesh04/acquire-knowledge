import java.util.*;

public class arrInt {
    public static void main(String[] args){
        Scanner sc = new Scanner(System.in);

        int num = sc.nextInt(), diff = sc.nextInt();

        int n = sc.nextInt();

        int arr[] = new int[n], res = 0;

        for(int i =0; i<n; i++){
            arr[i] = sc.nextInt();
        }
        for(int i =0; i<n; i++){
            System.out.print(arr[i]);
        }
        for(int i=0; i<n; i++){
            if(num-arr[i] <= diff){
                res ++;
            }
        }

        sc.close();
        System.out.println(res);
    }
}
