import os

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