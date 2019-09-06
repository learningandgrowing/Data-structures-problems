size = int(input())
def triangle():
    for _ in range(1, size+1):
        for j in range(1, _+1):
            
            print('*'* j)
        
        _ = _+1
        
triangle()