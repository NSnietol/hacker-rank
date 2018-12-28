/**
A string containing only parentheses is balanced if the following is true: 1. if it is an empty string 2. if A and B are correct, AB is correct, 3. if A is correct, (A) and {A} and [A] are also correct.

Examples of some correctly balanced strings are: "{}()", "[{()}]", "({()})" 

Examples of some unbalanced strings are: "{}(", "({)}", "[[", "}{" etc.

Given a string, determine if it is balanced or not.

Input Format

There will be multiple lines in the input file, each having a single non-empty string. You should read input till end-of-file.

The part of the code that handles input operation is already provided in the editor.

Output Format

For each case, print 'true' if the string is balanced, 'false' otherwise.

Sample Input

{}()
({()})
{}(
[]
Sample Output

true
true
false
true
Reference : https://www.hackerrank.com/challenges/java-stack/problem

*/

import java.util.*;
class Solution{
    
    public static boolean check(String s) {
        
        Stack<Character> validator = new Stack<>();
        char[] characterList = s.toCharArray();
        
        for (char c : characterList) {
            
            if(c=='{') {
                validator.push('{');
            }else if (c=='[') {
                validator.push('[');
            }else if (c=='(') {
                validator.push('(');
            }else {
                if(validator.size()==0){
                    return false;
                }
                if(c=='}' && validator.peek()=='{') {
                    validator.pop();
                }else if(c==']' && validator.peek()=='[') {
                    validator.pop();
                }else if(c==')' && validator.peek()=='(') {
                    validator.pop();
                }else{
                    return false;
                }
                
            }
            
        }
        return validator.size()==0;
        
    }
    
    public static void main(String []argh)
    {
        Scanner sc = new Scanner(System.in);
        
        while (sc.hasNext()) {
            String input=sc.next();
    
            System.out.println(Solution.check(input));
            
        }
        
    }
}





