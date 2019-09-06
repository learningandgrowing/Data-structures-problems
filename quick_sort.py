def partition(arr, si, ei):
    pivot = arr[si]
    c = 0
    for i in range(si+1, ei+1):
        if arr[i]<pivot:
            c = c + 1
    arr[si + c], arr[si] = arr[si], arr[si+c]
    pivot_index = si + c
    
    i = si
    j = ei
    while i < j:
        if arr[i]<pivot:
            i = i + 1
        elif arr[j]>= pivot:
            j = j - 1
        else:
            arr[i], arr[j] = arr[j], arr[i]
            i = i + 1
            j = j -1
    return pivot_index
            
        
            
            
def quicksort(arr, si, ei):
    if si >= ei:
        return
    
    pivot_index = partition(arr, si, ei)
    quicksort(arr,si, pivot_index - 1)
    quicksort(arr, pivot_index + 1,ei)
    
n = int(input())
arr = list(int(x) for x in input().strip().split())
quicksort(arr,0,len(arr)-1)

for num in arr:
    print(num, end = ' ')

    
    
    
    