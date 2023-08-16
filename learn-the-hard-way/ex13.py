from sys import argv
# read the WYSS section for how to run this
script, first, second, third = argv

print("The script is called:", script)
print("Your first variable is:", first)
print("Your second variable is:", second)
print("Your third variable is:", third)

# print(f"{first}")
name = input(first)
# print(f"{second}")
age = input(second)
# print(f"{third}")
work = input(third)

print(f"My name is {name}. I'm {age} years old. I work as {work}.")
