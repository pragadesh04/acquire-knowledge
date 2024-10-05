import java.util.*;

public class matSearch {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        
        System.out.println("enter m: ");
        int m = sc.nextInt();
        System.out.println("enter n: ");
        int n = sc.nextInt();

        int arr[][] = new int[m][n];

        for(int i=0; i<m; i++){
            for(int j=0; j<n; j++){
                arr[i][j] = sc.nextInt();
                // System.out.printf("%d %d", i,j);
            }
        }

        int key = sc.nextInt(), f = 0;
        for(int i=0; i<m; i++){
            for(int j=0; j<n; j++){
                if(arr[i][j] == key){
                    System.out.printf("%d %d",i, j);
                    f = 1;
                    break;
                }
            }
        }
        if(f==0){
            System.out.println(-1);
        }
        sc.close();
    }
}
