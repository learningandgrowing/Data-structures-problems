n = int(input())
i = 1
while i<=n:
    space = 1
    while space <=n-i:
        print(' ', end = '')
        space += 1
    j = 1
    while j<=i:
        print(i-j+1, end ='')
        j += 1
    print()
    i += 1