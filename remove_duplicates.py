def removeduplicates(string):
    if len(string) == 0 or len(string)==1:
        return string
    if string[0] == string[1]:
        smalleroutput = removeduplicates(string[1:])
        return smalleroutput
    else:
        smalleroutput = removeduplicates(string[1:])
        return string[0] + smalleroutput
print(removeduplicates(input()))

