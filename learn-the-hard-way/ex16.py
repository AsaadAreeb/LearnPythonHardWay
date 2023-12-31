from sys import argv

script, filename = argv

print(f"We're going to erase {filename}.")
print("If you don't want that, hit CTRL-C (^C).")
print("If you do want that, hit RETURN.")

input("?")

print("Opening the file...")
target = open(filename, 'w')

print("Truncating the file. Goodbye!")
# useless to do truncate cuz we're opening the file  with `w`
target.truncate()

print("Now I'm going to ask you for four lines.")

line1 = input("line 1: ")
line2 = input("line 2: ")
line3 = input("line 3: ")
line4 = input("line 4: ")

print("I'm going to write these to the file.")

target.write(line1)
target.write("\n")
target.write(line2)
target.write("\n")
target.write(line3)
target.write("\n")
target.write(line4)

print("And finally, we close it.")
target.close()
