import os
from pydantic import BaseModel




d=input("vvod ")


for filename in os.listdir(d):
    if ".txt" in filename:
        f=open(d+"//"+filename)
        t=f.read()
        temp=[]

        for i in t:
           if i!=" ":
               temp.append(int(i))
               #тут будет функция перебора списка и проверки на натуральность 
               print(temp)
        print(temp)


class Dictionary(BaseModel):
    простое: bool
    вхождений: int
    делители: list

def constr(n,p,o,m):
    temp=Dictionary(простое=p,вхождений=o,делители=m)
    return {str(n):temp.model_dump()}

print(constr(30,True,5,[1,2,3,4,54]))


