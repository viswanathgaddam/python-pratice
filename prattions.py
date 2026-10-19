
#A
'''
for i in range (5):
    for j in range(5):
        if i==0 or j==0 or j==4 or i==2:
            print("*",end=" ")
        else:
            print(" ",end=" ")
    print("")
'''
#B
'''
for i in range (5):
    for j in range(5):
        if i==0 or j==0 or j==4 or i==2 or i==4:
            print("*",end=" ")
        else:
            print(" ",end=" ")
    print("")
'''

#C
'''
for i in range (5):
    for j in range(5):
        if i==0 or j==0 or i==4:
            print("*",end=" ")
        else:
            print(" ",end=" ")
    print("")
'''''

#D
'''
for i in range (5):
    for j in range(5):
        if i==0 or j==2 or j==4 or i==4:
            print("*",end=" ")
        else:
            print(" ",end=" ")
    print("")
'''
#E
'''
for i in range (5):
    for j in range(5):
        if i==0 or j==0 or i==4 or i==2:
            print("*",end=" ")
        else:
            print(" ",end=" ")
    print("")
'''
    

#f
'''
for i in range (5):
    for j in range(5):
        if i==0 or j==0  or i==2:
            print("*",end=" ")
        else:
            print("",end=" ")
    print("")
'''
#G
'''
for i in range (5):
    for j in range(5):
        if i==0 or j==0 or i==4 or (j==4 and i!=2) or (i==3 and j!=1):
            print("*",end=" ")
        else:
            print(" ",end=" ")
    print("")
'''

#H
'''
for i in range (5):
    for j in range(5):
        if j==0 or i==2 or j==4:
            print("*",end=" ")
        else:
            print(" ",end=" ")
    print("")
'''
#I
'''
for i in range (5):
    for j in range(5):
        if i==0 or i==4 or j==2:
            print("*",end=" ")
        else:
            print(" ",end=" ")
    print("")
'''
#J
'''
for i in range (5):
    for j in range(5):
        if i==0 or j==2 or (i==4 and j!=4 and j!=3) :
            print("*",end=" ")
        else:
            print(" ",end=" ")
    print("")
'''
#k
'''
for i in range(5):
    for j in range(5):
        if j==0 or (i + j == 4 and i <= 2) or (i - j == 0 and i >= 2):
            print("*",end=" ")
        else:
            print(" ",end=" ")
    print("")
'''
#L
'''
for i in range (5):
    for j in range(5):
        if i==4 or j==0:
            print("*",end=" ")
        else:
            print(" ",end=" ")
    print("")
'''
#M not comming
'''
for i in range(5):
    for j in range(5):
        if j == 0 or j == 4 or (i == j and i <= 2) or (i + j == 4 and i <= 2):
            print("*", end=" ")
        else:
            print(" ", end=" ")
    print()
'''
# N
'''
for i in range(5):
    for j in range(5):
        if j == 0 or j == 4 or i == j:
            print("*", end=" ")
        else:
            print(" ", end=" ")
    print()
'''

#O
'''
for i in range (5):
    for j in range(5):
        if i==0 or i==4 or j==0 or j==4:
            print("*",end=" ")
        else:
            print(" ",end=" ")
    print("")
'''
#P not comming
'''
for i in range(5):
    for j in range(5):
        if j == 0 or (i == 0 or i == 2) and j < 4 or (j == 4 and i == 1):
            print("*", end=" ")
        else:
            print(" ", end=" ")
    print()
'''

# q not comming
'''
for i in range(5):
    for j in range(5):
        if ((i == 0 and j < 4) or
            (i == 4 and j < 4) or
            (j == 0 and i < 4) or
            (j == 3 and i < 4) or
            (i == j and i >= 2)):
            print("*", end=" ")
        else:
            print(" ", end=" ")
    print()
'''
# R not coming
'''
for i in range(5):
    for j in range(5):
        if (j == 0 or
            (i == 0 and j < 4) or
            (i == 2 and j < 4) or
            (j == 4 and i == 1) or
            (i - j == 1 and i >= 3)):
            print("*", end=" ")
        else:
            print(" ", end=" ")
    print()
'''
#s not comming
'''
for i in range(5):
    for j in range(5):
        if (i == 0 or i == 2 or i == 4) and j < 5:
            print("*", end=" ")
        elif j == 0 and i == 1:
            print("*", end=" ")
        elif j == 4 and i == 3:
            print("*", end=" ")
        else:
            print(" ", end=" ")
    print()
'''
#T
'''
for  i in range (5):
    for j in range(5):
        if i==0 or j==2:
            print("*",end=" ")
        else:
            print(" ",end=" ")
    print("")
'''
#U
'''
for i in range (5):
    for j in range(5):
        if i==4 or j==4 or j==0:
            print("*",end=" ")
        else:
            print(" ",end=" ")
    print("")
'''
#V
'''
for i in range(5):
    for j in range(9):
        if j == i or j == 8 - i:
            print("*", end=" ")
        else:
            print(" ", end=" ")
    print()
'''

