# Robin Groot
# This program calculates the age you are on earth and venus.
import datetime    # importing the datetime module

name = input("What is your name?")    # Asks for your name
birth_year = int(input("What is your birth year?"))    # Asks for your birth year
date = datetime.datetime.now()     # Getting the current date/time
year = date.year  # Get the current year from datetime.
age = year-birth_year    # Calculate age with current year minus your birth year
print(f"Dear {name}, in {year} your age on earth will be {age}.")

venus_years = age/.62   # Calculate how old you are in venus years
print(f"And your age in venus years will be {venus_years}")