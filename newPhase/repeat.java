import java.util.*;
class HelloWorld {
    public static void main(String[] args) {
        String st = "Hi", s = "";
        Scanner sc = new Scanner(System.in);
        int n = sc.nextInt();

        if (n > 0){
            for(int i = 0; i<n; i++){
                s += st;
            }
            System.out.print(s);
        }

        sc.close();
    }
}