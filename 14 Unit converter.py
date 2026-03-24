"""
14. Unit converter
"""

choice = input("What do you want to convert? Temperature, currency, or mass: ")

if choice.lower == 'temperature':
    temp_celcius = int(input("Enter your temperature in celcius"))
    temp_fahrenheit = (temp_celcius * 1.8) + 32
    print(f"{temp_celcius} °C in fahrenheit is {temp_fahrenheit} °F")
elif choice.lower == 'currency':
    money_gbp = int(input("Enter your amount in GBP"))
    money_usd = (money_gbp * 1.34) # As of 23/3/26 @ 12:46pm
    print(f"£{money_gbp} in USD is {money_usd}$")
elif choice.lower == 'mass':
    mass_kg = int(input("Enter your mass in conversion"))
    mass_lbs = mass_kg * 2.20462262
    print(f"{mass_kg}kg in pounds is {mass_lbs}lbs")
else:
    print("Invalid option")