#Task 1

#Create your own implementation of a built-in function enumerate, named with_index(), which takes two parameters: iterable and start, default is 0. Tips: see the documentation for the enumerate function

def with_index(iterable, start=0):
  
    index = start
    for value in iterable:
        yield index, value
        index += 1


my_list = ['apple', 'banana', 'cherry']

for index, value in with_index(my_list, start=1):
    print(f"Index: {index}, Value: {value}")
