import java.util.*;
public class socks {
    public static void main(String[] args){
        Scanner sc = new Scanner(System.in);

        int n = sc.nextInt(), arr[]= new int[n];
        for(int i=0; i<n; i++){
            arr[i] = sc.nextInt();
        }

        int count [] = new int[n], res =0;

        for(int i=0; i<n; i++){
            count[arr[i]] ++;
        }
        for(int i=0; i<n; i++){
            if(count[i] %2 != 0){
                res++;
            }
        }

        System.out.println(res);
        sc.close();
    }
}
