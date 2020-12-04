import csv
import requests
#import pandas as pd
from bs4 import BeautifulSoup
import json
#---------------------------------amzBE.txt----------------------------
url="https://www.amazon.in/gp/bestsellers/electronics/ref=zg_bs_nav_0"
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
#soup=soup.find('div',attrs={'id':'widgetContent'})
print("hello")
with open("amzBE.txt","w",encoding="utf-8",newline="") as dataFile:
	for a in soup.find_all('span',class_='aok-inline-block zg-item'):
		image=a.find('img').get('src')
		name=a.find('a',class_='a-link-normal')
		price=a.find('span',class_='p13n-sc-price')
		rating=a.find('span',class_='a-icon-alt')
		#----------------------
		if name is not None:
			products.append(name.text)
			images.append(image)
			link=name.get('href')
			link=link.split("dp/")
			link=link[1]
			link=link[:10]
			links.append("https://www.amazon.in/gp/product/"+link+"/?tag=ravi18-21")
			if price is None:
				prices.append("NA")
			else:
				prices.append(price.text)
			#
			if rating is None:
				ratings.append("NA")
			else:
				ratings.append(rating.text)
	#----------------------
	print(len(products))
	print(len(prices))
	dataFile.write('<table>')
	dataFile.write("".join(['<thead><tr><th>Product Image</th>','<th>Product Name</th>','<th>Price</th>','<th>Rating</th></tr></thead>']))
	dataFile.write('<tbody>')
	for x in range(len(products)):
		dataFile.write("".join(['<tr><td><img src="',images[x],'"></td><td>','<a href="',links[x],'" target="_blank">',products[x],'</a>','</td><td class="price">',prices[x],'</td><td>',ratings[x],'</td></tr>']))
	#---------------------------
	dataFile.write('</tbody>')
	dataFile.write('</table>')

#---------------------------------amzBH.txt----------------------------
url="https://www.amazon.in/gp/bestsellers/kitchen/ref=zg_bs_nav_0"
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
#soup=soup.find('div',attrs={'id':'widgetContent'})
print("hello")
with open("amzBH.txt","w",encoding="utf-8",newline="") as dataFile:
	for a in soup.find_all('span',class_='aok-inline-block zg-item'):
		image=a.find('img').get('src')
		name=a.find('a',class_='a-link-normal')
		price=a.find('span',class_='p13n-sc-price')
		rating=a.find('span',class_='a-icon-alt')
		#----------------------
		if name is not None:
			products.append(name.text)
			images.append(image)
			link=name.get('href')
			link=link.split("dp/")
			link=link[1]
			link=link[:10]
			links.append("https://www.amazon.in/gp/product/"+link+"/?tag=ravi18-21")
			if price is None:
				prices.append("NA")
			else:
				prices.append(price.text)
			#
			if rating is None:
				ratings.append("NA")
			else:
				ratings.append(rating.text)
	#----------------------
	print(len(products))
	print(len(prices))
	dataFile.write('<table>')
	dataFile.write("".join(['<thead><tr><th>Product Image</th>','<th>Product Name</th>','<th>Price</th>','<th>Rating</th></tr></thead>']))
	dataFile.write('<tbody>')
	for x in range(len(products)):
		dataFile.write("".join(['<tr><td><img src="',images[x],'"></td><td>','<a href="',links[x],'" target="_blank">',products[x],'</a>','</td><td class="price">',prices[x],'</td><td>',ratings[x],'</td></tr>']))
	#---------------------------
	dataFile.write('</tbody>')
	dataFile.write('</table>')

#---------------------------------amzBCA.txt----------------------------
url="https://www.amazon.in/gp/bestsellers/computers/ref=zg_bs_nav_0"
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
#soup=soup.find('div',attrs={'id':'widgetContent'})
print("hello")
with open("amzBCA.txt","w",encoding="utf-8",newline="") as dataFile:
	for a in soup.find_all('span',class_='aok-inline-block zg-item'):
		image=a.find('img').get('src')
		name=a.find('a',class_='a-link-normal')
		price=a.find('span',class_='p13n-sc-price')
		rating=a.find('span',class_='a-icon-alt')
		#----------------------
		if name is not None:
			products.append(name.text)
			images.append(image)
			link=name.get('href')
			link=link.split("dp/")
			link=link[1]
			link=link[:10]
			links.append("https://www.amazon.in/gp/product/"+link+"/?tag=ravi18-21")
			if price is None:
				prices.append("NA")
			else:
				prices.append(price.text)
			#
			if rating is None:
				ratings.append("NA")
			else:
				ratings.append(rating.text)
	#----------------------
	print(len(products))
	print(len(prices))
	dataFile.write('<table>')
	dataFile.write("".join(['<thead><tr><th>Product Image</th>','<th>Product Name</th>','<th>Price</th>','<th>Rating</th></tr></thead>']))
	dataFile.write('<tbody>')
	for x in range(len(products)):
		dataFile.write("".join(['<tr><td><img src="',images[x],'"></td><td>','<a href="',links[x],'" target="_blank">',products[x],'</a>','</td><td class="price">',prices[x],'</td><td>',ratings[x],'</td></tr>']))
	#---------------------------
	dataFile.write('</tbody>')
	dataFile.write('</table>')



#---------------------------------amzBB.txt----------------------------
url="https://www.amazon.in/gp/bestsellers/books/ref=zg_bs_nav_0"
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
#soup=soup.find('div',attrs={'id':'widgetContent'})
print("hello")
with open("amzBB.txt","w",encoding="utf-8",newline="") as dataFile:
	for a in soup.find_all('span',class_='aok-inline-block zg-item'):
		image=a.find('img').get('src')
		name=a.find('a',class_='a-link-normal')
		price=a.find('span',class_='p13n-sc-price')
		rating=a.find('span',class_='a-icon-alt')
		#----------------------
		if name is not None:
			products.append(name.text)
			images.append(image)
			link=name.get('href')
			link=link.split("dp/")
			link=link[1]
			link=link[:10]
			links.append("https://www.amazon.in/gp/product/"+link+"/?tag=ravi18-21")
			if price is None:
				prices.append("NA")
			else:
				prices.append(price.text)
			#
			if rating is None:
				ratings.append("NA")
			else:
				ratings.append(rating.text)
	#----------------------
	print(len(products))
	print(len(prices))
	dataFile.write('<table>')
	dataFile.write("".join(['<thead><tr><th>Product Image</th>','<th>Product Name</th>','<th>Price</th>','<th>Rating</th></tr></thead>']))
	dataFile.write('<tbody>')
	for x in range(len(products)):
		dataFile.write("".join(['<tr><td><img src="',images[x],'"></td><td>','<a href="',links[x],'" target="_blank">',products[x],'</a>','</td><td class="price">',prices[x],'</td><td>',ratings[x],'</td></tr>']))
	#---------------------------
	dataFile.write('</tbody>')
	dataFile.write('</table>')
