import requests
import csv
import time
import hashlib
myData = [['list_results', 'url']]



def hash_string(string):
	return hashlib.sha256(string.encode('utf-8')).hexdigest()
	

apigui='https://www.virustotal.com/ui/search?relationships%5Bcomment%5D=author%2Citem&relationships%5Burl%5D=network_location%2Clast_serving_ip_address&limit=20&query='
#'https://www.virustotal.com/ui/domains/'
#apinext='/urls'
contador =0 
with open('zbot.csv', newline='') as File:
	reader = csv.reader(File)
	for row in reader:
		url=row[0]
		#sha256=hash_string(url)
		#print(url)

		response_engines = requests.get(apigui+url)
		json=response_engines.json()

		
		if 'data' in json and len(json['data']) > 0:
			if 'attributes' in json['data'][0]:

				if 'last_analysis_stats' in json['data'][0]['attributes']:
					list_results = json['data'][0]['attributes']['last_analysis_stats']['malicious']
						#print(list_results)
					myData.append([list_results,url])
		else :
				print(json)

		contador = contador + 1
		print(contador)
		
		myFile = open('emotetdomain01.csv', 'w')
		with myFile:
			writer = csv.writer(myFile)
			writer.writerows(myData)
		if contador%30==0:
			time.sleep(60)