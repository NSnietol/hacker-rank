/*

You are given n lines. In each line there are zero or more integers. You need to answer a few queries where you need to tell the number located in y position of x line. 

Take your input from System.in.


Input Format
The first line has an integer n. In each of the next n  lines there will be an integer d denoting number of integers on that line and then there will be  d space-separated integers q. In the next line there will be an integer  denoting number of queries. Each query will consist of two integers x and y.

Output Format
In each line, output the number located in y position of  x line. If there is no such position, just print "ERROR!"
* */





import java.util.ArrayList;
import java.util.Arrays;
import java.util.List;
import java.util.Scanner;

public class Solution {

    public static void main(String[] args) {
        /* Enter your code here. Read input from STDIN. Print output to STDOUT. Your class should be named Solution. */
    Scanner scanner = new Scanner(System.in);
            
        int nArrays = Integer.parseInt(scanner.nextLine());
        
        List<List<String>> list = new ArrayList<>();
    
        for (int i = 0; i < nArrays; i++) {
        
         list.add(Arrays.asList(scanner.nextLine().split(" ")));
        }

            int nPoints = Integer.parseInt(scanner.nextLine());


        for (int i = 0; i < nPoints; i++) {
            int x = scanner.nextInt();
            int y = scanner.nextInt();
            try{
                   System.out.println(list.get( x-1).get( y ));
            }catch(IndexOutOfBoundsException e){

                System.out.println("ERROR!");
            
            }    


            

        }
    }
}

