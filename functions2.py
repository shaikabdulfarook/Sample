# def calculate_bill(price,quantity):
#     tot_bill=price*quantity
#     return tot_bill
# a=calculate_bill(4000,4)
# print(a)
#
# def student_details(name,age,course):
#     print(f"Name: {name}")
#     print(f"Age: {age}")
#     print(f"Course: {course}")
# student_details("rohit",39,"cse")
# student_details(name="virat",age=45,course="it")
#
# def calculate_sal(basic_sal,bonus=5000):
#     tot_sal=basic_sal+bonus
#     return tot_sal
# print(calculate_sal(50000))
# print(calculate_sal(100000,bonus=50000))
#
# def shopping_cart(*items):
#     print(f"ITEM NAMES:")
#     for item in items:
#         print(item)
#     print(f"TOTAL ITEMS:",len(items))
# shopping_cart('milk','joggery','oats','sugar')
#
# def employee_details(**details):
#     print(f"ENAME: {details['name']}")
#     print(f"Eage: {details['age']}")
#     print(f"Esal: {details['sal']}")
#     print(f"Eid: {details['id']}")
# print(employee_details(name="james",age=25,sal=25000,id=4578))
#
# def calculate_avg(*marks):
#     tot=0
#     for mark in marks:
#         print(mark)
#         tot+=mark
#     avg=tot/len(marks)
#     print("Average: ",avg)
# calculate_avg(100,98,90,96,95,80)
#
# def movie_ticket(movie_name,ticket_price,tickets=1):
#     tot_ticketprice=ticket_price*tickets
#     return tot_ticketprice
# print(movie_ticket("SPYDERMAN",4500,2))
# print(movie_ticket(movie_name='ODYSSEY',ticket_price=2000,tickets=5))
#
# def student_marks(name,*marks):
#     print(f"STUDENT NAME: ",name)
#     tot=0
#     for mark in marks:
#         tot+=mark
#     print(f"TOTAL: ",tot)
#     avg=tot/len(marks)
#     print(f"STUDENT AVG ",avg)
# student_marks('james',100,100,100,100,100)
# student_marks('riyaz',90,48,93,70,94)
#
# def student_details(**details):
#     print("SNAME: ",details["name"])
#     print("SAGE: ",details["age"])
#     print("SCOURSE: ",details["course"])
#     print("SCITY: ",details["city"])
#
# print(student_details(name='farook',age=57,course='cse',city='hyd'))
#
# def temparature(temp):
#     c=(temp*9/5)+32
#     return c
# print(temparature(35))
#
# def function(st):
#     c=0
#     for i in st:
#         if i =='A'or i=='E'or i == 'I'or i=='O' or i=='U' or i=='a' or i=='e' or i=='i' or i=='o' or i=='u':
#             c+=1
#     print(f"NO of vowels: ",c)
# function('hello')
#
# def fahrenheit_to_celsius():
#     f=float(input())
#     c=(f-32)*5/9
#     print("Temparature in celsius: ",c)
#
# def celsius_to_fahrenheit():
#     c=float(input())
#     f=(c*9/5)+32
#     print("Temparature in Fahrenheit: ",f)
#
# def fun(li):
#     print("/n 1.Fahrenheit to celsius")
#     print("2.Celsius to Fahrenheit")
#     choice=int(input("Enter your choice (1 0r 2): "))
#     if choice==1:
#         li[0]()
#     elif choice==2:
#         li[1]()
#     else:
#         print("Invalid choice")
#
# functions = [fahrenheit_to_celsius,celsius_to_fahrenheit]
# fun(functions)
#

# import copy
# from copy import deepcopy
# a=[10,20,30,[50,60]]
# b=copy.copy(a)
# print(a)
# print(b)
# b[3][0]=100
# print(a)
# print(b)
# c=copy.deepcopy(a)
# print(a)
# print(c)
# c[3][0]=15240
# print(a)
# print(c)

# def calculate_price(price,tax=5,discount=0):
#     tot_price=(price+tax)-discount
#     return tot_price
# print(f"TOTAL PRICE",calculate_price(2000,500,100))

# def create_profile(name,*skills,**details):
#     print(f"STUDENT NAME: ",name)
#     print(f"SKILLS: ",skills)
#     print(f"DETAILS: ",details)
#
# create_profile('Hardik',"java","python","c","aws",age='54',city='mumbai',course='cse')

                #11 - 08 - 2026
# def display_message():
#     print("Python is easy to learn")
# display_message()

# def welcome(name):
#     print(f"Welcome {name}")
# welcome('rohit')

# def cube(n):
#     print(n*n*n)
# cube(3)

# def is_even(n):
#     if n%2==0:
#         return True
#     else:
#         return False
# print(is_even(11))

# def full_name(first,last):
#     print(f"{first} {last}")
# full_name('rohit','sharma')

# def area_0f_rectangle(len,wid):
#     return len*wid
# print(area_0f_rectangle(6,4))

# def add(a,b):
#     return a+b
# print(add(10,20))

