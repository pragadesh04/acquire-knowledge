import java.util.Scanner;
public class mul {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);

        int n = sc.nextInt(), arr []= new int[n];
        for(int i=0; i<n; i++){
            arr[i] = sc.nextInt();
        }
        int arr1 [] = new int[n];
        for(int i=0; i<n; i++){
        int val = 1;
            for(int j =0; j<n; j++){
                if(i != j){
                    val *= arr[j];
                    arr1[i] = val;
                }
            }
        }
        for(int i=0; i<n; i++){
            System.out.println(arr1[i]);
        }
        sc.close();
    }   
}
