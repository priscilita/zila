import requests
import csv
import time
import hashlib
myData = [['list_results', 'url']]



def hash_string(string):
	return hashlib.sha256(string.encode('utf-8')).hexdigest()
	

apigui='https://www.virustotal.com/ui/urls/'
apinext='?relationships=last_serving_ip_address,network_location'
contador =0 
with open('zbot.csv', newline='') as File:
	reader = csv.reader(File)
	for row in reader:
		url=row[0]
		sha256=hash_string(url)

		response_engines = requests.get(apigui+sha256+apinext)
		json=response_engines.json()

		if 'data' in json:
			if 'attributes' in json['data']:
				if 'last_analysis_stats' in json['data']['attributes']:
					list_results = json['data']['attributes']['last_analysis_stats']['malicious']
						#print(list_results)
					myData.append([list_results,url])
		else :
				print(json)

		contador = contador + 1
		print(contador)
		myFile = open('emoteturl01.csv', 'w')
		with myFile:
			writer = csv.writer(myFile)
			writer.writerows(myData)
		if contador%30==0:
			time.sleep(60)