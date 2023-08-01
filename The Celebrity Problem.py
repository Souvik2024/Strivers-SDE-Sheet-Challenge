from os import *
from sys import *
from collections import *
from math import *
def findCelebrity(n, knows):
    i=0
    j=n-1
    while i<j:
        if knows(i,j):
            i+=1
        else:
            j-=1
    for A in range(n):
        if A!=i and (knows(A,i)==False or knows(i,A)):
            return -1
    return i
    pass