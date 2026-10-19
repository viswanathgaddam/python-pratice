#Print numbers from 1 to 10 using a for loop.
'''
for i in range(1,11,1):
    print(i,end="")
'''
'''
i=1
while i<=10:
    print(i,end="")
    i+=1
'''
#Print numbers from 10 to 1 using a while loop.
'''
n=10
while n>=1:
    print(n)
    n-=1
'''
'''
for i in range(10,0,-1):
    print(i,end=" ")
'''
#Print all even numbers from 1 to 20.
'''
for i in range(1,21,1):
    if i%2==0:
        print(i)
'''
'''
n=0
while n<=20:
    n+=1
    if n%2==0:
    print(n)
'''
#Print the sum of the first 10 natural numbers.
'''
n=0
for i in range (1,11,1):
    n=n+i
print(n)
'''
'''
n=0
v=0
while n<=10:
    v=v+n
    n+=1
print(v)
'''
#Print the multiplication table of a given number.
'''
n=int(input("enter any number: "))
for i in range(1,11,1):
    print(n,"x",i,"=",n*i)
'''
'''
v=int(input("enter any number: "))
n=1
c=1
while n<=10:
    c=v*n
    print(v,"x",n,"=",c)
    n+=1
'''
#Find the factorial of a given number using a while loop.
'''
k=1
v=int(input("enter any number: "))
n=1
while n<=v:
    k=k*n
    n+=1
print(k)
'''
'''
v=int(input("enter any number: "))
k=1
for i in range (1,v+1,1):
    k=k*i
print(k)
'''
#Check if a number is prime or not.
'''
n=int(input("enter any number: "))
for i in range(2,n,1):
    if n%2==0:
        print("not a prime number")
        break
else:
    print("prime number")
'''
'''
n=int(input("enter any number: "))
k=2
while k<n-1:
    if n%2==0:
        print("not a prime number")
        k+=1
        break
    else:
        print("prime number")
        break
'''
#Find the sum of digits of a given number
'''
n=input("enter any number")
k=0
for i in n:
    k=k+int(i)
print(k)
'''
#Print all odd numbers from 1 to 50
'''
for i in range(1,51,1):
    if i%2!=0:
        print(i,end=" ")
'''
'''
n=0
while n<=50:
    if n%2!=0:
        print(n,end=" ")
    n+=1    
'''
#Find the largest number in a list using a loop.
'''
l=list(map(int,input("entera list of numbers: ").split(" ")))
m=l[0]
for i in l:
    if i>m:
        m=i
print(m)
'''
'''
l=list(map(int,input("entera list of numbers: ").split(" ")))
m=l[0]
k=0
i=1
while i>=k:
    k=i
    i+=1
print(k)
'''
#Print all numbers from 1 to 100 that are divisible by 5.
'''
for i in range(1,101,1):
    if i%5==0:
        print(i,end=" ")
'''
'''
n=1
while n<=100:
    if n%5==0:
        print(n,end=" ")
    n+=1
'''

#pratice queshions
'''

toys=input("enter toy type(battery/wire/wireless): ")
price=int(input("enter toy price: "))
if toys=="wireless":
    if price >2000:
        discount=price*5/100
        final_price=price-discount
        print("discount:",discount)
        print("final price:",price)
    else:
        print("final price:", price)
elif toys=="wire:":
    if price >=1000:
        price("your get 2 extra toys")
    elif price>=500:
        print("you get one extra toy")
    else:
        print("no extra toy")
    print()
'''
'''

toy=input("battery or wire or wireless")
bill=int(input())
paidamount=bill
if toy =="battery":
    if bill>500:
        paidamount=price-(5/100)*price
        print(paidamount)
    else:
        print(paidamount)
elif toy=="wire":
    if bill>500:
        freetoy
'''
'''
x=["ram","sham","raj","sai","john"]
search=input("enter name: ")
if search in x:
    print("available")
else:
    print("not available")
'''
'''
d={101:["john",18], 102:["sai",22]}
print(d.keys())
print(d.values())
print(d.items())
search=102
if search in d:
    print(d[search])

print(d.get(102))#no error trown
'''
'''
for i in range(10,11,1):
    print(i)
'''
'''
print(30,20,1)
for (30,20,1)
print(1,50,5)
for (1,50,5)
print(17)
for(17)
'''
'''
#even numbers
for i in range(2,21,2):
    print(i)
'''
'''
# sum of first 10 numbers
n=0
for i in range (1,11,1):
    n=n+i
print(n)
'''

