"""
3)	Write a function to find whether 2 words or anagrams. 
Ex: silent , listen - anagram
dad , bad - not an anagram

"""

def sorting_string(string):
    sorted_string = ''.join(sorted(list(string.lower().replace(" ", ""))))
    return(sorted_string)

str1=sorting_string(input("enter the frist word:"))
str2=sorting_string(input("enter the second word:"))
if str1 == str2:
    print("it is an anagram")
else:
    print("it is not an anagram")