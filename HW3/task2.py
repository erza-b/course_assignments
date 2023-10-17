# Task 2
# The valid phone number program.
# Make a program that checks if a string is in the right format for a phone number.
# The program should check that the string contains only numerical characters and is only 10 characters long.
# Print a suitable message depending on the outcome of the string evaluation.



phoneNumber = "0498877788"
if phoneNumber.isnumeric() and len(phoneNumber) == 10:
    print("Numri juaj eshte ne rregull!")
else:
    print("Numri nuk eshte ne rregull,ju lutem rishikojeni")
