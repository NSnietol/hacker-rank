/**
Given 2 BitSets, A and B, of size N where all bits in both BitSets are initialized to 0,
perform a series of  M operations. After each operation, print the number of set bits in the respective BitSets as two space-separated integers on a new line.

Input Format

The first line contains 2 space-separated integers, N  (the length of both BitSets B1 and B2 ) and  (the number of operations to perform), respectively. 
The M  subsequent lines each contain an operation in one of the following forms:
AND SET SET
OR SET SET
FLIP SET INDEX
SET SET INDEX

Input format
In the list above, SET is the integer  1 or 2, where  denotes  A and  denotes B. 
Index is an integer denoting a bit's index in the BitSet corresponding to set.

For the binary operations , , and , operands are read from left to right and the BitSet resulting from the operation replaces the contents of the first operand. For example:

Output Format

After each operation, print the respective number of set bits in BitSet A and BitSet  B as 2 space-separated integers on a new line.
Reference :https://www.hackerrank.com/challenges/java-bitset/problem
*/


import java.util.ArrayList;
import java.util.BitSet;
import java.io.*;
import java.util.Scanner;
import java.util.regex.Pattern;

public class Solution {

	public static void show(ArrayList<BitSet> bits) {
        System.out.println(bits.get(0).cardinality() + " " + bits.get(1).cardinality());

	}
    public static void main(String[] args) {
        /* Enter your code here. Read input from STDIN. Print output to STDOUT. Your class should be named Solution. */

        ArrayList<BitSet> bits = new ArrayList<>();
    

        Scanner sc = new Scanner(System.in);
        String inicial = sc.nextLine();

        int tamano = Integer.parseInt(inicial.split(" ")[0]);
        int numIter = Integer.parseInt(inicial.split(" ")[1]);

        
        bits.add(new BitSet(tamano));
        bits.add(new BitSet(tamano));
        
        
        for (int i = 0; i < numIter; i++) {
            String cadena =  sc.nextLine();
            int numUno = Integer.parseInt(cadena.split(" ")[1])-1;
            int numDos = Integer.parseInt(cadena.split(" ")[2])-1;
            switch (cadena.split(" ")[0].trim()) {
                
            case "AND":

                bits.get(numUno).and(bits.get(numDos));

                show(bits);

                break;
            case "SET":
                bits.get(numUno).set(numDos+1);
               
                show(bits);

                break;
            case "FLIP":
                bits.get(numUno).flip(numDos+1);

                show(bits);
                
                break;
            case "OR":
                bits.get(numUno).or(bits.get(numDos));
                show(bits);
                break;
            case "XOR":
                bits.get(numUno).xor(bits.get(numDos));
                show(bits);                
                break;
            default:
                break;
            }
        }

    }
    
}

