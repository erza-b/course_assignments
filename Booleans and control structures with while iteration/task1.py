#Task 1
# String manipulation
# Write a Python program to get a string made of the first 2 and the last 2 chars from a given string.
# If the string length is less than 2, return an empty string.
# Sample String: 'helloworld'
# Expected Result: 'held'
# Sample String: 'my'
# Expected Result: 'mymy'
# Sample String: 'x'
# Expected Result: Empty String
# Tips:
# - Use the built-in function len() on an input string.
# - Use positive indexing to get the first characters of a string and negative indexing to get the last characters.

sampleString = "helloworld"

if len(sampleString) < 2:
    print(" ")
else:
    concatString = sampleString[0:2]+sampleString[-2:]
    print(concatString)
