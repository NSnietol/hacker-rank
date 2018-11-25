/*Objective

In this challenge, we learn about Arrays. Check out the attached tutorial for more details.

Task

Complete the getSecondLargest function in the editor below. It has one parameter: an array, nums, of n numbers. The function must find and return the second largest number in nums.

Input Format

Locked stub code in the editor reads the following input from stdin and passes it to the function: 
The first line contains an integer,n , denoting the size of the nums array. 
The second line contains n space-separated numbers describing the elements in .

https://www.hackerrank.com/challenges/js10-arrays/problem
**/

function getSecondLargest(nums) {
    // Complete the function

    nums.sort(function(a, b) {
        return a - b;
    });

    nums.reverse()

    let aux = nums[0] // Max

    for (let value of nums) {
        if (value < aux) {
            return value
        }
    }
}

function main() {
    const n = +(readLine());
    const nums = readLine().split(' ').map(Number);

    console.log(getSecondLargest(nums));
}