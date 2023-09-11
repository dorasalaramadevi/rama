import json

with open('config_test.json', 'r') as file:
    config_data = json.load(file)

number_from_config = config_data["number"]

try:
    user_input = int(input("Enter a number: "))
except ValueError:
    print("Invalid input. Please enter a valid number.")
    exit()

if user_input >= number_from_config:
    result = "You have passed"
else:
    result = "You have not passed"

print(result)
