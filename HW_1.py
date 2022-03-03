#A
def my_func1(x1, x2, x3):
    if(isinstance(x1, float ) and isinstance( x2, float ) and isinstance( x3, float )):
        denominator= (x1+x2+x3)
        if(denominator==0):
            return('Not a number – denominator equals zero')
        result=((x1+x2+x3)*(x2+x3)*x3)/denominator
        return(result)
    else:
        return('Error: parameters should be float')

print(my_func1(9.0,3.0,8.0))

print(my_func1('VV',3.0,8.0))


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
print(convert(1,9.9))