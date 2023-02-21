#Write a Python program to read a file line by line and store it into a list.

f_obj =open("demo2.txt","r")
lines= f_obj.readlines()
l1=[line.strip() for line in lines]
print(lines)
print(l1)

"""
#as list comp
print([line.strip() for line in open('demo2.txt','r')])
"""
