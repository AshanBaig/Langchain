# theory main 1_atheory me hy   


from typing import TypedDict

class Person (TypedDict):
    name:str
    age:int
    
new_person : Person = {"name":"ashan","age":20}   # new_person is inherited with prson and if we hover on age so it will tell us age int honi chahaye

print(new_person)