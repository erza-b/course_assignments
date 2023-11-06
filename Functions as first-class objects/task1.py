#Task 1

#Write a Python program to detect the number of local variables declared in a function.


def count_local_variables():
    a = 1
    b = 'hello'
    c = [1, 2, 3]
    d = {'name': 'Erza'}
    
     
    return len(locals())

num_locals = count_local_variables()
print(f"Number of local variables in the function: {num_locals}")
