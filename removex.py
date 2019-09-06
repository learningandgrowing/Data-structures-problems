def removeX(s, x):
    if len(s)==0:
        return s
    
    smalllist = s[1:]
    smalleroutput = removeX(smalllist, x)
    if s[0]== x:
        return smalleroutput
    else:
        return s[0] + smalleroutput
s = "axbxcx"
print(removeX(s, "x"))
         