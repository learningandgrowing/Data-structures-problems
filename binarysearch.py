def search_elem(arr,ele)
    start = 0
    end = len(arr)-1
    while start <= end:
        mid = (start+end)//2
        if arr[mid] == ele:
            return mid
        elif (arr[mid]<ele):
            start = mid + 1
        else:
            end = mid - 1
    return -1
            
    
n = int(input())
arr = list(int(i) for i in input().strip().split())
ele = int(input())
print(search_elem(arr,ele))