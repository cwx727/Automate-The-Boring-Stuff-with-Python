import requests 
import bs4
url = 'http://ifeve.com/' 
response = requests.get(url) 
soup = bs4.BeautifulSoup(response.text, "lxml") 
a_list = soup.select('a') 

for a in a_list: 
	a_url = a.get('href') 
	try: 
		response = requests.get(a_url) 
		if response.status_code == requests.codes.not_found: 
			print("Page %s is broken link" % a_url) 
		#else: 
			#print("Page %s is other type link" % a_url) 
		
	except: 
		print("Page %s is Error" % a_url)


