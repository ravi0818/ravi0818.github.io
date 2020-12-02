import csv
import requests
#import pandas as pd
from bs4 import BeautifulSoup
import json
#---------------------------------product1.txt----------------------------
url="https://www.flipkart.com/search?q=phone&sid=tyy%2C4io&as=on&as-show=on&otracker=AS_QueryStore_OrganicAutoSuggest_1_5_na_na_na&otracker1=AS_QueryStore_OrganicAutoSuggest_1_5_na_na_na&as-pos=1&as-type=RECENT&suggestionId=phone%7CMobiles&requestId=64cd63bd-f5ac-4de9-bfd2-dff45ca804a7&as-searchtext=phone"
r=requests.get(url)
#writer=csv.writer(dataFile)
htmlcontent=r.content
soup=BeautifulSoup(htmlcontent,'html.parser')
soup.prettify()
products=[] #List to store name of the product
prices=[] #List to store price of the product
ratings=[] #List to store rating of the product
links=[]
with open("products1.txt","w",encoding="utf-8",newline="") as dataFile:
	for a in soup.find_all(class_='_2kHMtA'):
		name=a.find('div', attrs={'class':'_4rR01T'})
		price=a.find('div', attrs={'class':'_30jeq3 _1_WHN1'})
		rating=a.find('div', attrs={'class':'_3LWZlK'})
		link=a.find('a').get('href')
		#print(rating)
		if rating==None:
			continue
		#-------------
		products.append(name.text)
		prices.append(price.text)
		ratings.append(rating.text)
		links.append("https://flipkart.com"+link)
	#---
	dataFile.write('<table>')
	dataFile.write("".join(['<thead><tr><th>Product Name</th>','<th>Price</th>','<th>Rating</th>','<th>Link</th></tr></thead>']))
	dataFile.write('<tbody>')
	for x in range(len(products)):
		dataFile.write("".join(['<tr><td>',products[x],'</td><td>',prices[x],'</td><td>',ratings[x],'</td><td><a href="',links[x],'"  target="_blank">Open</a></td></tr>']))
	#---
	dataFile.write('</tbody>')
	dataFile.write('</table>')
	
#--------------------------------products2.txt-------------------------------------------
url="https://www.flipkart.com/search?q=laptop&sid=6bo%2Cb5g&as=on&as-show=on&otracker=AS_QueryStore_OrganicAutoSuggest_1_6_na_na_na&otracker1=AS_QueryStore_OrganicAutoSuggest_1_6_na_na_na&as-pos=1&as-type=RECENT&suggestionId=laptop%7CLaptops&requestId=26b633bd-f739-481c-9a7a-4b30978c7dd9&as-searchtext=laptop"
r=requests.get(url)
#writer=csv.writer(dataFile)
htmlcontent=r.content
soup=BeautifulSoup(htmlcontent,'html.parser')
soup.prettify()
products=[] #List to store name of the product
prices=[] #List to store price of the product
ratings=[] #List to store rating of the product
links=[]
with open("products2.txt","w",encoding="utf-8",newline="") as dataFile:
	for a in soup.find_all(class_='_2kHMtA'):
		name=a.find('div', attrs={'class':'_4rR01T'})
		price=a.find('div', attrs={'class':'_30jeq3 _1_WHN1'})
		rating=a.find('div', attrs={'class':'_3LWZlK'})
		link=a.find('a').get('href')
		#print(rating)
		if rating==None:
			continue
		#-------------
		products.append(name.text)
		prices.append(price.text)
		ratings.append(rating.text)
		links.append("https://flipkart.com"+link)
	#---
	dataFile.write('<table>')
	dataFile.write("".join(['<thead><tr><th>Product Name</th>','<th>Price</th>','<th>Rating</th>','<th>Link</th></tr></thead>']))
	dataFile.write('<tbody>')
	for x in range(len(products)):
		dataFile.write("".join(['<tr><td>',products[x],'</td><td>',prices[x],'</td><td>',ratings[x],'</td><td><a href="',links[x],'"  target="_blank">Open</a></td></tr>']))
	#---
	dataFile.write('</tbody>')
	dataFile.write('</table>')


#--------------------------------products3.txt-------------------------------------------
url="https://www.flipkart.com/search?q=camera&sid=jek%2Cp31%2Ctrv&as=on&as-show=on&otracker=AS_QueryStore_OrganicAutoSuggest_2_6_na_na_na&otracker1=AS_QueryStore_OrganicAutoSuggest_2_6_na_na_na&as-pos=2&as-type=RECENT&suggestionId=camera%7CDSLR+Camera&requestId=fed848a8-0861-43df-8cc8-8ddb066d52ad&as-searchtext=camera"
r=requests.get(url)
#writer=csv.writer(dataFile)
htmlcontent=r.content
soup=BeautifulSoup(htmlcontent,'html.parser')
soup.prettify()
products=[] #List to store name of the product
prices=[] #List to store price of the product
ratings=[] #List to store rating of the product
links=[]
with open("products3.txt","w",encoding="utf-8",newline="") as dataFile:
	for a in soup.find_all(class_='_2kHMtA'):
		name=a.find('div', attrs={'class':'_4rR01T'})
		price=a.find('div', attrs={'class':'_30jeq3 _1_WHN1'})
		rating=a.find('div', attrs={'class':'_3LWZlK'})
		link=a.find('a').get('href')
		#print(rating)
		if rating==None:
			continue
		#-------------
		products.append(name.text)
		prices.append(price.text)
		ratings.append(rating.text)
		links.append("https://flipkart.com"+link)
	#---
	dataFile.write('<table>')
	dataFile.write("".join(['<thead><tr><th>Product Name</th>','<th>Price</th>','<th>Rating</th>','<th>Link</th></tr></thead>']))
	dataFile.write('<tbody>')
	for x in range(len(products)):
		dataFile.write("".join(['<tr><td>',products[x],'</td><td>',prices[x],'</td><td>',ratings[x],'</td><td><a href="',links[x],'"  target="_blank">Open</a></td></tr>']))
	#---
	dataFile.write('</tbody>')
	dataFile.write('</table>')