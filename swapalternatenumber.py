def swap(arr):
    size = len(arr)
    for j in range(0,size-1,2):
        arr[j],arr[j+1] = arr[j + 1], arr[j]
arr = list(int(i) for i in input().strip().split(' '))
swap(arr)
for i in arr:
    print(i, end=' ')
print()
