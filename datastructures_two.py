# Start by asking the number of numbers the user has
number = input("How many numbers do you have ?\n")
# Convert the received number to an integer
int_number = int(number)
# Direct the user to entering the numbers
print("Enter the", int_number,"numbers")
# Prepare an empty list to start receiving the numbers
betting_numbers = []
# Write loops to receive the numbers one by one
count = 0
while count < int_number:
    betting_numbers.append(input())
    count += 1
# Ask the user which number they want to bet with
bet_number = input("Enter the number you wish to bet with\n")
# Write a loop to check if the bet number exists
for nambari in betting_numbers:
    if nambari == bet_number:
        print("Bet successful")
        break