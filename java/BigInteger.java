/*

Reference
https://www.hackerrank.com/challenges/java-biginteger/problem
**/

import java.io.*;
import java.math.BigInteger;
import java.util.*;


public class Solution {

    public static void main(String[] args) {
        /* Enter your code here. Read input from STDIN. Print output to STDOUT. Your class should be named Solution. */
    
        Scanner sc= new Scanner(System.in);
        BigInteger n1=sc.nextBigInteger();

        BigInteger n2=sc.nextBigInteger();

        System.out.println(n1.add(n2));

        System.out.println(n1.multiply(n2));
    
    
    }
}

