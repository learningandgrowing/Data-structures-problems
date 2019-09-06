def combinations(a, l, r): 
    if l == r: 
        print(''.join(a))
    else: 
        for i in range(l, r + 1): 
            a[l], a[i] = a[i], a[l] 
            combinations(a, l + 1, r) 
            a[l], a[i] = a[i], a[l]
  
s = "HISTORY"
n = len(s) 
a = list(s) 
combinations(a, 0, n-1)