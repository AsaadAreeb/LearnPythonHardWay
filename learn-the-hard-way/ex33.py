def list_appender(goto, incrementer):
    i = 0
    numbers = []

    while i < goto:
        print(f"At the top i is {i}")
        numbers.append(i)

        i = i + incrementer
        print("Numbers now:", numbers)
        print(f"At the bottom i is {i}")
    return numbers

list = list_appender(int(input("> ")), int(input("> ")))

for i in list:
    print(f">> {i}\n")