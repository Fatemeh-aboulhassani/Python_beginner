#list[]

List=["python",67,"matlab",35]

list1=["day","12",23,"#","df34","57!"]
# 23 int    "day" string

#the first item has index [0], the second item has index [1]
print(List[:])
print(list1[1]) # 0..>"day"  1..> "12"
print(list1[2])
print(list1[1:4]) #until 4 not 4
print(list1[2:])
print(list1[2:2])


#list1[11] ....> list index out of range

length=len(list1)
b=list1[length-1] # 56!
print(b)


List=["python",67,"matlab",35]
print(List[0][0])  #p
print(List[2][0])  #m



list2=["23",1394,"day","year"]
print(list2[-1]) #year
print(list2[3][-1]) #r





Day=["saturday","sunday","monday","tuesday","wendesday"]
print(len(Day))#len=5
count=0
print("today is : ", Day[count])  #saturday
count=1
print("today is : ", Day[count])   #sunday






Day1=[1398,["january","february"],"march",13]
print(Day1[1]) 
print(Day1[1][1][-1])
print(Day1[-2][-5])
print(len(Day1))


 

L2=[100,200,300,400]
L2[2]=50
print(L2)
L2[1:1]=[900,800]
print(L2) #[100, 900, 800, 200, 50, 400]



T1=[10,20,30,40,50]
T2=[80,90,100]
print(T1+T2)  #[10, 20, 30, 40, 50, 80, 90, 100]
T1[2:2]=["Sara","ali"] 
print(T1)   # output [10, 20, 'Sara', 'ali', 30, 40, 50]



N1=[1,2,3,"S"]
N3=N1+N1
#Repeating the input list 2 times using the * operator
N4=N1*2
print(N3)  #output [1, 2, 3, 'S', 1, 2, 3, 'S']
print(N4) #output [1, 2, 3, 'S', 1, 2, 3, 'S']



N2=[6,"apple","orange",55]
N2[:]=[]
print(N2)#output []

del(N2)
#print(N2)   #output : not defined


P=[800,"Samsung","apple","microsoft",900,100]

if 800 in P:
    print("true")
else:
    print("false")
    
    
if not 7 in P:
    print("true")
else:
    print("false")



  #methods in List
    
Listx=["math","physics","arabic"]
Listx.append("algebra") # append +
print(Listx)
# output ['math', 'physics', 'arabic', 'algebra']
# name.append fügt am Ende hinzu aber name.insert fügt wo man genau will hinzu






Listx.remove("math") # remove -
print(Listx)
#output ['physics', 'arabic', 'algebra']



Listy=["math","physics","arabic","Math"]
Listy.count("math")
# repeating is 1 because Math , math

Listy.count("algebra")
#output 0  

list_new=[1,45,21,188,9,12]
list_new.append("math")
print(list_new)
#[1, 45, 21, 188, 9, 12, 'math']


list_new.append(2)
print(list_new)
#[1, 45, 21, 188, 9, 12, 'math', 2]

list_new.remove("math")
print(list_new)
#[1, 45, 21, 188, 9, 12, 2]


list_new.sort()
print(list_new)
#[1, 2, 9, 12, 21, 45, 188]
