"""
Consider the following:

    A string, s, of length n  where s = c0 c1 c2 .. 
    An integer, k, where k is a factor of n

we can split s into n/k subsegments where each subsegment, ti, consists of a contiguous block of k characters in s.

then.use each ti to create string ui such that:

    The characters in ui are a subsequence of the characters in ti.
    Any repeat occurrence of a character is removed from the string such that each character in Ui occurs exactly
    once. In other words, if the character at some index j in ti occurs at a previous index <j in ti, then do not
    include the character in string ui

    Given s and k, print n/k lines where each line i donetes string ui.

    Input format

    the firs line contains a single string denoting s
    the second line contains an integer, k, denoting the length of each subsegment.

    URL=https://www.hackerrank.com/challenges/merge-the-tools/problem

Python 3.x
"""


def merge_the_tools(string, k):


    for subcad in [string[i-k:i:] for i in range(len(string)+1) if(i%k==0 and i!=0)]:
        aux=list(subcad[::-1])
        aux2=list(subcad[::-1])
        for cad in aux2:
            if(aux.count(cad)>1):
                aux.remove(cad)
           
        print("".join(aux[::-1]))