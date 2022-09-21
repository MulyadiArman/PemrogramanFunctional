from math import fabs


word = "madam"

def is_palindrom(word):
    return word == word[::-1]

print("is palindrom", is_palindrom(word))

def is_palindromm2(word):
    return word ==''.join(reversed(word))

def is_palindrom3(word):
    for i in range(len(word)//2):
        if word[i] != word[-l-i]:
            return False
    return True

