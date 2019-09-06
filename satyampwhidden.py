
def extractMaximum(ss): 
    num, res = 0, 0
    
      
    # start traversing the given string  
    for i in range(len(ss)): 
          
        if ss[i] >= "0" and ss[i] <= "9": 
            num = num * 10 + int(int(ss[i]) - 0) 
        else: 
            res = max(res, num) 
            num = 0
          
    return max(res, num)

    
print(extractMaximum(input()))
