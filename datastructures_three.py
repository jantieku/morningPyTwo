# Start by asking the number of numbers the user has
number = input("How many numbers do you have ?\n")
# Convert the received number to an integer
int_number = int(number)
# Direct the user to entering the numbers
print("Enter the", int_number,"numbers")
# Prepare an empty list to start receiving the numbers
user_numbers = []
# Write a loop to receive the numbers one by one
count = 0
while count < int_number:
    user_numbers.append(input())
    count += 1
# Write a loop to print the numbers
for num in user_numbers:
    # convert num to integer
    converted_num = int(num)
    if (converted_num%2) == 1:
        print(converted_num)