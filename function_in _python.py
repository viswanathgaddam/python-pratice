'''
def Wish(name):
    print(f"{name} good morning. your are only who completed the given task")
    
    
Wish("viswa")
print(type(Wish))
'''
'''
def addition(a,b,c):
    return a+b+c
    
x,y,z=map(int,input().split(","))
print(addition(x,y,z))
print(x,y,z)
'''
'''
def Addition(a,b,c):
    print(a+b+c)  #local
    
x,y,z=map(int,input().split())  #global
print(Addition(x,y,z))  #none
'''
'''
l=[1,2,3]
print(len(l))
print(l.sort())
'''
'''
def Addition(a,b,c):
    return a+b+c  #local
    print("slkjdflj")#dont print after return function
    
x,y,z=map(int,input().split())  #global
print(Addition(x,y,z))  #None
'''
'''
def Find(l,search):
    for i in l:
        if search==i:
            return i
            
            
result=Find([1,2,3,4,5,1,1,1],1)
print(result+100)
'''
'''
def students(name,marks,place):
    print(f"name:{name},marks:{marks},place:{place}")
students("john",322,"gun") #positional argument 1
students(678,"sai","vig") #position2
students(marks=678,name="sai",place="gun") #keyword argument
'''
'''
def Stduents(name,marks,place="vijawada"): #defualt
    print(f"name:{name},marks:{marks},place:{place}")
    
    
Stduents("john",322) #positional

Stduents("sai",place="hyderbad",marks=678)  #keyword arguments

#positional arguments follows keyword argument
'''
'''
def cal(*values):
    print(sum(values))
cal(1,2,6)
cal(1,5,8,9,6)
'''
'''
def paradice(*items):
    print(items)
paradice(input().split())
'''
'''
def order(**items):
    print(items)
order(chicken=1,biryani=2)
'''
'''
#amstrong 
def armstrong(n):
    temp = n
    total = 0
    power = len(str(n))

    while temp > 0:
        digit = temp % 10
        total = total + digit ** power
        temp = temp // 10

    if total == n:
        print("Armstrong Number")
    else:
        print("Not an Armstrong Number")

n = int(input())
armstrong(n)
'''
#recursion
'''
def num(n):
    if n==10:
        return
    else:
        print(n)
        num(n+1)
num(1)
'''
'''
def Number(n):
    if n==0:
        return
    else:
        print(n)
        Number(n-1)
       
Number(10)
'''
'''
def Number(n):
    if n==0:
        print("end")
    else:
        print(n)
        print(Number(n-1))
       
Number(10)
'''
'''

def fact (n):
    if n==1:
        return 1
    else:
        print(n)
        return n*fact(n-1)
print(fact(5))
'''

