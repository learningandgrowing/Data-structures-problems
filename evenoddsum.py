n = (input())
num = len(n)
odd = 0
even = 0
for i in range(num):
    if (int(n[i])%2==0):
        even = even + int(n[i])
        i += i
    else:
        odd = odd + int(n[i])
print(even,'',odd)