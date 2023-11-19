#Task3
#Create your own implementation of an iterable, which could be used inside for-in loop. Also, add logic for retrieving elements using square brackets syntax

class MyIterable:
    def __init__(self,data):
        self.data=data
        self.index=0

    def __iter__(self):
        return self
    
    def __next__(self):
        if self.index<len(self.data):
            result=self.data[self.index]
            self.index+=1
            return result
        else:
            raise StopIteration
        
    def __getitem__(self,index):
        if 0<=index<len(self.data):
            return self.data[index]
        else:
            raise IndexError("Index out of range")
        

my_iterable=MyIterable([1,2,3,4,5])

print("For loop:")
for item in my_iterable:
    print(item)
print("Square bracket syntax:")
print(my_iterable[2])
