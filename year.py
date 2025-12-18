from datetime import datetime

year = int(input("enter year : "))
current_year = datetime.now().year
age = current_year - year
print("your age:", age)