# def greet(name):
#     print(f"Welcome {name}")
# greet('virat')

# def square(s):
#     return s*s
# s=square(6)
# print(s)

# def message():
#     print("Hello Python")
# a=message()
# a=message()
# a=message()

# def find_len(le):
#     c=len(le)
#     return c
# print(find_len([42,78,45,96,12]))

# display=print
# display("Functional references")

# def apply(func, value):
#     return func(value)
# def cube(n):
#     return n ** 3
# print(apply(cube, 5))

# numbers = [-5, 10, -2, 8, -1, 20]
# result = filter(lambda x: x > 0, numbers)
# print(list(result))

# numbers = [1, 2, 3, 4, 5, 6]
# even = filter(lambda x: x % 2 == 0, numbers)
# result = map(lambda x: x ** 3, even)
# print(list(result)

# from functools import reduce
# prices = [499, 1299, 250, 799, 1599]
# def total_bill(prices):
#     return reduce(lambda x, y: x + y, prices)
# def calculate_bill(prices, function):
#     total = function(prices)
#     if total > 3000:
#         total = total - (total * 10 / 100)
#     return total
# result = calculate_bill(prices, total_bill)
# print(result)

# students=[("Arjun", 78),
#     ("Priya", 95),
#     ("Kiran", 82),
#     ("Divya", 91)]
# res=sorted(students,key=lambda x: x[1],reverse=True)
# print(res)


# from functools import reduce
# products = [
#     ("Laptop", 55000, 4.5),
#     ("Mouse", 800, 4.2),
#     ("Keyboard", 2500, 3.8),
#     ("Monitor", 15000, 4.7),
#     ("Headphones", 3000, 4.0)
# ]
# p=list(filter(lambda x:x[2]>=4.0,products))
# dis=list(map(lambda x:x[1]-x[1]*10/100,p))
# print(dis)
# a=list(reduce(lambda x,y:x+y,dis))
# print(a)
# from functools import reduce
# deliveries=[("D101", 5, 120),
#     ("D102", 12, 300),
#     ("D103", 3, 80),
#     ("D104", 15, 450),
#     ("D105", 8, 200)]
# filtered=list(filter(lambda x:x[1]>5,deliveries))
# print(filtered)
# mapped=list(map(lambda x:x[2]+50,filtered))
# print(mapped)
# restored=sorted(mapped,key=lambda x: x)
# print(restored)
# reduced=reduce(lambda x,y: x+y,restored)
# print(reduced)

# def display_msg():
#     print("Python is Easy to learn")
# display_msg()

# def greet(name):
#     print("Welcome",name)
# greet('rohit')

# def cube(n):
#     return n**3
# n=int(input())
# res=cube(n)
# print(res)

# def is_even(n):
#     if n%2==0:
#         return True
#     return False
# n=int(input())
# r=is_even(n)
# print(r)

# def full_name(fname,lname):
#     print(f"Full Name:",fname,lname)
# full_name('rohit','sharma')

# def area_rect(l,b):
#     return l*b
# a=area_rect(6,4)
# print(a)

# def add(x,y):
#     return x+y
# def sub(x,y):
#     return x-y
# print(add(10,20))
# print(sub(10,20))

# def is_even(num):
#     if num%2==0:
#         return True
#     return False
# def check(func,num):
#     return func(num)
# print(check(is_even,8))

# def sample(*args):
#     return args
# print(sample('abc','efr','pioijri','pourghefugh',90,547,897,1452))

# def sample(*args):
#     mul=1
#     for num in args:
#         mul*=num
#     return mul
# print(sample(1,2,3))

# def no_0f_args(*args):
#     c=0
#     for n in args:
#         c+=1
#     return c
# print(no_0f_args(15,78,45,30,459))

# def even_num(*args):
#     res=[]
#     for num in args:
#         if num%2==0:
#             res.append(num)
#     return res
# print(even_num(10,22,127,89,69,35,2012))

# def dtype(*args):
#     for val in args:
#         print(type(val))
# dtype(14,45.78,'jiklol')

# def student_details(**details):
#     print(f"Student Details: ")
#     print(details)
# student_details(name='rohit',age=20,city='mumbai',dept='cse')

# def student_details(**details):
#     for key,value in details.items():
#         print(key,":",value)
# student_details(name='rohit',age=20,city='mumbai',dept='cse')

# def employee_details(**edetails):
#     for key,value in edetails.items():
#         print(key,":",value)
# employee_details(name='ramu',age=89,sal=909099,eid=4578,dept='manage')

# def count_val(**kwargs):
#     c=0
#     for i in kwargs:
#         c+=1
#     return c
# print(count_val(name='ramu',age=89,sal=909099,eid=4578,dept='manage'))

# def employee_details(**edetails):
#     for key in edetails.keys():
#         print(key)
# employee_details(name='ramu',age=89,sal=909099,eid=4578,dept='manage')

