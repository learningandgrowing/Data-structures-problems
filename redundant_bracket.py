def checkredundant(str):
    count = 0
    s = []
    for i in str:
        if i != ')':
    
            s.append(i)
            
    
        if (i == ')') :
            while s[-1] != '(':
                s.pop()
                count += 1
            s.pop()
            if count == 0 or count == 1:
                return 'true'
            
        count = 0
    return 'false'
        
    
      
           
                
                
                
                
            #if count == 0 or count == 1:
                #return 'true'
        #count = 0
    #return 'false'
str = input()
print(checkredundant(str))
    
    