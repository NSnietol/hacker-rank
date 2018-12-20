/**
 * You are given  a 6 * 6  2D array. An hourglass in an array is a portion shaped like this:

 a b c
  d
e f g

For example, if we create an hourglass using the number 1 within an array full of zeros, it may look like this:

1 1 1 0 0 0
0 1 0 0 0 0
1 1 1 0 0 0
0 0 0 0 0 0
0 0 0 0 0 0
0 0 0 0 0 0

Actually, there are many hourglasses in the array above. The three leftmost hourglasses are the following:

1 1 1     1 1 0     1 0 0
  1         0         0
1 1 1     1 1 0     1 0 0



The sum of an hourglass is the sum of all the numbers within it. The sum for the hourglasses above are 7, 4, and 2, respectively.

In this problem you have to print the largest sum among all the hourglasses in the array.

Input Format

There will be exactly  6 lines, each containing  9 integers seperated by spaces. Each integer will be between  -9  and -9 inclusive.

 * 
 * 
 * 
 * -1 -1 0 -9 -2 -2
-2 -1 -6 -8 -2 -5
-1 -1 -1 -2 -3 -4
-1 -9 -2 -4 -4 -5
-7 -3 -3 -2 -9 -9
-1 -3 -1 -2 -4 -5
 * 
 * 
 * 
 * Reference : https://www.hackerrank.com/challenges/java-2d-array/problem
*/

import java.io.*;
import java.math.*;
import java.security.*;
import java.text.*;
import java.util.*;
import java.util.concurrent.*;
import java.util.regex.*;

public class Solution {



    private static final Scanner scanner = new Scanner(System.in);

    public static void main(String[] args) {
        int[][] arr = new int[6][6];

        for (int i = 0; i < 6; i++) {
            String[] arrRowItems = scanner.nextLine().split(" ");
            scanner.skip("(\r\n|[\n\r\u2028\u2029\u0085])?");

            for (int j = 0; j < 6; j++) {
                int arrItem = Integer.parseInt(arrRowItems[j]);
                arr[i][j] = arrItem;
            }
        }
        int aux = 0;
        int sum = -10000000;
        for (int i = 0; i <4; i++) {
            
            for (int j = 0; j < 4; j++) {
                
                aux = arr[i][j]+arr[i][j+1]+arr[i][j+2];
                aux += arr[i+1][j+1];
                aux += arr[i+2][j]+arr[i+2][j+1]+arr[i+2][j+2];

                if(aux>sum) {
                    sum=aux;
                }
            }
            
        }
        System.out.println(sum);


        scanner.close();
    }
}
