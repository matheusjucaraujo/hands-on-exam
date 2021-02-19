def isPalindrome(word):
    return word == word[::-1]
word = input(" Type the word to check if it's a palindrome:")
answer = isPalindrome(word)
 
if answer:
    print("Yes")
else:
    print("No")