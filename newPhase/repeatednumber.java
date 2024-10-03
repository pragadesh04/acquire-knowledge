import java.util.*;
public class repeatednumber {
    public Boolean check(int val){
        int temp = val, unit;
        while(temp != 0){
            ArrayList<Integer> arr = new ArrayList<>();
            unit = temp % 10;
            temp /= 10;
            if (arr.contains(unit)){
                return false;
            }
            else{
                System.out.print("ok");
                arr.add(unit);
            }
        System.out.printf("%d %d",arr.get(0), arr.get(1));
        }
        return true;
    }
    public void main(String[] args){
        Scanner sc = new Scanner(System.in);

        int st = sc.nextInt(), en = sc.nextInt();

        for(int i=st; i<en; i++){
            if(check(i)){
                System.out.println(i);
            }
        }
    }
}