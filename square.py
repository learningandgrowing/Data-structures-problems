size = int(input())
def square():
    for _ in range(1, size+1):
        if (_ == 1 or _ == size):
            print('*' * size)
        else:
            print('*' + ' '*(size-2) + '*')
            
square()
    
