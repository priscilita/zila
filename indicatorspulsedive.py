import requests
import csv
import re
import json
import certifi

myData = [['tipo','IOC','riesgo']]


apigui='https://pulsedive.com/api/info.php?indicator='
apinext='&pretty=1&key=key'
contador =0 
with open('pulsebot.csv', newline='') as File:
	reader = csv.reader(File)
	for row in reader:
		url=row[0]
		

		response_engines = requests.get(apigui+url+apinext)
		json=response_engines.json()
		#print(json)

		if 'type' in json :
			tipo =json['type']
		if 'indicator' in json :
			IOC =json['indicator']
		if 'risk' in json :
			riesgo = json['risk']
		myData.append([tipo,IOC,riesgo])
		contador = contador + 1
		print(contador)
		myFile = open('Rpulse.csv', 'w')
		with myFile:
			writer = csv.writer(myFile)
			writer.writerows(myData) 
		if contador%30==0:
			time.sleep(60)
