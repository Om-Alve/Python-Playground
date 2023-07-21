with open("first.txt", "w") as file:
    file.write("Hello World!")

with open("first.txt", "r") as file:
    print(str(file.read()))
