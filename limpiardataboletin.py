import urllib.request
import requests
import time
import re
import webbrowser
import csv
myData = []


contents = urllib.request.urlopen("https://portal.cci-entel.cl/Threat_Intelligence/Boletines/625/").read().decode('utf-8')

urls = re.findall( r'href="([^"]*)', contents)
print(urls)

prefijo = "www.virustotal.com/#/search/"


lista_limpia = list(filter(lambda url: prefijo in url, urls))

lista_ips = list(filter(lambda url: re.match(r"^\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}$",url.replace(prefijo,"")), lista_limpia))

print(lista_ips)

for url in lista_limpia[0:4000]:
	info = url.replace('https://www.virustotal.com/#/search/','')
	print(info)
	for row in info:
		IOC=row

	myData.append(IOC)
	myFile = open('IoCboletin.csv', 'w')
	with myFile:
		writer = csv.writer(myFile)
		writer.writerows(myData)
		