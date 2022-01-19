"""Example memory diagram program."""

age: int = int(input("How old are you?"))
year: int = int(input("What year is it?"))
age_in_2041: int = 2041 - year + age

age = age + 1
year = year + 1
print("In " + str(year) + ", you'll be " + str(age))