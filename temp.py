import csv
import requests
#import pandas as pd
from bs4 import BeautifulSoup
import json
#-------------------------------products.csv----------------------------------------------
url="https://www.flipkart.com/search?q=realme+7+pro&sid=tyy%2C4io&as=on&as-show=on&otracker=AS_QueryStore_OrganicAutoSuggest_2_12_na_na_ps&otracker1=AS_QueryStore_OrganicAutoSuggest_2_12_na_na_ps&as-pos=2&as-type=RECENT&suggestionId=realme+7+pro%7CMobiles&requestId=f33d392b-5393-40b0-a703-3c247fc1cd20&as-searchtext=realme%207%20pro"
r=requests.get(url)
csvFile=open("products.csv","wt",encoding="utf-8",newline="")
writer=csv.writer(csvFile)
htmlcontent=r.content
soup=BeautifulSoup(htmlcontent,'html.parser')
#print(soup.title)
#writer.writerow(soup.title)
#temp=soup.select('._4rR01T')
#print(temp)
#print("")
#details=soup.find_all(class_='_4rR01T')
#rating=soup.find_all(class_='_3LWZlK')
#content = driver.page_source
products=[] #List to store name of the product
prices=[] #List to store price of the product
ratings=[] #List to store rating of the product

for a in soup.find_all(class_='_2kHMtA'):
	name=a.find('div', attrs={'class':'_4rR01T'})
	price=a.find('div', attrs={'class':'_30jeq3 _1_WHN1'})
	rating=a.find('div', attrs={'class':'_3LWZlK'})
	#print(price)
	products.append(name.text)
	prices.append(price.text)
	ratings.append(rating.text)
#---
writer.writerow('<table>')
writer.writerow(['<th>Product Name</th>','<th>Price</th>','<th>Rating</th>'])
for x in range(len(products)):
	writer.writerow(['<tr><td>',products[x],'</td><td>',prices[x],'</td>,<td>',ratings[x],'</td></tr>'])
#---
writer.writerow('</table>')
#-----------------------data.txt---------------------------
# url="https://github.com/ravi0818/Web/blob/main/products.csv"
# r=requests.get(url)
# dataFile=open("data.txt","wt",encoding="utf-8",newline="")
# #writer=csv.writer(dataFile)
# htmlcontent=r.content
# soup=BeautifulSoup(htmlcontent,'html.parser')
# d=soup.find(class_="markdown-body")
# #print(d)
# dataFile.write(str(d))

