def insertionsort(arr):
    l = len(arr)
    for i in range(1,l):
        j = i -1
        temp = arr[i]
        while (j>=0 and arr[j] > temp):
            arr[j+1] = arr[j]
            j = j - 1
        arr[j + 1] = temp
n = int(input())
arr = list(int(x) for x in input().strip().split())
insertionsort(arr)
for number in arr:
    print(number, end = ' ')