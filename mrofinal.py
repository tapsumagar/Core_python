class pilot:
    def __init__(self,fname,contact,gender):
        self.name=fname
        self.phone=contact
        self.htype=gender

class Copilot:
    def __init__(self, qlf, age):
        self.academic=qlf
        self.age=age

class Engneer(pilot,Copilot):
    def __init__(self, fname, contact, gender, qlf, age):
        super().__init__(fname, contact, gender)
        Copilot.__init__(self, qlf, age)

class Hostes:
   name = 'Anu'
        

class Software_Engineer(Engneer, Hostes):
    def __init__(self, fname, contact, gender, qlf, age):
        Engneer.__init__(self, fname, contact, gender, qlf, age)
        

#creating the object
objectlast = Software_Engineer(fname='Rima',contact='99999999',gender='Female',qlf='BIT',age='23')
print(Software_Engineer.__mro__)
print(objectlast.name)
