def palindromestring(check):
    i = 0
    j = len(check)-1
    while i < j:
        if check[i] != check[j]:
            return False
        else:
            i += 1
            j -= 1
    return True
        
    
check = input()
print(palindromestring(check))