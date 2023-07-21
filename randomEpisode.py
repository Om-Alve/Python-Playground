import os
import random
import os

path = 'C:\CS50x'

os.chdir(path)

episode = random.choice(os.listdir(path))
print(episode)

epPath = str(os.path.realpath(episode))
print(epPath)

os.system("start " + epPath)
