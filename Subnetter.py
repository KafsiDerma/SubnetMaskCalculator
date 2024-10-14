# okay , we give wack, then get subnet mask, more features in future


def num_input(input_num):


    num = int(input_num)
    numberofbytes= num//8
    
    
    
    
    if num%8 == 0:
    
        return "255."*(numberofbytes-1)+"255" + ".00"*(4-numberofbytes)
        
    else:
    
        
        stringof255 = "255."*numberofbytes
        
        stringof0s = ".00"*(3-numberofbytes)
        
        loop = num%8
        numberofmask = ''
        valueformask = 0
        
        for x in range(7,7-loop,-1):
        
            valueformask += 2**x
            
        
        return stringof255+str(valueformask)+stringof0s
        
        

def main():

    x = str(100)
    while x is not str(99):
    
        x = input("please enter /X number  ...")
        
        print(num_input(x))
    
    
    
    
    
# where the magic happens
main()