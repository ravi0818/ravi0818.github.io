from selenium import webdriver
from bs4 import BeautifulSoup

#--------------------------------------TopM.txt-------------------------------------------
url="https://www.flipkart.com/offers-list/top-selling-mobiles?screen=dynamic&pk=themeViews%3DTopsellers-Mobiles-March18%3ADesk~widgetType%3DdealCard~contentType%3Dneo&wid=7.dealCard.OMU_5&otracker=clp_omu_Top%2BSelling%2BMobiles_offers-store_5&otracker1=clp_omu_PINNED_neo%2Fmerchandising_Top%2BSelling%2BMobiles_NA_wc_view-all_5"
driver = webdriver.PhantomJS()
driver.get(url)
htmlcontent=driver.page_source

# r=requests.get(url)
# #writer=csv.writer(dataFile)
# htmlcontent=r.content
soup=BeautifulSoup(htmlcontent,'html.parser')
# soup.prettify()
# products=[] #List to store name of the product
# prices=[] #List to store price of the product
# details=[] #List to store rating of the product
# links=[]
# images=[]
# print(soup.find_all('a'))
# with open("FktTopM.txt","w",encoding="utf-8",newline="") as dataFile:
print(soup.find('a',class_='_6WQwDJ'))
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

