import datetime as dt

birth_year = input("Enter your birthyear")
today = dt.date(year=2023,month=12,day=17)

age = today - birth_year

def calculate_age():
    print("You are " + str(age) + " old")

