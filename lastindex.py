def firstIndex(arr, x,):
    
    if len(arr) ==0:
        return -1
    smallerlist = arr[1:]
    smallerlistoutput = firstIndex(smallerlist, x)
    if smallerlistoutput != -1:
        return smallerlistoutput + 1
    else:
        if arr[0] == x:
            return 0
        else:
            return -1
        
        

# Main
from sys import setrecursionlimit
setrecursionlimit(11000)
n=int(input())
arr=list(int(i) for i in input().strip().split(' '))
x=int(input())
print(firstIndex(arr, x, ))