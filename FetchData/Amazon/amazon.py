import csv
import requests
#import pandas as pd
from bs4 import BeautifulSoup
import json
#---------------------------------amz1.txt----------------------------
url="https://www.amazon.in/gp/goldbox/ref=gbps_ftr_s-5_859c_sort_RELV?gb_f_IN_BB_Deals_PC_Al_Customers=dealStates:AVAILABLE%252CWAITLIST%252CWAITLISTFULL%252CUPCOMING,dealTypes:DEAL_OF_THE_DAY,page:3,sortOrder:BY_SCORE,MARKETING_ID:Marvolo_gaunt%252CGIF20_BB_GW%252CBB_JUP20,dealsPerPage:6&pf_rd_p=daa47517-5bef-4e97-b82e-ec3e7d37859c&pf_rd_s=slot-5&pf_rd_t=701&pf_rd_i=gb_main&pf_rd_m=A1VBAL9TL5WCBF&pf_rd_r=NGG03KPEJVEX6YBQ3XV5&gb_f_c2xvdC01=dealTypes:LIGHTNING_DEAL%252CBEST_DEAL,includedAccessTypes:KINDLE_CONTENT_DEAL,sortOrder:BY_SCORE&ie=UTF8"
r=requests.get(url)
#writer=csv.writer(dataFile)
htmlcontent=r.content
soup=BeautifulSoup(htmlcontent,'html.parser')
soup.prettify()
s=soup.find_all(id='100_dealView_0')
print(s)
#soup.encode("utf-8")
products=[] #List to store name of the product
prices=[] #List to store price of the product
ratings=[] #List to store rating of the product
links=[]
images=[]
with open("amz1.txt","w",encoding="utf-8",newline="") as dataFile:
	for a in soup.find_all('div',attrs={'class':'a-section dealContainer'}):
		print(a.find('a'))

	#---------------------------
	dataFile.write('<table>')
	dataFile.write("".join(['<thead><tr><th>Product Name</th>','<th>Price</th>','<th>Rating</th>','<th>Link</td></tr></thead>']))
	dataFile.write('<tbody>')
	for x in range(len(products)):
		dataFile.write("".join(['<tr><td>',products[x],'</td><td>',prices[x],'</td><td>',ratings[x],'</td><td><a href="',links[x],'"  target="_blank">Open</a></td></tr>']))
	#---------------------------
	dataFile.write('</tbody>')
	dataFile.write('</table>')
