import java.util.*;
public class typeAndChocolate {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);

        int n = sc.nextInt();
        ArrayList<Integer> arr = new ArrayList<>();
        
        for(int i=0; i<n; i++){
            arr.add(sc.nextInt());
        }

        Collections.sort(arr);
        n = sc.nextInt();
        int res = 0;

        for(int i=0;i<n; i++){
            res += arr.get(i);
        }
        
        System.out.print(res);
        sc.close();
    }
}
