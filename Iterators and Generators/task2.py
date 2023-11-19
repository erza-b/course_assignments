#Task 2

#Create your own implementation of a built-in function range(), named in_range(), which takes three parameters: start, end, and optional step. Tips: See the documentation for range() function

def in_range(start,end,step=1):
    if not all(isinstance(arg,int)for arg in (start,end,step)):
        raise TypeError("Arguments must be integers")
    if step==0:
        raise ValueError("Step cannot be zero")
    result=[]
    current=start

    while(step>0 and current <end) or(step<0 and current>end):
        result.append(current)
        current+=step

    return result

print(in_range(1, 5))       
print(in_range(1, 10, 2))     
print(in_range(5, 1, -1))