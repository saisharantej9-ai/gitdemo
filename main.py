from operator import truediv

#strings
first_name = "bro"
food = "pizza"
email = "hi@gmail .com"
print(f"hello {first_name}")
print(f"you like {food}")

#integers
age = 17
number_of_students = 10
print(f"you are {age} years old")
print(f"in your class there are {number_of_students} students")

#float
price = 10.99
gpa = 4.98
distance = 80
print(f"the price is {price}")

#boolean
is_student = False
for_sale = True

if for_sale:
    print(f"item for sale , the price is {price}")
else:
    print("item not for sale")
if is_student:
    print("you are a student")
else:
    print("you are not a student")

#typecasting
name = "sharan"
age = 17
gpa = 9.5
is_student = True
gpa = int(gpa)
print(gpa)
age += 0
name = bool(name)
print(name)
print(age)

#input()
name = input("What is you name? :")
print(f"hello: {name}")
age = int(input("how old are you? :"))
age += 1
print ("happy birthday!")
print(f"you are {age} years old")