'''
#nultiplication of given sumber
n=int(input("enter any number"))
m=n

for i in range(1,11):
    print(m,"x",i,"=",n*i)
'''
'''
n=int(input("entr any number: "))
for i in range(1,11):
    print(n,"x",i,"=",n*i)
'''
'''
n=int(input("enter any number"))
f=1
i=1
while(i<=n):
    f=f*i
    i=i+1
print(f)
'''
'''
n=int(input("enter any number "))
if n<=1:
    print(n, "is not a prime number")
else:
    for i in range(2,n):
        if n%i==0:
            print(n, " is not a prime number")
            break
    else:
        print(n, "is a prime number")
'''
'''
l=[1,3,2,5,7,9,8]
empty=[]
for i in range(len(l)):
    if i%2==0:
        empty.append(l[i])
        print(empty)
print(empty)
'''
'''
l=[1,3,2,5,7,9,8]
empty=[]
for i in range(len(l)):
    if i%2==0:
        if l[i]%2!=0:
            print(l[i])
        #empty.append(l[i])
            #print(empty)
'''
'''
l=[1,3,2,5,7,9,8]
empty=[]
for i in range(len(l)):
    print(l[i]**2)


##    if i%2==0:
##        if l[i]%2!=0:
##            print(l[i])
##        #empty.append(l[i])
##            #print(empty)
'''
'''
l=[1,3,2,5,7,9,8]
empty=[]
for i in range(len(l)):
    print(l[i]**2)
'''
'''
l=[1,3,2,5,7,9,8]
empty=[]
for i in l:
    if i%2!=0:
        empty.append(i+10)
    else:
        empty.append(i)
print(empty)

'''
'''
l=[1,3,2,5,7,9,8]
l.reverse()
print(l)
'''
'''
l=[1,3,2,5,7,9,8]
empty=[]
for i in range(len(l)-1,-1,-1):
    empty.append(l[i])
print(empty)
'''
'''
l=[1,3,2,5,7,9,8]
empty=[]
for i in range(len(l)-1,-1,-1):
    empty.insert(0,l[i])
    print(empty)
'''
'''
#
l=["mohan","sravya","pavani","babu","laysa"]
search=input("enter any name: ")
for i in l:
    if i==search:
        print("available")
        break
else:
    print("not available")

'''
''' 
l=["mohan","sravya","pavani","babu","lasya"]
length=[]
for i in range(len(l)):
  length.append(len(l[i]))
print(length)
'''
'''
names=["mohan","sravya","pavani","babu","lasya"]
i=0;count=[]
while i<len(names):
    count.append(len(names[i]))
    i+=1
print(count)
'''
'''
l=["mohan","sravya","pavani","babu","lasya"]
length=[]
for i in range(len(l)):
  length.append(len(l[i]))
print(length)
'''
'''
names=["mohan","sravya","pavani","babu","lasya"]
i=0
d={}
while i<len(names):
    d[names[i]]=len(names[i])
    i+=1
print(d)
'''
'''
n=int(input())
for i in range(n-1):
    for j in range(n-1):
        print("#",end=" ")
    print()
'''
'''
for i in range (3,-1,-1):
    for j in range(3):
        print(i,end=" ")
    print()
'''
'''
n=int(input("enter range: "))
for i in range(n):
    for space in range (n-i-1):
        print("",end="")
    for star in range (i+1):
        print("*",end="")
'''
'''
i=0
n=4
while i<n:
        j=0
        k=0
        while  j<n-i-1:
                print(" ", end=" ")
                j+=1
        while k<i+1:
                print("*", end=" ")
                k+=1
        print()
        i+=1
'''
'''
n=4
rows=0
while rows<n:
    spaces=0
    while spaces<n-rows-1:
        print(" ",end=" ")
        spaces+=1
    
    stars=0
    while stars<rows+1:
        print(stars,end=' ')
        stars+=1
    print()
    rows+=1
'''



























































