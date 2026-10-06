# def decorator(function):
#     def inner():
#         print("Before Function Execution")
#         function()
#         print("After Function Execution")
#     return inner
# @decorator
# def hello():
#     print("Hello Student")
# hello()

# def my_decorator(function):
#     def inner():
#         print("Welcome Message")
#         function()
#         print("Thank you Message")
#     return inner
# @my_decorator
# def greet():
#     print("Good Morning")
# greet()

# def calculator(function):
#     def inner(*args,**kwargs):
#         result=function(*args,**kwargs)
#         return result
#     return inner
# @calculator
# def add(a,b):
#     return a+b
# result=add(10,50)
# print(result)
# print(add(a=10,b=20))

# def check_number(function):
#     def inner(x):
#         if x%2==0:
#             print("Even Number")
#         else:
#             print("Odd Number")
#         function(x)
#     return inner
# @check_number
# def show(x):
#     print("Number Accepted")
# show(5)

# def login_verification_decorator(function):
#     def inner(username):
#         if username=="RohitSharma":
#             print("Access Granted")
#             function(username)
#         else:
#             print("Please Login First")
#     return inner
# @login_verification_decorator
# def profile(username):
#     print("Welcome to Profile")
# profile("RohitSharma")

# def electricity(rate):
#     def inner(units):
#         tot_bill=rate*units
#         print(tot_bill)
#     return inner
# rate=int(input())
# units=int(input())
# a=electricity(rate)
# a(units)

# def cal_salary(bonus):
#     def bas_sal(amount):
#         bonus_amount=amount*bonus//100
#         tot_sal=bonus_amount+amount
#         print(tot_sal)
#     return bas_sal
# sal=cal_salary(10)
# sal(500000)

# def discount(dis):
#     def prod_price(price):
#         dis_amount=price*dis//100
#         tot_bill=price-dis_amount
#         print(tot_bill)
#     return prod_price
# t_amount=discount(10)
# t_amount(50000)

# def bank_account(balance):
#     def withdraw(amount):
#         rem_bal=balance-amount
#         print(rem_bal)
#     return withdraw
# new_bal=bank_account(20000)
# new_bal(2000)

# def movie(movie_name):
#     def person(name):
#         print(f"{name} booked a Ticket for {movie_name}")
#     return person
# m_name=movie("Paradise")
# m_name("Sharuk")

# def multiplier(x):
#     def multiply(y):
#         print(x*y)
#     return multiply
# double=multiplier(2)
# triple=multiplier(3)
# double(3)
# triple(5)

# def food_order(food_item):
#     def food_quantity(quantity,price):
#         tot=quantity*price
#         print(f"{food_item}: {quantity}:",tot)
#     return food_quantity
# det=food_order("Biryani")
# det(5,200)

# def create_password(password):
#     def pwd_check(pwd):
#         if password==pwd:
#             print("Access Granted")
#         else:
#             print("Access Denied")
#     return pwd_check
# password=input()
# pwd=input()
# check=create_password(password)
# check(pwd)

# def shopping_cart(item_name):
#     def details(price,quantity):
#         print(f"{item_name}:{quantity}:{price}")
#         bill=price*quantity
#         print("Total bill:",bill)
#     return details
# tot=shopping_cart("Laptop")
# tot(50000,4)
#

# def outer():
#     count=0
#     def inner():
#         nonlocal count
#         count+=1
#         print(count)
#     return inner
# a=outer()
# a()
# a()
# a()
