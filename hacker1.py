##[Yesterday 10:21 PM] Tejeshwari Gandi
##    
##def bucket_sort(l):
##d=[]
##r = []
##c=len(l)
##for i in range(c):
##d.append([])
##for j in l:
##if j*10<c:
##index=j*10
##d[int(index)].append(j)
##else:
##index=c-1
##d[int(index)].append(j)
##for k in d:
##k.sort()
##for m in d:
##for z in m:
##r.append(z)
##return r
##print(bucket_sort([0.1,0.3,2.5,5.6,0.2,1.2,2.2]))
##=========================================================================
###1. How do you print the first non-repeated character from a string?
##
##
##st=input("enter string ")
##
##
##for i in st:
##    count=st.count(i)
##    if count==1:
##        print(i)
##        break
##
##
##
##output:
##enter string sandeep
##==========================================================================
###4.check if the given string is valid email address or not.
##
##
##s=input('enter string')
##if s.endswith('@gmail.com') or s.endswith('@gmail.com'):
##    print("given email address is valid')
##else:
##    print("invalid emaild")
##
##
##
##output:
##
##
##enter string sandeep@gmail.com
##given email address is valid
##==========================================================================
###5.How do you find all the permutations of a string?
##
##
##from itertools import permutations
##str=input('enter values')
##per=permutations(str)
##for i in per:
##    print(i)
##    
##output:
##enter values123
##('1', '2', '3')
##('1', '3', '2')
##('2', '1', '3')
##('2', '3', '1')
##('3', '1', '2')
##('3', '2', '1')
##
##
##
##
##
##
##
##
##
##
##
##
##
##
##
##
##
##
##
##
##
##
##>>> 


'''a = ["sandeep","praveen","salman"]
for i in  a:
  print(i[0])
          

d = {"A":20,"B":30,"C":40}
num = int(input("Enter a number :"))
for i,j in d.items():
  if d[i] == num:
    print(i)
  else:
    print("Element not found")
  break'''
n=int(input("Enter a number :"))
if n%2==0 :
  print("Not Weired")
elif n >= 20:
  print("Not weired")
else:
  print("weired")


  





