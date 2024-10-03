import java.util.*;
public class chkPass {
    public static Boolean checkPass(String str){
        Boolean c = false, n = false;

        if(str.contains(" ") || str.contains("/") || str.length()<4 || (str.charAt(0) >= '0' && str.charAt(0)<='9')){
            return false;
        }
        else{
            for(int i=0; i<str.length(); i++){
                if(str.charAt(i) >= 'A' || str.charAt(i) <= 'Z'){
                    c = true;
                }
                if(str.charAt(i)>='0' && str.charAt(i)<='9') n = true;
            }
        }
        // System.out.println(n);
        return c && n;
    }
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);

        String str = sc.nextLine();

        // if(str.charAt(0) >= '0' && str.charAt(0)<='9') System.out.println("sala");
        if(checkPass(str)){
            System.out.println("valid Password");
        }
        else{
            System.out.println("invalid");
        }
    }
}
