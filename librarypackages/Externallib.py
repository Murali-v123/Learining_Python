# usage of external libraries
from currency_converter import CurrencyConverter
from datetime import datetime
from datetime import date

c = CurrencyConverter()

c.convert(112, "EUR", "USD")

# to convert user entered amount to inr
inr = int(input("Enter any amount:"))
amt = c.convert(inr, "INR", "USD")
print(f"The amount in usd is {amt}")
print(datetime.now())
print(datetime.now().time())
print(date.today())
