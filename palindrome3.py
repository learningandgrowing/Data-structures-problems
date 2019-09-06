
def palindromest(statement):
    i = 0
    j = len(statement)-1
    
    while i < j:
        if statement[i].isalpha() and statement[j].isalpha():
            if statement[i] != statement[j]:
                return False
            else:
                i += 1
                j -= 1
        elif statement[i].isalpha():
            j -= 1
        elif statement[j].isalpha():
            i += 1
    return True
    
statement = input().split()    
print(palindromest(statement))