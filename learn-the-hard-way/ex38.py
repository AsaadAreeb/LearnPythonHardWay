ten_things = "Apples Oranges Crows Telephones Light Sugar"

print("Wait there are not 10 things in that list. Let's fix that.")

stuff = ten_things.split(" ")
more_stuff = ["Days", "Night", "Song", "Frisbee", 
            "Corn", "Banana", "Girl", "Boy"]

while len(stuff) != 10:
    next_one = more_stuff.pop()
    print("Adding: ", next_one)
    stuff.append(next_one)
    print(f"There are {len(stuff)} items now.")

print("There we go:", stuff)

print("Let's do some things with stuff.")

print(stuff[1])
print(stuff[-1]) # fancy
print(stuff.pop())
print(' '.join(stuff)) # cool right?
print('#'.join(stuff[3:5])) # aint that awesome
