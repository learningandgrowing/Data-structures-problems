def merge(a1, a2, arr):
    i = 0
    j = 0
    k = 0
    l = len(a1)
    m = len(a2)
    while (i<l) and (j<m):
        if a1[i] < a2[j]:
            arr[k] = a1[i]
            
            i += 1
            k += 1
            
        else:
            arr[k] = a2[j]
            j += 1
            k += 1
    while i < l:
        arr[k] = a1[i]
            
        i += 1
        k += 1
        
        
    while j < m:
        arr[k] = a2[j]
        j += 1
        k += 1
    
def mergesort(arr, n):
    if len(arr) == 0 or len(arr) == 1:
        return
    mid = len(arr)//2
    a1 = arr[:mid]
    a2 = arr[mid:]
    mergesort(a1, n)
    mergesort(a2, n)
    
    merge(a1 ,a2 , arr)
n = int(input())
arr= list(int(x) for x in input().strip().split())
mergesort(arr, n)
for num in arr:
    print(num, end = ' ')
    


