import requests, os, bs4

url = 'https://imgur.com/search?q=cat'
os.makedirs('imgur', exist_ok=True)

print('Downloading Page %s...' %url)
res = requests.get(url)
res.raise_for_status()
soup = bs4.BeautifulSoup(res.text)

if soup == []:
	print("Could not find comic image.")
else:
	imageCats = soup.select('img[alt]')
	for i in range(len(imageCats)):
		imageCat = imageCats[i].get('src')
		#print(imageCat)
		imageCatUrl = 'http:' + imageCat
		print(imageCatUrl)

		# TODO: Download the image.
		print('Downloading image %s...' %imageCatUrl)
		res = requests.get(imageCatUrl)
		res.raise_for_status()


		# TODO: Save the image to ./imgur.
		imageFile = open(os.path.join('imgur', os.path.basename(imageCatUrl)), 'wb')
		for chunk in res.iter_content(100000):
			imageFile.write(chunk)
		imageFile.close()


print('Done.')

