# WHILE LOOP
x = 0
while x <= 5:
    print(x)
    x += 1
y = 90

while y <= 100:
    print(y)
    y += 1
z = 50

while z >= 40:
    print(z)
    z -= 1

# EVEN NUMBERS, 1---100
counter = 1
while counter <=100:
    if (counter%2) == 0:
        print(counter)
        counter += 1
    else: counter += 1

# FOR IN LOOP
cars = ["BMW", "RANGE", "TESLA","TOYOTA", "NOAH"]
print(cars[1])
print(cars[3])
cars.append("Mercedes")
cars.append("Land rover")
for gari in cars:
    print(gari)

# How many names do you have?
    # 5
# Enter the five names
    # -
    # -
    # -
    # -
    # -
    # Logic prints all the entered names
text = input("How many names do you have?\n")
jina = input("Enter the", text,"names")
jina = []