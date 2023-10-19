#Task 1

#Make a program that has some sentence (a string) on input and returns a dict containing all unique words as keys and the number of occurrences as values. 




sentence = input("Enter a sentence: ")

words = sentence.split()
word_count = {}

for word in words:
    word = word.strip('.,?!').lower()
    if word in word_count:
        word_count[word] += 1
    else:
        word_count[word] = 1

print("Word count:")
for word, count in word_count.items():
    print(f"{word}: {count}")
