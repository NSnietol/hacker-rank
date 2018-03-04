"""
Kevin and Stuart want to play the 'The Minion Game'.

Game Rules

Both players are given the same string, .
Both players have to make substrings using the letters of the string .
Stuart has to make words starting with consonants.
Kevin has to make words starting with vowels. 
The game ends when both players have made all possible substrings. 

Scoring
A player gets +1 point for each occurrence of the substring in the string .

For Example:
String  = BANANA
Kevin's vowel beginning word = ANA
Here, ANA occurs twice in BANANA. Hence, Kevin will get 2 Points. 

Input Format

A single line of input containing the string S. 

Output Format

Print one line: the name of the winner and their score separated by a space.

If the game is a draw, print Draw.

URL=https://www.hackerrank.com/challenges/the-minion-game/problem
"""


def minion_game(string):

    vowels = 'AEIOU'
    size = len(s)
    
    countK = sum([size-i for i in range(size) if string[i] in vowels])
    
    
    countS = sum([size-i for i in range(size) if string[i] not in vowels])
    
    if(countK>countS):
        print("Kevin "+str(countK))
    elif(countS>countK):
        print("Stuart "+str(countS))
    else:
        print("Draw")