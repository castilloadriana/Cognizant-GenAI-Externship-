# Task 1 - String Slicing and Indexing
sentence= "Python is amazing!"



print("First word: ", sentence[0:7])
print("Amazing part: ", sentence[10:17])
print("Reversed string: ", sentence[::-1])


#Task 2 - String Methods
value= " hello, python world! "
print(value.strip())
print(value.capitalize())
print(value.replace("world", "universe"))
print(value.upper())

#Task 2 - Check for Palindromes
word= input("Enter a word: ")
word2= word[::-1]
if (word == word2):
    print("Yes, '",word, "' is a palindrome!")




