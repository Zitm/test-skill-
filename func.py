from pydantic import BaseModel

def Prime(num):
    t=2
    while num%t!=0:
        t+=1
    return t==num






class Dictionary(BaseModel):
    простое: bool
    вхождений: int
    делители: list
    
    def constr(p,o,m):
        temp=Dictionary(простое=p,вхождений=o,делители=m)
        return temp.model_dump()
