import requests
from bs4 import BeautifulSoup
import selenium
import time
from selenium import webdriver
#---------------------------------amz1.txt----------------------------
url="https://www.amazon.in/gp/goldbox/ref=gbps_fcr_s-5_859c_wht_97641903?gb_f_c2xvdC01=dealTypes:LIGHTNING_DEAL%252CBEST_DEAL,includedAccessTypes:KINDLE_CONTENT_DEAL,sortOrder:BY_SCORE,enforcedCategories:976442031&pf_rd_p=daa47517-5bef-4e97-b82e-ec3e7d37859c&pf_rd_s=slot-5&pf_rd_t=701&pf_rd_i=gb_main&pf_rd_m=A1VBAL9TL5WCBF&pf_rd_r=78QH33Z82NW25NM35BD8&ie=UTF8"
driver = webdriver.Chrome('C:/WebDrivers/chromedriver.exe')
driver.get(url)

# Give the javascript time to render
time.sleep(20)

# Now we have the page, let BeautifulSoup do the rest!
soup = BeautifulSoup(driver.page_source,'html.parser')

soup.prettify()
products=[] #List to store name of the product
prices=[] #List to store price of the product
ratings=[] #List to store rating of the product
links=[]
images=[]
#soup=soup.find('div',attrs={'id':'widgetContent'})
with open("ATDH.txt","w",encoding="utf-8",newline="") as dataFile:
	for a in soup.find_all('div',class_='dealTile'):
		if a.find('span',id="shipSoldInfo") is None:
			continue
		#------------------------------
		image=a.find('img').get('src')
		link=a.find('a')
		name=a.find('span',class_='a-declarative')
		price=a.find('div',class_='priceBlock')
		rating=a.find('span',class_='a-icon-alt')
		#----------------------
		if name is not None:
			link=link.get('href')
			link=link.split("/")
			if link[4]=='dp':
				link=link[5]
				print(link)
			else:
				continue
			#-----------------
			products.append(name.text)
			images.append(image)
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
	#----------------------------------------------
	for x in range(len(products)):
		dataFile.write("".join(['<div class="col-lg-2 col-md-4 col-sm-4"><div class="thumbnail"><a href="',links[x],'" target="_blank"><div><img class="center" src="',images[x],'"></div><section class="center">',products[x],'<br>',ratings[x],'<br></section></a><div class="price">',prices[x],'</div></div></div>']))
	#------------------
	print("Done")
	dataFile.close()
	driver.close()

#---------------------------------amz1.txt----------------------------
url="https://www.amazon.in/gp/goldbox/ref=gbps_ftr_s-5_859c_wht_97641903?gb_f_c2xvdC01=dealTypes:LIGHTNING_DEAL%252CBEST_DEAL,includedAccessTypes:KINDLE_CONTENT_DEAL,sortOrder:BY_SCORE,enforcedCategories:976419031&pf_rd_p=daa47517-5bef-4e97-b82e-ec3e7d37859c&pf_rd_s=slot-5&pf_rd_t=701&pf_rd_i=gb_main&pf_rd_m=A1VBAL9TL5WCBF&pf_rd_r=78QH33Z82NW25NM35BD8&ie=UTF8"
driver = webdriver.Chrome('C:/WebDrivers/chromedriver.exe')
driver.get(url)

# Give the javascript time to render
time.sleep(20)

# Now we have the page, let BeautifulSoup do the rest!
soup = BeautifulSoup(driver.page_source,'html.parser')

soup.prettify()
products=[] #List to store name of the product
prices=[] #List to store price of the product
ratings=[] #List to store rating of the product
links=[]
images=[]
#soup=soup.find('div',attrs={'id':'widgetContent'})
with open("ATDE.txt","w",encoding="utf-8",newline="") as dataFile:
	for a in soup.find_all('div',class_='dealTile'):
		if a.find('span',id="shipSoldInfo") is None:
			continue
		#------------------------------
		image=a.find('img').get('src')
		link=a.find('a')
		name=a.find('span',class_='a-declarative')
		price=a.find('div',class_='priceBlock')
		rating=a.find('span',class_='a-icon-alt')
		#----------------------
		if name is not None:
			link=link.get('href')
			link=link.split("/")
			if link[4]=='dp':
				link=link[5]
				print(link)
			else:
				continue
			#-----------------
			products.append(name.text)
			images.append(image)
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
	#----------------------------------------------
	for x in range(len(products)):
		dataFile.write("".join(['<div class="col-lg-2 col-md-4 col-sm-4"><div class="thumbnail"><a href="',links[x],'" target="_blank"><div><img class="center" src="',images[x],'"></div><section class="center">',products[x],'<br>',ratings[x],'<br></section></a><div class="price">',prices[x],'</div></div></div>']))
	#------------------
	print("Done")
	dataFile.close()
	driver.close()