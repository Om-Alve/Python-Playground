height = int(input("Enter the height of the pyramid: "))
i = 1
while i <= height:
    print(" "*(height-i), end="")
    print("* " * i)
    i += 1
