from os import *
from sys import *
from collections import *
from math import *
import copy
def solve(startIndex,curIndex,s,curOut,output,dictionary):
    if curIndex==len(s)-1:
        if str(s[startIndex:curIndex+1]) in dictionary:
            curOut.append(s[startIndex:curIndex+1])
            word=' '.join(curOut)
            output.append(word)
            curOut.pop()
        return 
    if str(s[startIndex:curIndex+1]) in dictionary:
        curOut.append(s[startIndex:curIndex+1])
        solve(curIndex+1,curIndex+1,s,curOut,output,dictionary)
        curOut.pop() 
    solve(startIndex,curIndex+1,s,curOut,output,dictionary)
def wordBreak(s, dictionary):
    dictionary=set(dictionary)
    curOut,output=[],[]
    startIndex,curIndex=0,0
    solve(startIndex,curIndex,s,curOut,output,dictionary)
    return output