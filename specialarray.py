
def specialproduct(arr):
    product = 1
    ans = []
    for i in range(len(arr)):
        newarr = arr[0:i] + arr[i+1:]
        for j in newarr:
            product = product*j
        ans.append(product)
        product = 1
    for ans in ans:
        print(ans)
        
            
n = int(input())
arr = []
for i in range(n):
    var = int(input())
    arr.append(var)
specialproduct(arr)