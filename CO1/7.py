l1=[1,2,3,4,5]
l2=[3,4,2,1,5]

#print(" Whether list are of same length :")
#if len(l1)==len(l2):
 #   print("Same length")       
#else:
  #  print("Not Same Length")
  
#print("whether list sums to same value : ")
#s1=0
#s2=0
#for x in l1:
 #   a=s1+x
#for y in l2:
  #  b=s2+y
#if a==b:
 #   print("same value")
#else:
#    print("Not same")
print("whether any value occur in both : ")

for x in l1:
    for y in l2:
        if x==y:
            print("common element is ",y)
       