# def intro(name,city,hobby):
#     print(f"My name is {name} , my city is {city}, and hobby is {hobby}")
# intro('james','mumbai','playing')
# intro('dancing','hyd','rohit')

# def sub(x,y):
#     return x-y
# print(sub(10,3))
# print(sub(3,10))

# def send_email(to,sub,body):
#     print("to",to)
#     print("Subj",sub)
#     print("body",body)
# send_email(sub="greeting",body="thank you",to="abc@gmail")
#
# def power(base,exp=2):
#     return base**exp
# print(power(3))

# def connect(host,port=1230,protocol='TCP'):
#     print("Host",host)
#     print("port",port)
#     print("protocol",protocol)
# connect("localhost")
# connect("localhost",4578,"udp")

# def discount_price(price,dis=10):
#     res=price*dis//100
#     tot_price=price-res
#     return tot_price
# print(discount_price(2000))
# print(discount_price(2000,20))
#
# l=[[1,2],[3,4],[5,6]]
# print(list(map(lambda x:x +[5] ,l)))
#
# d={'apple':100,'banana':40,'cherry':150}
# print(list(filter(lambda x: d[x] > 50,d)))
# #
#
# s=input()
# res=list(map(ord,s))
# print(res)

s=input()
v='AEIOUaeiou'
print(" ".join(filter(lambda x:x not in v,s)))

# num=[10,350,10,350,20]
# a=list(map(id,num))
# for address in a:
#     print(address)

# k=[5,10,15,20,25,30]
# s=list(map(lambda x:x**2,k))
# print(s)
# f=list(filter(lambda x:x%5==0,k))
# print(f)

# l=[[1,2],[3,4],[5,6]]
# print(list(map(lambda x:x + [5] ,l)))

# l=[45,788,61,3,78]
# print(list(map(lambda x:x**3,l)))

# l=[45,788,61,3,78]
# print(list(map(lambda x:str(x),l)))
# print(list(map(str,l)))

# def simple_interest(p,r=3,t=1):
#     si=(p*t*r)/100
#     return si
# print(simple_interest(10000))
# print(simple_interest(200000,4,5))
#
# def student_info(name,*subjects,**details):
#     print("Student Details")
#     print(f"Name: {name}")
#     print(f"Subjects: ")
#     for sub in subjects:
#         print(sub)
#     print(f"Details: ")
#     for key,value in details.items():
#         print(key,":",value)
# student_info("Rohit",'English','Maths','Social','Biology',city='Mumbai',age=38,dept='cse')
#
#
# def order_food(*items,**preferences):
#     print("Items: ")
#     for item in items:
#         print(item)
#     print("Preferences")
#     for key,val in preferences.items():
#         print(key,":",val)
# order_food('Biryani','Mutton dum','Chicken Fry piece','Lollipop Biryani',starters='Chilli Chicken Mutton ghee roast',spices='medium',addons='onions')
#
# def shopping_cart(discount=0,*prices):
#     total=sum(prices)
#     dis_amount=total*discount/100
#     final_price=total-dis_amount
#     return final_price
# print(shopping_cart(10,2000,3000,500,850))
# print(shopping_cart(10,1000,500,500))
#
# def register_user(username, role="user", *permissions, **details):
#     print("UserName:",username)
#     print("Role:",role)
#     print("Permissions:")
#     for p in permissions:
#         print(p)
#     print("Details: ")
#     for key,val in details.items():
#         print(key,":",val)
# register_user("Virat Kohli","Manager",'allow','deny',age=36,city='Banglore')
#
# import copy
# org=[{"item":"Laptop","Price":50000},{"item":"Mouse","Price":500}]
# shallow=copy.copy(org)
# deep=copy.deepcopy(org)
# org[0]["Price"]=45000
# print("Original: ",org)
# print("Shallow: ",shallow)
# print("Deep: ",deep)
#
# def login(username,password='1234'):
#     if password=='1234':
#         print("Login Successful")
#     else:
#         print("Login Failed")
# login("Rohit")
# login("Sharuk",9803)
#
# def area(len,breadth=None):
#     if breadth is None:
#         breadth=len
#     return len*breadth
# print(area(5,10))
# print(area(5))
#
# def calculate_score(base_score=0,*bonus_point,**penalities):
#    score=base_score
#    for bonus in bonus_point:
#        score+=bonus
#    for penality in penalities.values():
#        score=score-penality
#    return score
# print(calculate_score(20,3,2,5,red_card=5,yellow_card=2))
# print(calculate_score(100,10,20,5,red_card=10,yellow_card=5))
#
# def send_email(sender, receiver, subject="No Subject", *attachments, **options):
#     print("Sender: ",sender)
#     print("Receiver: ",receiver)
#     print("Subject: ",subject)
#     print("Attachments: ")
#     for i in attachments:
#         print(i)
#     print("Options: ")
#     for key,val in options.items():
#         print(key,":",val)
# send_email('rohit45@gmail','virat18@gmail','SELECTED FOR WORLDCUP 2027','congratulations','All the best',f_test='cleared',m_test='cleared')
#

