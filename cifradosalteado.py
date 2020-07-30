import requests
import csv
import time
import hashlib
import random
contador =0

myData =[]
fija='zil@'


with open('newfilename.txt', newline='') as File:
	reader = csv.reader(File)
	#

	for row in reader:
		variable=str(random.randint(0,10000))
		if len(row)>0:
			resumida=row[0]
			unida=fija+variable+resumida
			print(unida)
			h = hashlib.sha256()
			h.update(unida.encode('utf-8'))
			data=h.hexdigest()
			myData.append([data])
		else:
			myData.append([])
	
		myFile = open('encodefilename.txt', 'w')
		with myFile:
			writer = csv.writer(myFile)
			writer.writerows(myData)
