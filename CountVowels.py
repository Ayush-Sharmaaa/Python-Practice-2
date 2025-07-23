def count_vowels(text):
    vowels="aeiouAEIOU"
    count = 0
    for char in text:
        if char in "aeiouAEIOU":
            count += 1
    return count
str=input("Enter a string: ")
print("Total number of vowels: ", count_vowels(str))

