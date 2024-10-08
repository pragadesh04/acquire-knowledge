import java.util.*;
public class hours24 {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int val = (sc.nextInt())*(sc.nextInt());
        if(val > 12) val -= 12;
        if((val) > 24) val = -1;
        else val = val - 12;
        System.out.println(val);
        sc.close();
    }
}
