##sequence



seq1="python"
seq2="123"
seq3="introduction to python"
s3=seq3[3]
print(s3)
s4=seq3[1:5] # to 5 not exactly 5
print(s4)
s5=print(seq3[0:4])
s6=print(seq3[7:]) #until the end
s7=print(seq3[:4]) # from 0 to 3
# i want to write (I) instead of i
seq3_new="I"+seq3[1:] #I is sequence
print(seq3_new)
seq3_new1="I"+seq3[1:16]+"P"+seq3[17:] # P and I big
print(seq3_new1)
snew=seq3_new1+" for the students" #space is important
print(snew)
length=len(seq3_new)
print(length)





a="my name is fatemeh"
b=a.upper() 
# I want to make the letters bigger
print(b)


c=a.lower()
#I want to make the letters smaller
print(c)


d=a.count("a")
# I want to count the "a" in sentence
print(d)


e=a.find("a")
#the address of "a" is (only first a)
print(e)

f=a.count("fat")
print(f)

g=a.find("a",5)
# first a is 4 then where is second "a"
print(g)


# in , not in
"p" in a #false  "p" not exist
"p" not in a #true


if "p" in a:
    print("true") 
else:
    print("false")