#W
'''
for i in range (5):
    for j in range(5):
        if j==0 or j==2 or j==4 or i==4:
            print("*",end=" ")
        else:
            print(" ",end=" ")
    print("")
'''
#x
'''
for i in range(5):
    for j in range(5):
        if i == j or i + j == 4:
            print("*", end=" ")
        else:
            print(" ", end=" ")
    print()
'''

#y not comming
'''
for i in range(5):
    for j in range(5):
        if (i == j and j!=3 and j!=4)  or i + j == 4:
            print("*", end=" ")
        else:
            print(" ", end=" ")
    print()
'''
#z not comming
'''
for i in range(5):
    for j in range(5):
        if i==0 or i==4 or i + j == 4 :
            print("*",end=" ")
        else:
            print(" ",end=" ")
    print()
'''
'''
n="viswa"
for i in range (1,len(n)+1):
    print(n[:i])
'''

#vowels and consonants in list
'''
name=input("enter any name")
v=[]
c=[]
for ch in name:
    if ch.lower() in "aeiou":
        v.append(ch)
    elif ch.isalpha():
        c.append(ch)
print("vowels ",v)
print("vowel count ", len(v))
print("consonants ",c)
print("consonant count ",len(c))
'''
#leap year and non leape year
'''
years = [2000, 2003, 2004, 1990]

leap_years = []
non_leap_years = []

for year in years:
    if year % 400 == 0 or (year % 4 == 0 and year % 100 != 0):
        leap_years.append(year)
    else:
        non_leap_years.append(year)

print("Leap years:", leap_years)
print("Non-leap years:", non_leap_years)
'''
'''
n = int(input("Enter a number: "))

if n <= 1:
    print(n, "is not a prime number")
else:
    prime = True

    for i in range(2, n):
        if n % i == 0:
            prime = False
            break

    if prime:
        print(n, "is a prime number")
    else:
        print(n, "is not a prime number")

'''
'''
n=int(input())
count=0
for number in range(1,n):
    for  i in range (2,number):
        if number%i==0:
            break
    else:
        count+=number
        #print(number)

print(count)
'''
'''
n=int(input())
for i in range (1,n,2):
    print((i*".|.").center(21,"-"))
print(("welcome").center(21,"-"))
for j in range (n-2,0,-2):
    print((j*".|.").center(21,"-"))
'''
#swathik symbol
'''

for i in range (5):
    for j in range(5):
        if i==2 or j==2 or (i==0 and j!=3 and j!=4) or (j==4 and i!=3 and i!=4) or (j==0 and i!=1) or (i==4 and i!=1 and j!=1):
            print("*",end=" ")
        else:
            print(" ",end=" ")
    print("")
'''
#print name into + formate
'''
n=str(input("enter any name: "))
v=n.upper()
for i in v:
    if i=="A":
        print(" ")
        for i in range (5):
            for j in range(5):
                if i==0 or i==2 or j==4 or j==0:
                    print("*",end=" ")
                else:
                    print(" ",end=" ")
            print("")
    if i=="B":
        print(" ")
        for i in range (5):
            for j in range(5):
                if i==0 or j==0 or j==4 or i==2 or i==4:
                    print("*",end=" ")
                else:
                    print(" ",end=" ")
            print("")
    if i=="C":
        print(" ")
        for i in range (5):
            for j in range(5):
                if i==0 or j==0 or i==4:
                    print("*",end=" ")
                else:
                    print(" ",end=" ")
            print("")
    if i=="D":
        print(" ")
        for i in range (5):
            for j in range(5):
                if i==0 or j==1 or i==4 or j==4:
                    print("*",end=" ")
                else:
                    print(" ",end=" ")
            print("")
    if i=="E":
        print(" ")
        for i in range (5):
            for j in range(5):
                if i==0 or j==0 or i==2 or i==4:
                    print("*",end=" ")
                else:
                    print(" ",end=" ")
            print("")
    if i=="F":
        print(" ")
        for i in range (5):
            for j in range(5):
                if i==0 or j==0  or i==2:
                    print("*",end=" ")
                else:
                    print(" ",end=" ")
            print("")
    if i=="G":
        print(" ")
        for i in range (5):
            for j in range(5):
                if i==0 or j==0 or i==4 or (j==4 and i!=2) or (i==3 and j!=1):
                    print("*",end=" ")
                else:
                    print(" ",end=" ")
            print("")
    if i=="H":
        print(" ")
        for i in range (5):
            for j in range(5):
                if j==0 or i==2 or j==4:
                    print("*",end=" ")
                else:
                    print(" ",end=" ")
            print("")
    if i=="I":
        print(" ")
        for i in range (5):
            for j in range(5):
                if i==0 or i==4 or j==2:
                    print("*",end=" ")
                else:
                    print(" ",end=" ")
            print("")
    if i=="J":
        print(" ")
        for i in range (5):
            for j in range(5):
                if i==0 or j==2 or (i==4 and j!=4 and j!=3):
                    print("*",end=" ")
                else:
                    print(" ",end=" ")
            print("")
    if i=="K":
        print(" ")
        for i in range (5):
            for j in range(5):
                if j==0 or (i + j == 4 and i <= 2) or (i - j == 0 and i >= 2):
                    print("*",end=" ")
                else:
                    print(" ",end=" ")
            print("")
    if i=="L":
        print(" ")
        for i in range (5):
            for j in range(5):
                if i==4 or j==0:
                    print("*",end=" ")
                else:
                    print(" ",end=" ")
            print("")
    if i=="M":
        print(" ")
        for i in range (5):
            for j in range(5):
                if j == 0 or j == 4 or (i == j and i <= 2) or (i + j == 4 and i <= 2):
                    print("*",end=" ")
                else:
                    print(" ",end=" ")
            print("")
    if i=="N":
        print(" ")
        for i in range (5):
            for j in range(5):
                if j == 0 or j == 4 or i == j:
                    print("*",end=" ")
                else:
                    print(" ",end=" ")
            print("")
    if i=="O":
        print(" ")
        for i in range (5):
            for j in range(5):
                if i==0 or i==4 or j==0 or j==4:
                    print("*",end=" ")
                else:
                    print(" ",end=" ")
            print("")
    if i=="P":
        print(" ")
        for i in range (5):
            for j in range(5):
                if j == 0 or (i == 0 or i == 2) and j < 4 or (j == 4 and i == 1):
                    print("*",end=" ")
                else:
                    print(" ",end=" ")
            print("")
    if i=="Q":
        print(" ")
        for i in range (5):
            for j in range(5):
                if ((i == 0 and j < 4) or
            (i == 4 and j < 4) or
            (j == 0 and i < 4) or
            (j == 3 and i < 4) or
            (i == j and i >= 2)):
                    print("*",end=" ")
                else:
                    print(" ",end=" ")
            print("")
    if i=="R":
        print(" ")
        for i in range (5):
            for j in range(5):
                if (j == 0 or
            (i == 0 and j < 4) or
            (i == 2 and j < 4) or
            (j == 4 and i == 1) or
            (i - j == 1 and i >= 3)):
                    print("*",end=" ")
                else:
                    print(" ",end=" ")
            print("")
    if i=="S":
        print(" ")
        for i in range(5):
            for j in range(5):
                if (i == 0 or i == 2 or i == 4) and j < 5:
                    print("*", end=" ")
                elif j == 0 and i == 1:
                    print("*", end=" ")
                elif j == 4 and i == 3:
                    print("*", end=" ")
                else:
                    print(" ", end=" ")
            print()
    if i=="T":
        print(" ")
        for i in range (5):
            for j in range(5):
                if i==0 or j==2:
                    print("*",end=" ")
                else:
                    print(" ",end=" ")
            print("")
    if i=="U":
        print(" ")
        for i in range (5):
            for j in range(5):
                if i==4 or j==4 or j==0:
                    print("*",end=" ")
                else:
                    print(" ",end=" ")
            print("")
    if i=="V":
        print(" ")
        for i in range(5):
            for j in range(9):
                if j == i or j == 8 - i:
                    print("*", end=" ")
                else:
                    print(" ", end=" ")
            print()
    if i=="W":
        print(" ")
        for i in range(5):
            for j in range(5):
                if j==0 or j==2 or j==4 or i==4:
                    print("*", end=" ")
                else:
                    print(" ", end=" ")
            print()
    if i=="X":
        print(" ")
        for i in range(5):
            for j in range(5):
                if i==j or i+j==4:
                    print("*", end=" ")
                else:
                    print(" ", end=" ")
            print()
    if i=="Y":
        print(" ")
        for i in range(5):
            for j in range(5):
                if (i==j and j!=4 and j!=3) or i+j==4:
                    print("*", end=" ")
                else:
                    print(" ", end=" ")
            print()
    if i=="Z":
        print(" ")
        for i in range(5):
            for j in range(5):
                if i+j==4 or i==0 or i==4:
                    print("*", end=" ")
                else:
                    print(" ", end=" ")
            print()
'''
    
    
            
        
        
        






    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    