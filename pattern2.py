n = int(input())
print(1)
i = 1
while i<n:
    j = 0
    
    while j<=i:
        if (j==0 or j==i):
            print('1', end = '')
        else:
            print('0', end ='')
        j = j+1
    print()
    i = i+1