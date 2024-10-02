// import java.util.*;
// public class dice                                                                           {
//     public static void main(String[] args)                                                  {
//         Scanner sc = new Scanner(System.in);
//         int val = sc.nextInt(), va = 0;
//         for(int i=1; i<=6; i++)                                                             {
//             for(int j=1; j<=6; j++)                                                         {
//                 if(i+j == val)                                                              {
//                     System.out.printf("%d + %d = %d\n",i,j, val);
//                     va++;                                                                   }}}
//         System.out.printf("Total Possibilities: %d",va);                             }}

import java.util.*;
class dice{
    public static void main(String[] args){
        Scanner sc = new Scanner(System.in);

        int val = sc.nextInt();

        int i = 1, j = 6;
        while(i < 6 || j >2){
            if(j == 1){
                i++;
            }
            if(i+j == val){
                System.out.printf("%d %d\n",i,j);
            }
            j--;
        }
    }
}