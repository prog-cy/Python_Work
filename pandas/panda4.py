import pandas as pd
import html5lib

link = "C:\\Users\\rupes\\Desktop\\WEBDEV\\Basic\\prog10.html"

data = pd.read_html(link)
print(data)