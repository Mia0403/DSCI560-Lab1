import requests
from bs4 import BeautifulSoup
url="https://www.cnbc.com/world/?region=world"
headers={
     "User-Agent":"Mozilla/5.0"
}
html=requests.get(url,headers=headers)
with open("../data/raw_data/web_data.html", "w", encoding="utf-8") as f:
    f.write(html.text)
print("HTML saved")

#make it lool pretty
beautifulsoup=BeautifulSoup(html.text,"html.parser")
with open("../data/raw_data/web_data.html", "w", encoding="utf-8") as f:
    f.write(beautifulsoup.prettify())
print("HTML saved and prettified")
