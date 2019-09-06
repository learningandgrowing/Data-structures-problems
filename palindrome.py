def palindrome(num):
    n =num
    rev = 0
    while num != 0:
        div = num %10
        rev = rev*10 + div
        num = num // 10
    if n == rev:
        return True
    

    
    
num = int(input())
print(palindrome(num))

