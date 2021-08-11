import pandas as pd
import html5lib

from bs4 import BeautifulSoup

link = "C:\\Users\\Rupesh Kumar Dwivedi\\Desktop\\Document\\HTML\\table.html"

data = pd.read_html(link)
print(data)