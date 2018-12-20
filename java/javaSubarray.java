/**
We define the following:

A subarray of an n -element array is an array composed from a contiguous block of the original array's elements.
For example, if array=[1,2,3] , then the subarrays are [1],[2], [3],[1,2],[1,2,3],[2,3] and . Something like[1,3]  would not be a subarray as it's not a contiguous subsection of the original array.
The sum of an array is the total sum of its elements.
An array's sum is negative if the total sum of its elements is negative.
An array's sum is positive if the total sum of its elements is positive.
Given an array of n integers, find and print its number of negative subarrays on a new line.


Input Format

The first line contains a single integer,n , denoting the length of array A=[a1,a2...an-1] . 
The second line contains n  space-separated integers describing each respective element,ai , in array A.

Reference https://www.hackerrank.com/challenges/java-negative-subarray/problem
*/
import java.io.*;
import java.util.*;

public class Solution {

    public static void main(String[] args) {

        Scanner scan = new Scanner(System.in);
        int q = scan.nextInt();
        int[] array = new int[q];

        for (int i = 0; i < array.length; i++) {
            array[i] = scan.nextInt();

        }
        // 1 -2 4 -5 1
        int aux = 0;
        int value = 0;

        for (int i = 0; i < array.length; i++) {
            value += array[i];
            if (value < 0) {
                aux++;
            }
            for (int j = i + 1; j < array.length ; j++) {

                value += array[j];
                if (value < 0) {
                    aux++;
                }
            }
            value = 0;

        }
        System.out.println(aux);

        scan.close();
    }
}

