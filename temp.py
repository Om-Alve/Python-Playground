myDict = {'ravi': 10, 'rajnish': 9,
          'sanjeev': 15, 'yash': 2, 'suraj': 32}

l = max(myDict.values())
for i in myDict.keys():
    if myDict[i] == l:
        print(i)
        break
