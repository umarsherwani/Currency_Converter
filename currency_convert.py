with open('currency.txt') as f:
    lines = f.readlines()
# Create empty dictionary to store data
currency_dict = {}
for line in lines:
    parsed= line.split('\t')
    currency_dict[parsed[0]]= parsed[1]
# Show dictonary keys 
[print(item) for item in currency_dict]
amount = int(input('Enter the amount in Rupee : '))
choose_currency = input('Enter the one of these item : ')
# Multiply user input to dictionary Values
converted = amount * float(currency_dict[choose_currency])
print(f"Your amount is  {amount} and your converted amount is {converted} {choose_currency}")
