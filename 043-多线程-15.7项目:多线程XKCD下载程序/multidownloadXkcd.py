import threading, time, os, requests, bs4

os.makedirs('xkcd', exist_ok=True)

def downloadXkcd(startComic, endComic):
	for urlNumber in range(startComic, endComic):
		print('Downloading page http://xkcd.com/%s...' % (urlNumber))
		res = requests.get('http://xkcd.com/%s' %(urlNumber))
		res.raise_for_status()
		
		soup = bs4.BeautifulSoup(res.text)
		
		comicElem = soup.select('#comic img')
		
		if comicElem == []:
			print('Could not find comic image.')
		else:
			comicUrl = 'http:' + comicElem[0].get('src')
			print('Downloading image %s...' %(comicUrl))
			
			res = requests.get(comicUrl)
			res.raise_for_status()
			
			imageFile = open(os.path.join('xkcd', os.path.basename(comicUrl)), 'wb')
			for chunk in res.iter_content(100000):  #将一段图像数据写入文件（每次最多10 万字节）
				imageFile.write(chunk)
			
			imageFile.close()
			
downloadThreads = []
for i in range(1, 300, 100):
	downloadThread = threading.Thread(target=downloadXkcd, args=(i, i+2))
	downloadThreads.append(downloadThread)
	downloadThread.start()
	
for downloadThread in downloadThreads:#调用 Thread 对象 join()方法将阻塞，直到该线程完成。
	downloadThread.join()
print('Done.')
