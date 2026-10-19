#if Statement Questions:
#Write a program to check if a number is greater than 10.
'''
n=int(input("enter any number: "))
if n>10:
    print("given number greater than 10")
elif n==10:
    print("given number equal to 10")
else:
    print("given number is less than 10")
'''
#Write a program to check if a person is eligible to vote (age 18 or above).
'''
age=int(input("enter your age: "))
if age>=18:
    print("you are eligible to vote")
else:
    print("you are not eligible to vote")
'''
#Write a program to check if a number is positive.
'''
n=int(input("enter any number: "))
if n>=1:
    print("given number is positive")
elif n==0:
    print("given number is 0")
else:
    print("given number is negitive")
'''
#Write a program to check if a number is negative.
'''
n=int(input("enter any number: "))
if n>=1:
    print("given number is not negitive")
elif n==0:
    print("given number is 0")
else:
    print("given number is negitive")
'''
#if-else Statement Questions
#Write a program to check if a number is even or odd.
'''
n=int(input("enter any number: "))
if n%2==0:
    print("given number is even")
else:
    print("given number is odd")
'''
#Write a program to check if a person is eligible for a driving license (age 18 or above).
'''
age=int(input("enter your age: "))
if age>=18:
    print("you are eligible for licence")
else:
    print("you are not eligible for licence")
'''
#Write a program to check if a student passed or failed based on marks (Pass: 40+, Fail: below 40).
'''
m=float(input("enter marks: "))
if m>=40:
    print("pass")
elif m<=39 and m>=0:
    print("fail")
elif m>=101:
    print("out of range")
else:
    print("give valied marks")
'''
#if-elif-else Statement Questions
#write a program to categorize a person’s age as a child (0-12), teenager (13-19), or adult (20+).
'''
age=int(input("enter your age: "))
if age<=12:
    print("child")
elif age>=13 and age<=19:
    print("teen")
elif age>=20:
    print("adult")
'''
#Write a program to determine the grade of a student based on marks (A: 90+, B: 80+, C: 70+, D: 60+, Fail: <40).
'''
m=float(input("enter marks: "))
if m>=90 and m<=100:
    print("A")
elif m>=80 and m<=89:
    print("B")
elif m>=70 and m<=79:
    print("C")
elif m>=60 and m<=69:
    print("D")
elif m>=41 and m<=59:
    print("E")
elif m<=40 and m>=0:
    print("F")
else:
    print("enter valied marks out of 100")
'''
#Nested_if statements:
#A bank checks if a person is eligible for a loan based on their age and salary.
'''
a=int(input("enter your age: "))
if a>=21:
    s=int(input("enter your salary: "))
    if s>=50000:
        b=int(input("enter your cible score: "))
        if b>750:
            print("you are eligibul for loan")
        else:
            print("cible  score must be above 750")
    else:
        print("salary must be above 50000")
        
else:
    print("age must be aboue 21")
'''
#A student needs at least 35 marks to pass. If they score above 90, they get a scholarship.
'''
m=int(input("enter marks: "))
if m<35:
    print("fail")
elif m>=35 and m<=100:
    print("pass")
    if m>90:
        print("scholarship")
'''
#Real time
#E-commerce Platforms (Amazon, Flipkart, eBay)
#Order Discounts & Shipping Charges
'''
a=int(input("enter order amount: "))
if a>500:
    print("free shipping")
elif a<=499:
    print("add shipping cost")
'''
#Surge Pricing Logic
'''
print("type yes or no")
p=input("is it peack hour: ")
d=input("is it high demand: ")
if p=="yes" and d=="yes":
    print("apply surge price")
else:
    print("no surge price")
'''
#Restaurant Order Availability
'''
item=["idle","dosa","puri","chapathi"]
o=input("is restorent open (yes/no): ")
if o=="yes":
    print(item)
    i=input("order your item: ")
    if i in item:
        print("item available")
        print("order placed")
    else:
        print("item not available")
else:
    print("restorent is colsed")
'''
#Video Quality Adjustment
'''
q=int(input("enter internet speed in Mbps: "))
if q>=10 :
    print("1080p")
elif q>=5:
    print("720p")
else:
    print("480p")
'''
#Practice programs: # medium_level
#Scenario: A system checks if a user is eligible for a senior citizen discount (age ≥ 60).
'''
a=int(input("enter age: "))
if a>=60:
    print ("senior citizen")
elif a>=0 and a<=59:
    print ("not a senior citizen")
else:
    print("enter valible age")
'''
#📌 Scenario: A system classifies water usage based on liters used.
'''
i=int(input("how many liters used: "))
if i>0 and i<=100:
    print("low usage")
elif i>=101 and i<=500:
    print("moderate usage")
elif i>500:
    print("high usage")
'''
#📌 Scenario: A movie booking system checks age and ticket availability.
'''
a=int(input("enter age: "))
if a>=18:
    c=input("enter seate avable or not (yes/no): ")
    if c=="yes":
        print("seat is avaible")
    else:
        print("seats are not avaible")
else:
    print("age must be above 18")
'''










































