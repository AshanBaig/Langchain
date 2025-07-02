from pydantic import BaseModel,EmailStr,Field
from typing import Optional,Annotated,Literal
class Student(BaseModel):
    name:str = "John boss" # default a jayga if i dont put anyname
    age : Optional[int] = None # agr age nhi tw None
    email:EmailStr
    school: str = "Defaulter"
    cgpa :float = Field(gt=0, lt=4,default = 3, description="A decimal value reprsenting the cgpa of the student", example=3.5, title="CGPA")
    # field ki madad se hum phone number ke bare me mail ke bare me description de skhte etc
new_student = {"name":"ashan","email":"asha@gmail.com","age":"21","cgpa":3.9}

student = Student(**new_student)  #**new_student ka matlab hai dictionary ke key-value pairs ko unpack kar do.
# student = Student(name="ashan") # uper wla or ye both are euqal
print(student)
student_json = student.model_dump_json()
print(student_json)


#email format na do tw error
# ye itna smart hy ke khud 21 ko int me convert kr lega
# new_student = {"name":32} # error a jayega str nhi hy


