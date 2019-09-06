n = int(input())
x = 1
for _ in range(n, 0, -1):
    print(' '*_ + '*'*x)
    x=x+2
    _ = _-1
    

    
    