import requests
from bs4 import BeautifulSoup
import selenium
import time
from selenium import webdriver
#---------------------------------product1.txt----------------------------
url="https://www.flipkart.com/dotd-store?=Web&wid=2.dealCard.OMU_1&otracker=clp_omu_Deals%2Bof%2Bthe%2BDay_offers-store_1&otracker1=clp_omu_PINNED_neo%2Fmerchandising_Deals%2Bof%2Bthe%2BDay_NA_wc_view-all_1"
driver = webdriver.Chrome('C:/WebDrivers/chromedriver.exe')
driver.get(url)

# Give the javascript time to render
time.sleep(20)

# Now we have the page, let BeautifulSoup do the rest!
soup = BeautifulSoup(driver.page_source,'html.parser')
soup.prettify()
products=[] #List to store name of the product
prices=[] #List to store price of the product
details=[] #List to store rating of the product
links=[]
images=[]
with open("FDOD.txt","w",encoding="utf-8",newline="") as dataFile:
	for a in soup.find_all(class_='_6WQwDJ'):
		name=a.find('div', attrs={'class':'_3LU4EM'})
		price=a.find('div', attrs={'class':'_2tDhp2'})
		detail=a.find('div', attrs={'class':'_3khuHA'})
		link=a.get('href')
		# print(link)
		img=a.find('img').get('src')
		if name is not None:
			products.append(name.text)
			prices.append(price.text)
			details.append(detail.text)
			images.append(img)
			links.append("https://flipkart.com"+link)
	#---
	# print(links)
	print(len(prices))
	for x in range(len(products)):
		dataFile.write("".join(['<div class="col-lg-2 col-md-4 col-sm-4"><div class="thumbnail"><a href="',links[x],'" target="_blank"><div><img class="center" src="',images[x],'"></div><section class="center">',products[x],'<br>',details[x],'<br>',prices[x],'</section></a></div></div>']))
	#------------------
	print("Done")
	dataFile.close()
	driver.close()

#---------------------------------product1.txt----------------------------
url="https://www.flipkart.com/offers-list/big-steals-of-the-week?screen=dynamic&pk=themeViews%3DBSOW-7Days%3ADealcardDT~widgetType%3DdealCard~contentType%3Dneo&wid=4.dealCard.OMU_3&otracker=clp_omu_Big%2BSteals%2Bof%2Bthe%2BWeek_offers-store_3&otracker1=clp_omu_PINNED_neo%2Fmerchandising_Big%2BSteals%2Bof%2Bthe%2BWeek_NA_wc_view-all_3"
driver = webdriver.Chrome('C:/WebDrivers/chromedriver.exe')
driver.get(url)

# Give the javascript time to render
time.sleep(20)

# Now we have the page, let BeautifulSoup do the rest!
soup = BeautifulSoup(driver.page_source,'html.parser')

soup.prettify()
products=[] #List to store name of the product
prices=[] #List to store price of the product
details=[] #List to store rating of the product
links=[]
images=[]
print("test")
with open("FBSOTW.txt","w",encoding="utf-8",newline="") as dataFile:
	for a in soup.find_all(class_='_6WQwDJ'):
		# print("test")
		name=a.find('div', attrs={'class':'_3LU4EM'})
		price=a.find('div', attrs={'class':'_2tDhp2'})
		detail=a.find('div', attrs={'class':'_3khuHA'})
		link=a.get('href')
		# print(link)
		img=a.find('img').get('src')
		if name is not None:
			products.append(name.text)
			prices.append(price.text)
			if detail is None:
				details.append("NA")
			else:
				details.append(detail.text)
		#---------------
		images.append(img)
		links.append("https://flipkart.com"+link)
	#---
	# print(links)
	print(len(prices))
	for x in range(len(products)):
		dataFile.write("".join(['<div class="col-lg-2 col-md-4 col-sm-4"><div class="thumbnail"><a href="',links[x],'" target="_blank"><div><img class="center" src="',images[x],'"></div><section class="center">',products[x],'<br>',details[x],'<br>',prices[x],'</section></a></div></div>']))
#----
print("Done")
dataFile.close()
driver.quit()




# driver = webdriver.Chrome()  # Optional argument, if not specified will search path.
# driver.get('https://www.flipkart.com/offers-list/top-selling-mobiles?screen=dynamic&pk=themeViews%3DTopsellers-Mobiles-March18%3ADesk~widgetType%3DdealCard~contentType%3Dneo&wid=7.dealCard.OMU_5&otracker=clp_omu_Top%2BSelling%2BMobiles_offers-store_5&otracker1=clp_omu_PINNED_neo%2Fmerchandising_Top%2BSelling%2BMobiles_NA_wc_view-all_5');
# driver.execute_script("window.scrollTo(0, document.body.scrollHeight);var lenOfPage=document.body.scrollHeight;return lenOfPage;")
# print(driver.title)
# s = driver.find_element_by_xpath('//*[@id="container"]/div/div[3]/div/div/div[2]')
# print(s.text)
# # search_box.send_keys('ChromeDriver')
# # search_box.submit()
# time.sleep(25) # Let the user actually see something!
# driver.quit()

# r=requests.get(url)
# #writer=csv.writer(dataFile)
# htmlcontent=r.content
# soup=BeautifulSoup(htmlcontent,'html.parser')
# soup.prettify()
# products=[] #List to store name of the product
# prices=[] #List to store price of the product
# details=[] #List to store rating of the product
# links=[]
# images=[]
# print(soup.find_all('a'))
# with open("FktTopM.txt","w",encoding="utf-8",newline="") as dataFile:
# print(soup.find('a',class_='_6WQwDJ'))
# 	for a in soup.find_all('div',attrs={'class':'_1FNrEw'}):
# 		print("test")
# 		name=a.find('div', attrs={'class':'_3LU4EM'})
# 		price=a.find('div', attrs={'class':'_3khuHA'})
# 		detail=a.find('div', attrs={'class':'_2tDhp2'})
# 		link=a.find('a',attrs={'class':'_6WQwDJ'}).get('href')
# 		img=a.find('img').get("src")
# 		products.append(name.text)
# 		prices.append(price.text)
# 		details.append(detail.text)
# 		images.append(img)
# 		print(img)
# 		links.append("https://flipkart.com"+link)
# 	#---
# 	for x in range(len(products)):
# 		dataFile.write("".join(['<div class="col-lg-2 col-md-4 col-sm-4"><div class="thumbnail"><a href="',link[x],'" target="_blank"><div><img src="',images[x],'"></div><div>',products[x],'</div><div>',details[x],'</div><div>',Prices[x],'</div></a></div></div>']))

