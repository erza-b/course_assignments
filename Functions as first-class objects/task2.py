#Task 2

#Write a Python program to access a function inside a function (Tips: use function, which returns another function)

def first_function(message):
    def second_function():
        print(message)
    
    return second_function


my_var = first_function("Hello from the second function!")


my_var()
