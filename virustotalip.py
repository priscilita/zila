import requests
import csv
import time
myData = [['name','country','list_results','ip']]
api = 'https://www.virustotal.com/vtapi/v2/ip-address/report'
apigui='https://www.virustotal.com/ui/ip_addresses/'
contador =0 
with open('zbot.csv', newline='') as File:
	reader = csv.reader(File)
	for row in reader:
		ip=row[0]
		if ':' in ip:
			casi_limpia=ip.split(':')
			ip=(casi_limpia[0])

		response_engines = requests.get(apigui+ip)
		json=response_engines.json()

		if 'data' in json:
			if 'attributes' in json['data']:
				if 'as_owner' in json['data']['attributes']:
					name = json['data']['attributes']['as_owner']
				else:
					name ='null'
				if 'country' in json['data']['attributes']:	
					country = json['data']['attributes']['country']
				else:
					country ='null'

				if 'last_analysis_stats' in json['data']['attributes']:
					if 'malicious' in json['data']['attributes']['last_analysis_stats']:
						list_results = json['data']['attributes']['last_analysis_stats']['malicious']
					else:
						last_analysis_stats ='null'
						#print(list_results)
					myData.append([name,country, list_results, ip])
		else :
			print(json)

		contador = contador + 1
		print(contador)
		
		myFile = open('iplucifer01.csv', 'w')
		with myFile:
			writer = csv.writer(myFile)
			writer.writerows(myData)
		if contador%30==0:
			time.sleep(60)