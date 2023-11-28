import os
from pydantic import BaseModel
from func import Prime 



d=input("vvod ")


for filename in os.listdir(d):
    if ".txt" in filename:
        f=open(d+"//"+filename)
        t=f.read()
        temp=[]
        

        for i in t:
           if i!=" ":
               temp.append(int(i))
               print(i)
               Prime(i) #булевое значение натуральности
               t.count(i)  #количество вхождений 
               if a==False: #вычисление делителей
                   Div(i)
               
               print(temp)
        print(temp)


class Dictionary(BaseModel):
    простое: bool
    вхождений: int
    делители: list

def constr(p,o,m):
    temp=Dictionary(простое=p,вхождений=o,делители=m)
    return temp.model_dump()

print(constr(30,True,5,[1,2,3,4,54]))


 
def Div(num):
    div=[]
    i=1
    while i<=num:
        if num%i==0:
            div.append(i)
        i+=1
    return div




