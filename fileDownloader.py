import requests
import math
url = "https://www.africau.edu/images/default/sample.pdf"

chunk_size = 256

data = requests.get(url)

with open("file.pdf", "wb") as file:
    for chunk in data.iter_content(chunk_size=chunk_size):
        file.write(chunk)
