/** 
 Objective

Today, we're practicing bitwise operations. Check the attached tutorial for more details.

Task

We define  S to be a sequence of distinct sequential integers from 1 to n ; in other words, S={1,2,3,..n} . We want to know the maximum bitwise AND value of any two integers, a and b ( where a <b), in sequence S that is also less than a given integer K, .

Complete the function in the editor so that given n and k, it returns the maximum  a & b < k.

Note: The  symbol represents the bitwise AND operator.
 
Reference : https://www.hackerrank.com/challenges/js10-bitwise/problem
*/
'use strict';

process.stdin.resume();
process.stdin.setEncoding('utf-8');

let inputString = '';
let currentLine = 0;

process.stdin.on('data', inputStdin => {
    inputString += inputStdin;
});

process.stdin.on('end', _ => {
    inputString = inputString.trim().split('\n').map(string => {
        return string.trim();
    });

    main();
});

function readLine() {
    return inputString[currentLine++];
}

let getMaxLessThanK = (n, k) => {

    let aux = 0
    let decimalValue = 0
    for (var i = 1; i < n; i++) {
        // 1 2 3 4 5
        // 2 3 4 5 
        for (var j = i + 1; j <= n; j++) {
            decimalValue = i & j
            if (decimalValue < k) {
                if (decimalValue > aux) {
                    aux = decimalValue
                }
            }

        }
    }
    return aux

}