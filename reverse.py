def rev():
    n = int(input())
    num = n
    rev = 0
    while (n != 0):
        div = n % 10
        rev = rev*10 + div
        n = n//10
    if (num == rev):
        print('true')
    else:
        print('false')
    
    
rev()

        
