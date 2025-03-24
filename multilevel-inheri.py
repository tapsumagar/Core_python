class copilot:
    def __init__(self, First_name, age1, contact):
        self.name = First_name
        self.age = age1
        self.phone = contact


class Hotess(copilot):
    def __init__(self, skill, scale, First_name, age1, contact):
        super().__init__(First_name, age1, contact)
        self.able = skill
        self.salary = scale

access1 = Hotess(skill='Flight manage',scale='170000',First_name='Tapsu Magar',age1=25,contact='9809589332')
print(access1.name + 'has' + access1.salary + 'and her contact is' + access1.phone + 'and duties is' + access1.able)

class Air_craft_Engineer(Hotess):
    def __init__(self, qlf, skill, scale, First_name, age1, contact):
        super().__init__(skill, scale, First_name, age1, contact)
        self.academic= qlf

access2 = Air_craft_Engineer(qlf= 'Be. Aircraft', skill='Flight manage',scale='170000',First_name='Tapsu Magar',age1=25,contact='9809589332')
print(access2.academic)
