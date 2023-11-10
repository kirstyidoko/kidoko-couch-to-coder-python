pin_number = 1234
balance = 5000
attempt = 3

input_pin = int(input("Welcome to Bright Network Banking. Please enter your PIN:"))

while(input_pin != pin_number):
    print(f"Incorrect PIN. You have {attempt} attempt(s) remaining.")
    attempt -= 1
    input_pin = int(input())
    if attempt == 0:
        print("Account locked. Please contact us for assistance.")

print("Hello. Your balance is £" + str(balance))
# Ask if customer would like to withdraw or deposit cash
print("Would you like to withdraw or deposit some money? Type 'withdraw', 'deposit' or 'no'.")
input_decision = input()

# If customer wants to withdraw, ask for amount to be withdrawn and subtract from balance
if input_decision == "withdraw":
    print("Please enter the amount you would like to withdraw:")
    input_withdraw = input()
    print("Your new balance is £" + str(balance - int(input_withdraw)) + ". Thank you for banking with us today.")

# If customer wants to deposit, ask for amount to be deposited and add to balance
elif input_decision == "deposit":
    print("Please enter the amount you would like to deposit:")
    input_deposit = input()
    print("Your new balance is £" + str(balance + int(input_deposit)) + ". Thank you for banking with us today.")

# If nothing else, thank customer
else:
    print("Thank you for banking with us today.")