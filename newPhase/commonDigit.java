import java.util.Scanner;

public class commonDigit {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        String str = "";
        int arr [] = new int[10];
        
        for(int i = 0; i<3; i++){
            str += sc.nextLine();
        }

        for(int i=0; i<str.length(); i++){
            arr[(int)str.charAt(i)-'0'] += 1;
        }

        for(int i=0; i<10; i++){
            if(arr[i] >= 3) System.out.println(arr[i]);
        }

        sc.close();
    }
}
