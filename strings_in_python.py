#Programs on strings:
#Replace all occurrences of "a" with "@" in a given string.
'''
n=input("enter any string: ")
print(n.replace("a","@"))
'''
#Write a program to print the first and last character of a given string.
'''
n=input("enter any string: ")
print(n[0])
print(n[-1])
'''
#Write a program to convert a string to uppercase and lowercase.
'''
n=input("enter any string: ")
print(n.upper())
print(n.lower())
'''
#Write a program to remove all spaces from a given string.
'''
n=input("enter any string: ")
v="   mi   "
s=n.strip()
print(s)
print(v.strip())
'''
#Check if the word "Python" exists in the given sentence.
'''
w= "i am learnig python"
if "python" in w:
    print("present")
else:
    print("not present")
'''
#Print the first three characters of a given string.
'''
s=input("enter any string: ")
print(s[0:3:1])
'''
#Take two strings as input and merge them.
'''
s1=input("enter first string: ")
s2=input("enter second string: ")
v=s1+s2
print(v)
'''
#Write a program to check if a string contains only numbers.
'''
n=input("enter any string: ")
j=n.isdecimal()
print(j)
'''
#Remove all occurrences of "e" from a string.
'''
n=input("enter any string: ")
k=n.replace("e","")
print(k)
'''
#Count how many times the letter 'o' appears in a given string.
'''
n=input("enter any string: ")
h=n.count("o")
print(h)
'''
#Medium_level:
#Check if a username contains only letters and numbers
#An email has "@" and ends with ".com".
'''
e=input("enter e mail id: ")
if (e.endswith("@gmail.com"))==True:
    print("email accepected")
else:
    print("give correct email id")
'''
#Ensure a password contains at least 8 characters, a number, and a special character.
'''
p=input("enter password: ")

if len(p) >= 8 and any(ch.isdigit() for ch in p) and any(not ch.isalnum() for ch in p):
    print("Valid Password")
else:
    print("Invalid Password")
'''
#Write a program to find the length of a given string without using len().
'''
n=input("enter any string: ")
count=0
for i in (n):
    count+=1
print(count)
'''
#Write a Python program to reverse a given string.
'''
s=input("enter any string: ")
v=s[::-1]
print(v)
'''
#Count Vowels in a String
'''
s=input("enter any string: ")
o=["a","e","i","o","u"]
a=0
count=0
for i in s:
    if i in o:
        count+=1
    else:
        a+=1
print(count)
print(a)
'''








