# INBUILT FUNCTIONS
greeting = "Hello world"
print(greeting)

capital_greeting = greeting.upper()
print(capital_greeting)

lower_greeting = greeting.lower()
print(lower_greeting)

striped_greeting = greeting.strip()
print(striped_greeting)

number = -4
print(number)

pos_number = abs(number)
print(pos_number)

sqrd_number = pow(number,2)
print(sqrd_number)

print(number + number)
str_number = str(number)
print(str_number + str_number)

int_number = int(str_number)
print(int_number + int_number)
#CUSTOM / USER DEFINED FUNCTION
def motto():
    print("Hey this is our motto")
motto()


def adding_numbers():
    x = 20
    y = 30
    z = x + y
    print(z)
adding_numbers()
def multiplying_numbers():
    a = 50
    b = 30
    c = a * b
    print(c)
multiplying_numbers()
def avg(x,y,z):
    mean = (x + y + z) / 3
    print("Hello there your answer is", mean)

avg(25,60,65)
avg(50,58,64)

def s_interest(p,t,r):
    interest = (p*t*r) / 100
    print("Hey your interest is", interest)

s_interest(20000,4,10)