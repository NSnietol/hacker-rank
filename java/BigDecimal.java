
/*
Given an array, s, of n real number strings, sort them in descending order — but wait, there's more! Each number must be printed in the exact same format as it was read from stdin, meaning .1 that 0.1 is printed as 0.1 , and  is printed as . If two numbers represent numerically equivalent values (e.g., 0.1 = .1), then they must be listed in the same order as they were received as input).

Complete the code in the unlocked section of the editor below. You must rearrange array S 's elements according to the instructions above.



Input format

The first line consists of a single integer, n , denoting the number of integer strings. 
Each line  i  of n the  subsequent lines contains a real number denoting the value of  Si.


Output Format

Locked stub code in the editor will print the contents of array S to stdout. You are only responsible for reordering the array's elements.
**/


import java.math.BigDecimal;
import java.util.*;

class Solution{
    public static void main(String []args){
        //Input
        Scanner sc= new Scanner(System.in);
        int n=sc.nextInt();
        String []s=new String[n+2];
        // La persona que propuso el reto asignò String[n+2]
        for(int i=0;i<n;i++){
            s[i]=sc.next();
        }
        sc.close();

     // The idea is to keep the string format stored in vector
     //  In order for  the ordering criterion is based on representation
     // BigDecimal of each value so that the numerical value is not altered.
     // that is formatted as a string for example: .1 does not become 0.1
     // when casting to numerical value           
    Comparator<String> comparetor = new Comparator<String>() {
    @Override
    public int compare(String s1, String s2) {
        BigDecimal a = new BigDecimal(s1);
        BigDecimal b = new BigDecimal(s2);
        return b.compareTo(a); 
    }
};

Arrays.sort(s, 0, n, customComparator);


        //Output
        for(int i=0;i<n;i++)
        {
            System.out.println(s[i]);
        }
    }
}