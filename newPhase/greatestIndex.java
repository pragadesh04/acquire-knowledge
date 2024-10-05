import java.util.*;

public class greatestIndex {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);

        int n = sc.nextInt(), arr []= new int[n];
        for(int i=0; i<n; i++){
            arr[i] = sc.nextInt();
        }
        int g = arr[0], j = 0;
        for(int i=1; i<n; i++){
            if(g < arr[i]){
                g = arr[i];
                j = i;
            }
        }
        System.out.println(j);

        sc.close();
    }
}