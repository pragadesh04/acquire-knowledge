import java.util.*;
public class ratFood {
    public static void main(String[] args){
        Scanner sc = new Scanner(System.in);

        int rat = sc.nextInt(), unit = sc.nextInt(), n = sc.nextInt(), arr [] = new int[n], base = 0, res = 0, totFood = rat * unit;

        System.out.println("-----------");
        for(int i=0; i<n; i++){
            arr[i] = sc.nextInt();
        }

        System.out.println("-----------");
        for(int i=0; i<n; i++){
            if(base < totFood){
                base += arr[i];
                res ++;
            }
            if(i == n-1 && base<totFood){
                res = 0;
                break;
            }
        }

        System.out.println(res);

        sc.close();
    }
}
