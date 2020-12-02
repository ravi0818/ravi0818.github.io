import csv
import requests
#import pandas as pd
from bs4 import BeautifulSoup
import json
#---------------------------------amz1.txt----------------------------
url="https://amzn.to/3muga3B"
r=requests.get(url)
#writer=csv.writer(dataFile)
htmlcontent=r.content
soup=BeautifulSoup(htmlcontent,'html.parser')
soup.prettify()
#soup.encode("utf-8")
products=[] #List to store name of the product
prices=[] #List to store price of the product
ratings=[] #List to store rating of the product
links=[]
images=[]
with open("amz1.txt","w",encoding="utf-8",newline="") as dataFile:
	#for a in soup.find_all('div',attrs={'class':'sg-col-inner'}):
	for a in soup.find_all('div',attrs={'class':'s-asin'}):
		name=a.find('h2')
		price=a.find('span', attrs={'class':'a-offscreen'})
		rating=a.find('span', attrs={'class':'a-icon-alt'})
		link=name.find('a').get('href')
		link=link.split("dp/")
		link=link[1]
		link=link[:10]
		links.append("https://www.amazon.in/gp/product/"+link+"/?tag=ravi18-21")
		#---------
		# if name is not None:
		products.append(name.text)
		#-------------------------------
		# if price is not None:
		prices.append(price.text)
		#--------------------------------
		# if rating is not None:
		ratings.append(rating.text)

	#---------------------------
	dataFile.write('<table>')
	dataFile.write("".join(['<thead><tr><th>Product Name</th>','<th>Price</th>','<th>Rating</th>','<th>Link</td></tr></thead>']))
	dataFile.write('<tbody>')
	for x in range(len(products)):
		dataFile.write("".join(['<tr><td>',products[x],'</td><td>',prices[x],'</td><td>',ratings[x],'</td><td><a href="',links[x],'"  target="_blank">Open</a></td></tr>']))
	#---------------------------
	dataFile.write('</tbody>')
	dataFile.write('</table>')
