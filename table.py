num = int(input())
table = [[]]
table = [[num*i for i in range(1, 11)] for num in range(1, num+1)]
for number in table:
    print(number)
