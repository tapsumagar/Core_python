"""
First knowledge about user define Higher order function then we can understand easily 
decorator concept
"""
#user define Higher order
# def print_func(user_define_function):
#     print(user_define_function())

# def get_user_info():
#     return 'Name','Dikhsya', 'age','21','kathmandu'

# print_func(get_user_info)

# decorator #kunaii yauta chij laii harek patak use garnu laii decorator vaninxa

# def us_dollor_conv(comfunc):
#     print(comfunc()*137)

# def get_salary():
#     return 500

# def pay_fee():
#     return 300

# us_dollor_conv(get_salary)
# us_dollor_conv(pay_fee)

def us_conv(cust_func):
    def wrapper():
        return cust_func()*137
    return wrapper

@us_conv
def re_salary():
    return 17000

@us_conv
def pay_fee():
    return 4700


salary_calcu=re_salary()
Feepay = pay_fee()
print('Emplyoee has {}' . format(salary_calcu)+' and Due Fee is {}'.format(Feepay))




from datetime import datetime
def log_file(func):
    def wrapper():
        with open('log_details.txt','a')as f:
            f.write('The user '+func.__name__+' activity at' +str(datetime.now()) +'\n')
            func()
        
    return wrapper

@log_file
def login():
    print('user login')

@log_file
def logout():
     print('user logout')

#login()
logout()