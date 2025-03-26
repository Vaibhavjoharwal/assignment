print("hello world")
#variables
a= 3
print(type(a))

# string
print("\n")
str = "python is easy"

#indexing
print("\n")
print(str[5])
print(str[-1])

#slicing
print("\n")
print(str[2:5])
print(str[-4:-1])
print(str[::-1]) #revarce

#string methords
print("\n")
str1 ="python is easy"
print(str1.upper())
print(str1.lower())
print(str1.split())
print(str1.strip())
print(str1.replace("easy","hello"))
print(str1.find("easy"))
print(str + str1)
print(str + " " +str1)

# Tuples
print("\n")
tuple=(1,2,3,"python",True)
print(tuple)
print(type(tuple))
print(tuple[2:6])
print(tuple[::-1])

#operaters
print("\n")
t=(1,2,3,4,5,6,7,)
print(t+ tuple)
print(t*2)
print(t.count(3))
print(t.index(7))

#list
lst=[1,2,3,4,5,6,]
print(lst)

#indexing
print(lst[0])

#slicing
print(lst[1:6])


#modifing the list
lst[2] ="python" 
print(lst)
lst.append(3)
print(lst)
lst.insert(4,3)
print(lst)
lst.remove(6)
print(lst)
lst.pop()
print(lst)
lst.reverse()
print(lst)
lst2=[2,3,1,5,6,4]
lst2.sort()
print(lst2)