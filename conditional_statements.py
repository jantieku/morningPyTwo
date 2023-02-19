x = 10
y = 20
if x > y:
    print("TRUE")
else:
    print("FALSE")
# Write a logic to implement a grading system
# with the following
# 0_______40______E
# 40.1_______50______D
# 50.1_______60______C
# 60.1_______70______B
# 70.1_______100______A
marks = 90
if marks < 0 or marks > 100:
    print("Please enter valid marks")
elif marks <=40:
    print("E")
elif marks <=50:
    print("D")
elif marks <=60:
    print("C")
elif marks <= 70:
    print("B")
else:
    print("A")

