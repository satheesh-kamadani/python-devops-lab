# Dictionaries

my_dict = {"name": "John", "age": "25", "city": "mumbai"}
print(my_dict)

# Accessing value
print(my_dict["age"])

# Modifying and adding elements
my_dict["age"] = "26"
print(my_dict)
my_dict["gender"] = "male"
print(my_dict)

# Remove elements
del my_dict["city"]
print(my_dict)

# Checking key existance
if "age" in my_dict:
    print("Age is present in my dict")

# Iterating through keys and values
for key, value in my_dict.items():
    print(key, value)