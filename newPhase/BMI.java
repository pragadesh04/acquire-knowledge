import java.util.Scanner;

public class BMI {
    public static int checkReturn(float bmi){
        if(bmi < 18) return 0;
        if(bmi >= 18 && bmi < 25) return 1;
        if(bmi >= 25 && bmi < 30) return 2;
        if(bmi >= 30 && bmi < 40) return 3;
        if(bmi >= 40) return 4;
        return -1;
    }
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);

        float w = sc.nextInt(), h = sc.nextInt();
        h /= 100;
        float bmi = w/(h*h);
        System.out.println(bmi);
        
        System.out.println(checkReturn(bmi));

        sc.close();
    }
}
