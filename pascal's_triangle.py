def pascaltriangle(n):
    arr = [[0 for i in range(n)] for j in range(n)]
    for line in range(n):
        for i in range(line+1):
            if i == 0 or i == line:
                arr[line][i] = 1
            else:
                arr[line][i] = arr[line-1][i] + arr[line-1][i-1]
            print(arr[line][i] , end=' ')
        print()
n = int(input())
pascaltriangle(n)