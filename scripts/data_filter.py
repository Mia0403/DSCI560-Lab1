from bs4 import BeautifulSoup
import csv

# Reading the html files
with open("../data/raw_data/web_data.html","r",encoding="utf-8") as f:
    #get the contents to BeautifulSoup,html parser is the  RONGQI
    Soup=BeautifulSoup(f,"html.parser")

print("Filtering field")
#store all the data
market_data=[]
#find all the div which class=marketcard
market_cards=Soup.find_all("a",class_="MarketCard-container")
#loop all the data to find the symbol,stockposition,changepct
for card in market_cards:
    symbol=card.find("span",class_="MarketCard-symbol")
    stockposition=card.find("span",class_="MarketCard-stockPosition")
    pct=card.find("span",class_="MarketCard-changesPct" )

    market_data.append([
         symbol.get_text(strip=True) if symbol else "",
         stockposition.get_text(strip=True) if stockposition else"",
         pct.get_text(strip=True) if pct else""
    ])

#write it into the database
print("Store the market data")
with open("../data/processed_data/market_data.csv","w",newline="",encoding="utf-8") as f:
#create a writer
    writer=csv.writer(f)
    writer.writerow(["symbol","stockposition","pct"])
    writer.writerows(market_data)

#Deal the lastest news
news_data=[]
#find all the symbol class=LastestNews
news_items=Soup.find_all("a",class_="LatestNews-headline")

for item in news_items:
    title=item.get_text(strip=True)
    link=item.get("href")
    #find the  timestamp
    time_tag=item.find_previous("time")
    timestamp=time_tag.get_text(strip=True) if time_tag else""
    news_data.append([timestamp,title,link])

#Store the news data
with open("../data/processed_data/news_data.csv","w",newline="",encoding="utf-8") as f:
    writer=csv.writer(f)
    writer.writerow(["timestamp","title","link"])
    writer.writerows(news_data)
print("CSV created")
