import os

from func import Prime,  Dictionary

def divisor(num):
    div=[]
    i=1
    while i<=num:
        if num%i==0:
            div.append(i)
        i+=1
    return div


print(divisor(5))

print(Dictionary.constr(True,5,[1,2,3,4,54]))


d=input("vvod ")


for filename in os.listdir(d):
    if ".txt" in filename:
        f=open(d+"//"+filename)
        t=f.read()
        temp=list(map(int,t.split()))
        print(temp)    


 




