# Conditional handling
import sys

type = sys.argv[1]

if type == "t2.micro":
    print("it will charge you 2 dollars per day")
elif type == "t2.medium":
    print("it will charge you 4 dollars per day")
elif type == "t2.large":
    print("it will charge you 8 dollars per day")
else:
    print("Please provide a valid instance type")