import html
from urllib.request import urlopen
import re
import requests
import os

saveloc = "C:\\Users\\alw98\\Downloads\\Programming Stuff\\survivorlibrary"
url = "http://www.survivorlibrary.com/index.php/library-download"
print("Starting crawler...")

website = urlopen(url)
print("opened website " + url)

html = website.read().decode('utf-8')
print("read website...")

links = re.findall('"((/index.php/8-category/)(.*?))"', html)
print("found links at " + url)

for link in links:
	categorylink = "http://www.survivorlibrary.com" + link[0]
	category = urlopen(categorylink)
	print("opened categorylink " + categorylink)
	categoryhtml = category.read().decode('utf-8')
	print("read categorylink...")
	pdfs = re.findall('"((/library/)(.*?)(.pdf))', categoryhtml)
	print("got pdf links")
	print("make a dir for the pdfs")
	path = saveloc + "\\" + link[2]
	if not os.path.isdir(path):
		os.makedirs(path)
	print("made dir")
	for pdf in pdfs:
		pdflink = "http://www.survivorlibrary.com" + pdf[0]
		pdfname = pdf[2] + pdf[3]
		fullpath = saveloc + "\\" + link[2] + "\\" + pdfname
		if not os.path.isfile(fullpath):
			print("downloading " + pdfname)
			stream = requests.get(pdflink, stream = True)
			print("got stream...")
			with open(fullpath, 'wb') as f:
				print("opened file")
				f.write(stream.content)
			print(pdfname + " saved at " + saveloc + "\\" + pdfname)
		else:
			print(fullpath + " is already downloaded")