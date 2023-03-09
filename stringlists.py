'''
Ask the user for a string and print out
whether this string is a palindrome or not. (same forwards and backwards)
'''
'''
Option to reverse -- each letter is iterated and then new characters are added in front
def reverse(s):
    str = ""
    for i in s:
        str = i + str
    return str

s = input("Say something: ")
print(reverse(s))
'''
str = input("Say something: ")

def palindrome(str):
    if str == str[::-1]:
        return True
    else:
        return False

print(palindrome(str))