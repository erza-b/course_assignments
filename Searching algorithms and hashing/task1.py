#Task 1

#Implement binary search using recursion.

def binary_search_recursive(arr,low,high,target):
    if low<=high:
        mid=(low+high)//2

        if arr[mid]==target:
            return mid
        elif arr[mid]>target:
            return binary_search_recursive(arr,low,mid-1,target)
        else:
            return binary_search_recursive(arr,mid+1,high,target)
    else:
        return -1
    
arr = [1, 2, 3, 4, 5, 6, 7, 8, 9]
target = 6
result = binary_search_recursive(arr, 0, len(arr) - 1, target)

if result != -1:
    print(f"Element {target} is present at index {result}")
else:
    print(f"Element {target} is not present in the array")
    