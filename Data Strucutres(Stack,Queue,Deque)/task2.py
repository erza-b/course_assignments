#Task2
#Write a program that reads in a sequence of characters, and determines whether it's parentheses, braces, and curly brackets are "balanced."



def is_balanced(expression):
    stack = []
    opening_brackets = {'(', '[', '{'}
    closing_brackets = {')': '(', ']': '[', '}': '{'}

    for char in expression:
        if char in opening_brackets:
            stack.append(char)
        elif char in closing_brackets:
            if not stack or stack.pop() != closing_brackets[char]:
                return False

    return not stack  


if __name__ == "__main__":
    user_input = input("Enter a sequence of characters: ")
    if is_balanced(user_input):
        print("The sequence is balanced.")
    else:
        print("The sequence is not balanced.")
