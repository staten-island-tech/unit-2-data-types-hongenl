""" #Data types 
#Numbers 1,2,3
def add(x,y):
    print(x + y)
add(1,2)
#strings "a,b,c"
name = "Mark"
def greeting(person):
    print(person)
greeting(name)
#1 & "1" are not the same
add("1","2")
#undefined/null

#booleans
tenure = False
def is_tenured(status):
    if(status == True):
        print("they have tenure")
    else:
        print("they are not tenure") """

""" x = 3
y = float(3)
print(x,y) """

""" values = [1,2.23,5,7,2,30,15]
print(values)
for i in values:
    print(i)

print(values[0])
print(values[6])

x = "this is a thing"
y= x.split( )
z = y[0]
print(y)
print(z) """

""" sentence = input():
word = sentence.split( )
z = 1
for i in sentence:
    print(z) """

""" day_of_week = input("what day is it? ")
if day_of_week == "Friday":
    print("correct")
else:
    print("incorrect") """

""" x = "test"
print(f"hello {x}") """

""" temp = 75
if temp > 68:
    print('warm')
elif temp == 68:
    print('perfect')
else:
    print('cold') """

""" num = int(input("put your number here:"))
if (num % 2) == 0:
    print("even")
else:
    print("odd") """



""" service = input("Describe the service using the words great, good, okay, or bad: ")
if service == "great":
    print('25%')
elif service == "good":
    print('20%')
elif service == "okay":
    print('15%')
elif service == "bad":
    print('0%')
else:
    print('Dont leave tip') """

""" number = int(input("Put your number here:"))
print("Factors:")
for i in range(1,number+1):
    if number%i == 0:
        print(i) """

number1 = int(input("Put your first number here:"))
number2 = int(input("Put your second number here:"))
if  number1 > number2:
        smaller = number2
else:
        smaller = number1
for i in range(1,smaller+1):
    if(number1 % i == 0) and (number2 % i == 0):
            gcf = i
print(gcf)