import java.util.Scanner;
public class validIP {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int flag = 0;
        String str = sc.nextLine();

        String arr [] = str.split("\\.");
        int count =1;

        for(String i:arr){
            System.out.println(i);
            count++;
        }

        if(count != 4){
            System.out.println("Not valid");
        }
        else{
            for(int i=0; i<4; i++){
                int val = Integer.parseInt(arr[i]);
                if(val <=0 || val >= 255){
                    flag = 1;
                }
            }
            if(flag == 0){
                System.out.println("Valid IP address");
            }
            else{
                System.out.println("Not valid.......");
            }
        }
        
    }
}
