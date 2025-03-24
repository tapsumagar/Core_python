"""
Method Resolution order (MRO) is the order in which python looks
for  a method in a hierarchy of classes. Especially it plays vital
role in the context of multiple inheritence as single method may be
found in multiple super classes.
"""

class copilot:
    def __init__(self, First_name, age1, contact):
        self.name = First_name
        self.age = age1
        self.phone = contact


class Hostess(copilot):
    def __init__(self, skill, scale, First_name, age1, contact):
        super().__init__(First_name, age1, contact)
        self.able = skill
        self.salary = scale

class AircraftEng (Hostess):
    def __init__(self,age_of_eng, interest_of_eng,skill,scale,First_name,age1,contact):
        super().__init__(skill,scale,First_name,age1,contact)
        self.age = age_of_eng
        self.interest=interest_of_eng

class pilot(AircraftEng):
    def __init__(self,name_pilot,age_of_eng, interest_of_eng,skill,scale,First_name,age1,contact):
        super().__init__(age_of_eng, interest_of_eng,skill,scale,First_name,age1,contact)
        self.nam = name_pilot

class MroData(pilot):
   def __init__(self,gap, First_name, age1, contact, skill, scale, age_of_eng, interest_of_eng, name_pilot):
        super().__init__(name_pilot, age_of_eng, interest_of_eng, skill, scale, First_name, age1, contact)
        self.lackup = gap
#creating an instance of the MroData class
objectfinal = MroData(First_name="Hari KC",age1=23,contact="9878997",skill="dance",scale="983947",
                      age_of_eng=45,interest_of_eng="swimming",name_pilot="captain lama",gap="mina")

#printing the name of the pilot
print(objectfinal.nam)
print(MroData.__mro__)
        

