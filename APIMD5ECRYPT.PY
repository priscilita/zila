import requests
import csv
import time
import hashlib
contador =0

myData =[]
code=''  [credenciales de md5decrypt.net]
email='' [correo] 
hash_type='md5'
apigui='https://md5decrypt.net/en/Api/api.php?code='+code+'&email='+email+'&hash_type='+hash_type+'&hash='



contador =0

with open('filename.txt', newline='') as File:
	reader = csv.reader(File)
	#

	for row in reader:
		hashes = row[0].split(' ')
		for fila in hashes:
			info=fila
			response_engines = requests.get(apigui+info)
			response = str(response_engines.content, 'utf-8').replace('\n','')
			print(response)
			#print(len(response))
			if len(response)==0:
				myData.append([])
			else:
				myData.append([response])
			myFile = open('zila.txt', 'w')
			with myFile:
				writer = csv.writer(myFile)
				writer.writerows(myData)
