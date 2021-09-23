"""
Name:           Robin Groot
Version:        1.0
Inputs:         Type of currency, The amount of currency
Outputs:        Amount of euro, transaction fees, total minus the fees
Description:    This program will convert USD, Pounds or Yen to euro.
"""
# imports
from forex_python.converter import CurrencyRates
from forex_python.converter import CurrencyCodes
cr = CurrencyRates()
cc = CurrencyCodes()

# Currency Rates for dollar, pound and yen
dollar = cr.get_rate('USD', 'EUR')
pound = cr.get_rate('GBP', 'EUR')
yen = cr.get_rate('JPY', 'EUR')

# Asks for what currency you want to convert
exchange_currency = input("Choose between USD, GBP and YEN\n"
                          "Which currency do you want to convert to euro?\n")

# Asks for how much of it you want to convert
currency_amount = float(input("How much of this currency do you want to convert to euro?\n"))

# Sets the currency to convert and the symbol to place next to the final calculation.
exchange_currency_total = "Nothing"
cs_symbol = "Nothing"
if exchange_currency == "USD":
    exchange_currency_total = dollar
    valid_currency = True
    cs_symbol = cc.get_symbol('USD')
elif exchange_currency == "GBP":
    exchange_currency_total = pound
    valid_currency = True
    cs_symbol = cc.get_symbol('GBP')
elif exchange_currency == "JPY":
    exchange_currency_total = yen
    valid_currency = True
    cs_symbol = cc.get_symbol('JPY')
else:
    valid_currency = False

# Calculates total, fees and total minus fees
total_before = currency_amount * exchange_currency_total

total_fee = 2
float(total_fee)
total_after = total_before-total_fee

# Makes list of items to format.
list_input = [currency_amount, total_before, total_fee, total_after]
list_input = ['%.2f' % elem for elem in list_input]
list_output = []

# Decides if it should be 1 or 2 decimals based on if the last number is 0 or not
for o in list_input:
    if o[-1] == '0':
        o = o[:-1]
        list_output.append(o)
    else:
        list_output.append(o)

# Does the calculation if a valid currency has been selected else it will print a error message.
sy_eur = cc.get_symbol('EUR')
if valid_currency:
    print(f"Amount to be converted: {cs_symbol}{list_output[0]} into {sy_eur}.\n"
          f"For {cs_symbol}{list_output[0]} you get {sy_eur}{list_output[1]}\n"
          f"The fees are: {sy_eur}{list_output[2]}\n"
          f"You get {sy_eur}{list_output[3]} after fees.")
else:
    print("No valid currency has been given so no conversion can be given")
