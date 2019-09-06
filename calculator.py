# Write your code here
z = int(input())

while z != 6:
    
    if z <= 5 and  z >= 1:
        m = int(input())
        n = int(input())
    if z == 1:
        sum = m + n
        print(sum)
    if z == 2:
        diff = m - n
        print(diff)
    if z == 3:
        prod = m * n
        print(prod)
    if z == 4:
        quot = m // n
        print(quot)
    if z == 5:
        rem = m % n
        print(rem)

    elif z < 1 or z > 6:
        
        print("Invalid Operation")
    
    z = int(input())