'''
def fact(n):
    if n==5:
        return 5
    else:
        print(n)
        return n*fact(n+1)
print(fact(1))
'''
'''
n=int(input("enter any number: "))
def fib(n):
    if n==0:
        return 0
    elif n == 1:
        return 1
    else:
        return fib(n-1) + fib(n-2)
for i in range(n):
    print(fib(i), end=" ")
'''
'''
n=int(input("enter any number: "))

def Fib(n):
    if n<=1:
        return n
    else:
       return Fib(n-1)+Fib(n-2)
    
for i in range(n):
    print(Fib(i),end=(" "))
'''
'''

def Score_board(overs):
    l=[];start=1
    while start<=overs:
        balls=1
        while balls<=6:
            ball_score=input(f"enter over {start} ball:{balls}:")
            if ball_score=="wd" or ball_score=="nb":
                l.append(1)
                continue
            else:
                l.append(ball_score)
                balls+=1
        print(l)
        start+=1
    
Score_board(2)
'''
'''
from e import total
n=[1,2,3,4,5]
print(total(n))
'''
'''
import gen as Files

print(gen.Length([1,2,3,4,5,4,4]))
'''
'''
import gen as Files     #all functions

print(Files.Length([1,2,3,4,5,4,4]))

from gen import Pardhu as p    #only particular function
print(p("john"))
'''
'''
from e import total as add
n=[25,69,87,56]
print(add(n))
'''
'''
sub=lambda x,y:x-y
print(sub(56,100))
'''
'''
lambda s:s[0].capitalise()
'''
'''
result=lambda x,y,z,n:[x,y,z,n]
print(result("python","cython","java","bava"))
'''
'''
x=10;y=20
print((lambda x,y:x+y)(x,y))
'''
'''
print((lambda x,y:x+y)(10,20))
'''
'''
print((lambda x:"even" if x%2==0 else "odd")(10))
'''
'''
print((lambda x:"even" if x%2==0 else "odd")(10))

print((lambda x:x%2==0 "even")(12))   #error
'''
'''
#if is mendatory whern you use if else if mandatory
n=int(input("enter any number: "))

print((lambda n:"even" if n%2==0 and n>5 else "odd" if  n%2!=0 else "not")(n))
'''
'''
s=input()
print(lambda x:"valied" if len(x) >=5 and len(x)<=12 else "invalied")(s)
'''
'''
s = input()
print((lambda s:"valid" if len(s)>5 and len(s)<12 else "Invalid")(s))
'''
'''


x=[7,8,9,1,2,3,4]
l=[]
for i in x:
    if i%2==0:
        l.append(i)
print(l)

print((lambda n:[i for i in range(n)])(5))

x=[7,8,9,1,2,3,4]
l=[]
for i in x:
    if i%2==0:
        l.append(i)
    else:
        l.append("odd")
print(l)

print([i for i in x if i%2==0])
print([i if i%2==0 else "odd" for i in x])

print({i if i%2==0 else "odd" for i in x})

x=[7,8,9,1,2,3,4]
print({i:"even" if i%2==0 else "odd" for i in x})

'''
'''
x=[[0,1,2],[3,4,5],[6,7,8]]
y=[j for i in x for j in i]
print(y)
'''
'''
print(list(map(lambda x:"even" if x%2==0 else "odd",[1,2,3,4,5,6])))

print(list(map(lambda x:"even" if x%2==0 else x,[1,2,3,4,5,6])))
'''
'''
x=["a","b","c","d","e"]
print(set(map(lambda x:x.upper(),x)))

prices=[900,1000,800,700,300,200,1200]
result=filter(lambda x:x<500 ,prices)
print(list(result))

a=["python","cython","pardhu","paul","john"]
res=filter(lambda x:x.startswith("p"),a)
print(list(res))
'''
#reduce:
'''
from functools import reduce
prices=[900,500,100,500]
result=reduce(lambda x,y:x+y,prices)
print(result)

import functools
prices=[900,500,100,500]
result=functools.reduce(lambda x,y:x+y,prices)
print(result)
'''
'''
import functools
x=["sir","madam","sir","anthey"]
print(all(i for i in x if len(i)<3))

x=["sirs","madam","sir","anthey"]
print(all(len(i)>3 for i in x ))

x=["sirs","madam","sir","anthey",1]
print(all(type(i)==str for i in x ))

Pardhu
12:03 PM
x=["sirs","madam","sir","anthey",1]
print(any(type(i)==int for i in x ))
'''
'''
def generator(n):
    for i in n:
        yield i
n=["1f","2f","3f","4f"]
print(next(generator(n)))
'''
'''
def Generator(n):
    for i in n:
        yield i
    
    
n=["1file","7file","3file","4file","5file"]
result=Generator(n)
print(next(result))
print(next(result))
print(next(result))


def Generator(n):
    for i in n:
        yield i
    
    
n=["1file","7file","3file","4file","5file"]
result=Generator(n)
print(type(result))
# print(next(result))
# print(next(result))
# print(next(result))

for i in range(len(n)):
    print(result.__next__())
'''
print(list((i for i in range(4))))












