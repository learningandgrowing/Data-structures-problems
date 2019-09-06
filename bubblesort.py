def bubblesort(arr):
    l = len(arr)
    for i in range(l-1):
        for j in range(l-1-i):
            if arr[j]>arr[j+1]:
                arr[j],arr[j+1] = arr[j+1],arr[j]
                
                
n = int(input())
arr = list(int(x) for x in input().strip().split())
bubblesort(arr)
for number in arr:
    print(number,end='')
