n = int(input())
i = 1
while i<=n:
    j = 1
    while j<=i:
        print(j, end='')
        j += 1
    space = 1
    
    while space<=2*n-2*i:
        print(' ', end='')
        space += 1
    p = 1
    while p <= i:
        print(i-p+1, end ='')
        p += 1
    print()
    i += 1