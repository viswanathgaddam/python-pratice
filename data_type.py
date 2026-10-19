#Programs on tuples:
#Write a program to create a tuple containing integers, strings, and floats. Print the tuple.
'''
t=tuple(map(str,input("enter any data: ").split(",")))
print(t)
'''
#Given the tuple t = (10, 20, 30, 40, 50), write a program to print the first and last elements using indexing.
'''
t=(10,20,30,40,50)
print(t[0],t[-1])
'''
#Write a program to slice a tuple t = (1, 2, 3, 4, 5) and print elements from index 1 to 3.
'''
t=(1,2,3,4,5)
print(t[1:4])
'''
#Given a tuple t = (1, 2, (3, 4), 5), write a program to access the second element of the nested tuple
'''
t = (1, 2, (3, 4), 5)
print(t[2][1])
'''
#Write a program to find how many times a specific element appears in a tuple t = (1, 2, 3, 1, 4, 1).
'''
t = (1, 2, 3, 1, 4, 1)
n=int(input("enter which element should be count: "))
count=0
for i in t:
    if i==n:
        count+=1
print(count)
'''
#Write a program to find the index of a specific element in the tuple t = ("apple", "banana", "cherry").
'''
t = ("apple", "banana", "cherry")
print(t)
c=input("type the word to find its index: ")
for i in t:
    if i==c:
        print(id(i))
else:
    print("no index found")
'''
#Write a program to concatenate two tuples and print the result. For example, t1 = (1, 2, 3) and t2 = (4, 5, 6).
'''
t1 = (1, 2, 3)
t2 = (4, 5, 6)
c=t1+t2
print(c)
'''
#Write a program to multiply a tuple by an integer. For example, multiply the tuple t = (1, 2) by 3.
'''
t = (1, 2)
for i in t:
    print(i*3)
'''
#Write a program to find the length of a given tuple.
'''
n=tuple(map(str,input().split(",")))
print(len(n))
'''
#Write a program to check if an element exists in a given tuple.
'''
print("tuple=orange, green,white,pink,yellow,red")
t=("orange", "green","white","pink","yellow","red")
c=input("enter any colour: ")
for c in t:
    print("colour exists")
    break
else:
    print("not exists")
'''
#Write a program to delete a tuple after it has been created and print a message.
'''
t=tuple(map(str,input("enter list of tuple").split(",")))
print("your tuple is:",t)
del t
print("tuple deleted")
'''
#pratice
'''
babu={"phani", "sai","john","ram"}
ntr={"pardhu", "john", "ram", "kiran"}
#union
print(babu.union(ntr))
print(ntr|babu)
#intersection
print(babu.intersection(ntr))
print(ntr.intersection(babu))
print(ntr&babu)
#difference
print(babu.difference(ntr))
print(ntr-babu)
print(babu-ntr)
#symmetric_difference
print(babu.symmetric_difference(ntr))
print(ntr.symmetric_difference(babu))
#subset
x={1,2,3,4}
y={1,2,3,4,5}
print(x.subset(y))
print(y.subset(x))
'''








































    
