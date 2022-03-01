#A
def my_func(x1, x2, x3):
    try:
        x1=float(x1)
        x2=float(x2)
        x3=float(x3)
        denominator= (x1+x2+x3)
    except:
        return('Error: parameters should be float')
    
    if(denominator==0):
        return('Not a number – denominator equals zero')
    
    result=((x1+x2+x3)*(x2+x3)*x3)/denominator
    return(result)



print(my_func(8,73,-3))


#B
def  convert(hours, minutes=0):
    try:
        hours=float(hours)
        minutes=float(minutes)
    except:
        return('Input error!')
    if(hours<0 or minutes<0):
      return('Input error!')   
    
    sec=int(hours*3600+minutes*60)
    return(sec)

print(convert(1,3))
print(convert(1.75))