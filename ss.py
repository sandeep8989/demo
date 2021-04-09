'''import csv
dict={'name':['a','b','c'],'dept':['python','java','UI'],'id':[1,2,3]}
with open('employee_file3.csv', mode='a+',newline="") as csv_file:
    fieldnames = [i for i in dict]
    writer = csv.DictWriter(csv_file, fieldnames=fieldnames)
    if csv_file.tell()==0:
        writer.writeheader()
    temp=[]
    for i in dict.values():
        temp.append(i)
    zi=list(zip(*temp))
    for j in zi:
        writer.writerow({fieldnames[i]:j[i] for i in range(len(zi))})
        '''
'''
def prime(num):
    temp=[]
    for i in range(2,num):
        for j in range(2,i):
            if i%j==0:
                break
        else:
            temp.append(i)
    for i in range(len(temp)-1):
        if temp[i+1]-temp[i]==2:
            print(temp[i],',',temp[i+1],':')
prime(100)
          '''
'''
runs=int(input("enter required runs"))
overs=float(input("enter required overs"))
ov=str(overs).split(".")
if int(ov[1])<6:
    balls=int(ov[0])*6+int(ov[1])
 
    if balls>=100:
            print(f"{runs} runs in {overs} @ {runs/overs} runs per over")
    else:
        print(f"{runs} runs in {balls} balls @ {runs/balls} runs per ball")
else:
    print("enter valid overs")

'''
"""salary = float(input("enter salary :"))
if salary > 0:
    while True:
        try:
            expensename = input("enter expense name :")
            if expensename.isalpha() == True:
                    expensename = expensename.lower()
            else:
                raise 'error'
                expenseamount = float(input("enter expense amount :"))
                break
        except:
            print("Please Enter valid details")
        else:
            print("enter valid salary")"""

 


'''
while True:
    try:
        salary=float(input("enter expense salary : "))
        while True:
            try:
                expensename=input("enter expense name :")
                while True:
                    try:
                        expenseamount=float(input("enter expense amount :"))
                        while True:
                            
                except:
                        print("enter valid amount")
                            
            except:
                print("enter valid exp name")
    except:
        print("enter valid salary")
        '''
        
 
d={}
salary = 0
total = 0
def salary_val():
    while True:
        while True:
            try:
                global salary
                salary=float(input("ENTER YOUR SALARY: "))
                return salary
            except:
                print("ENTER VALID SALARY")
                break
            
    
def validation():
    validity = True
    while validity:             
        expname=input("ENTER YOUR EXPENDITURE NAME:").lower() 
        if expname.isalpha(): 
            while True:
                try:                        
                    expamt=float(input("ENTER YOUR AMOUNT: "))
                    return [expname,expamt]
                except:
                    print("ENTER VALID AMOUNT: ")    
        else:
            print("ENTER VALID EXPENDITURE NAME: ")
    
    

def Expanse_calculator():
    salary = salary_val()
    global total
    global temp
    temp = salary
    
    while temp>0:
        rt = validation()
        x = rt[0]
        if x in d.keys():
                price =rt[1]
                if temp>=price:
                    d[x]+=price
                    temp-=price
                else:
                    print("insufficint found")
                    break
        else:
            price =rt[1]
            if temp>=price:
                d[x]=price
                temp-=price
            else:
                print("insufficint found")
                break
        total=sum(d.values())
        while True:
            ip = input("If you want to add any more expenditure [YES|NO]:")
            if ip.lower() == 'no':
                return
            elif ip.lower() == 'yes':
                break
            else:
                print("Invalid Entry")
            
        if total>salary:
            print("insufficint found")
            break
    else:
        print("insufficint found")
    return
l=  Expanse_calculator()
print(d)

   
""" Table Format """
print(f"salary{' '*15}:{' '*15}{salary}/-")
print(f"{'-'*75}")
for k,v in d.items():
    print(f"{k}{' '*16}:{' '*15}{v}")
print(f"{'-'*75}")
print(f"Total{' '*16}:{' '*15}{total}/-")
print(f"Balance{' '*14}:{' '*15}{temp}/-")
       
                     














    
