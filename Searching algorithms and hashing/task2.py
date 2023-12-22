#Task 2

#Read about the Fibonacci search and implement it using python. Explore its complexity and compare it to sequential, binary searches.

def fibonacci_search(arr, target):
    fib_m_minus_2 = 0
    fib_m_minus_1 = 1
    fib = fib_m_minus_1 + fib_m_minus_2

    while fib < len(arr):
        fib_m_minus_2 = fib_m_minus_1
        fib_m_minus_1 = fib
        fib = fib_m_minus_1 + fib_m_minus_2

    offset = -1

    while fib > 1:
        i = min(offset + fib_m_minus_2, len(arr) - 1)

        if arr[i] < target:
            fib = fib_m_minus_1
            fib_m_minus_1 = fib_m_minus_2
            fib_m_minus_2 = fib - fib_m_minus_1
            offset = i

        elif arr[i] > target:
            fib = fib_m_minus_2
            fib_m_minus_1 = fib_m_minus_1 - fib_m_minus_2
            fib_m_minus_2 = fib - fib_m_minus_1

        else:
            return i

    if fib_m_minus_1 and arr[offset + 1] == target:
        return offset + 1

    return -1



arr = [1, 2, 3, 4, 5, 6, 7, 8, 9]
target = 6

result = fibonacci_search(arr, target)

if result != -1:
    print(f"Element {target} is present at index {result}")
else:
    print(f"Element {target} is not present in the array")
