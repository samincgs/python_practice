# Palindrome Checker: Write a function to check if a given string is a palindrome.

def palindrome_checker(word):
    print('The word is:', word)
    single_letters = list(word.lower())
    half = len(single_letters) // 2
    
    if len(single_letters) % 2 == 1:
        a = single_letters[:half]
        b = single_letters[half + 1:][::-1]
    else:
        a = single_letters[:half]
        b = single_letters[half:][::-1]
    
    if a == b:
        return "It is a palindrome"
    
    return "It is a not palindrome"
    
# test cases
print(palindrome_checker('Noon'))
print(palindrome_checker('Racecar'))
print(palindrome_checker('Level'))
print(palindrome_checker('Python'))
print(palindrome_checker('Madam'))
print(palindrome_checker('Palindrome'))

