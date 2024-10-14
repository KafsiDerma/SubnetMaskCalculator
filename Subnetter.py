# okay , we give wack, then get subnet mask, more features in future


def num_input(num):

    numberofbytes= num//8
    
    
    
    
    if num%8 == 0:
    
        return "255."*(numberofbytes-1)+"255"
        
    else:
    
        
        stringof255 = "255."*numberofbytes
        
        stringof0s = ".00"*(numberofbytes-3)
        
        loop = num%8
        numberofmask = ''
        valueformask = 0
        
        for x in range(7,7-loop,-1):
        
            valueformask += 2**x
            
        
        return stringof255+str(valueformask)+stringof0s
            