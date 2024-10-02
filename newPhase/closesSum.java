import java.util.*;

public class closesSum {
    public static void main(String[] args){
        Scanner sc = new Scanner(System.in);
        int n = sc.nextInt(), res = 0;
        ArrayList<Integer> arr = new ArrayList<>();
        for(int i = 0; i<n; i++){
            arr.add(sc.nextInt());
        }
        Collections.sort(arr);
        System.out.println("_______________________________");
        for(int i=0; i<n; i++){
            if(i==0){
                res += Math.abs(arr.get(0)-arr.get(1));
            }
            else if(i == n-1){
                res += Math.abs(arr.get(n-2)-arr.get(n-1));
            }
            else{
                res += Math.min(Math.abs(arr.get(i)-arr.get(i-1)),Math.abs(arr.get(i)-arr.get(i+1)));
            }
        }
        System.out.printf("%d", res);
        sc.close();
    }
}
