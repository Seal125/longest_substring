'''
PEDAC Process

P - Find the longest substring in the string given, and return its length

E - print(longest_substring('abcdedef') == 5)
    print(longest_substring('bbbbbb') == 1)
    print(longest_substring('acdfdv') == 4)

D - List

A -
    1. Create empty list
    2. Loop through entire string
      a. If the letter in the string is in the list, continue on
      b. If the letter in the string is not in the list, add the letter to the list
    3. Return the length of the list
'''

def longest_substring(string):

    subtring = []

    for letter in string:
        print(letter)
        print(substring)
        print(len(substring))
        if letter in substring:
            substring.clear()
        if letter not in substring:
            substring.append(letter)

    return len(substring)

print(longest_substring('abcdedef') == 5)
print(longest_substring('bbbbbb') == 1)
print(longest_substring('acdfdv') == 4)
print(longest_substring('pwwkew') == 3)
print(longest_substring('abcdefghi') == 9)