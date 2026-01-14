age = float(input("enter your age:"))
if age >= 18:
    print("you are now signed up")
elif age < 0:
    print("you are not yet born")
else:
    print("you are not yet authorized")
#2
response = input("would you like some food? Y/N")
if response == "Y":
    print("have some food")
else:
    print("no food")


#conditional expression
num = 5
print("positive" if num > 0 else "negative")
numb = 6
if numb > 6:
    print("great")
else:
    print("not great")

#length
#name = input("what is your name?")
#result = len(name)
#result_1 = name.find(" ")
#result_2 = name.rfind("q")
#name1 = name.capitalize()
#print(name1)
#name2 = name.upper()
#result1 = name.isdigit()
#print(result1)
#print(result_1)
#print(result)

#validate user input
username = input("enter your username:")
if len(username) >12:
    print("12 letters is the limit")
elif not username.find(" ") == -1:
    print("no space")
else:
    print("you are welcome")