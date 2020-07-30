import requests
import csv
import time
import hashlib
myData =[['sha256','md5','name_archivo','resultado','Antivirus_Panda','Antivirus','tipo']]
apigui='https://www.virustotal.com/ui/search?relationships%5Bcomment%5D=author%2Citem&relationships%5Burl%5D=network_location%2Clast_serving_ip_address&limit=20&query='
contador =0
with open('zbot.csv', newline='') as File:
    reader = csv.reader(File)
    for row in reader:
        sha256=row[0]
        response_engines = requests.get(apigui+sha256)
        json=response_engines.json()

        if 'data' in json and len(json['data']) > 0:
            if 'attributes' in json['data'][0]:
                if 'md5' in json['data'][0]['attributes']:
                    md5 = json['data'][0]['attributes']['md5']
                
            if 'meaningful_name' in json['data'][0]['attributes']:
                name_archivo = json['data'][0]['attributes']['meaningful_name']
            if 'last_analysis_results' in json['data'][0]['attributes']:
                Antivirus_Panda= json['data'][0]['attributes']['last_analysis_results']['Panda']['category']
                Antivirus= json['data'][0]['attributes']['last_analysis_results']['Panda']['engine_name']
                tipo= json['data'][0]['attributes']['last_analysis_results']['Panda']['result']
            if 'last_analysis_stats' in json['data'][0]['attributes']:
                resultado= json['data'][0]['attributes']['last_analysis_stats']['malicious']
                    #print(resultado
                #print(md5)
                #print(meaningful_name)
        else:
            md5 = 'null'
            name_archivo = 'null'
            Antivirus_Panda= 'null'
            Antivirus = 'null'
            resultado= 'null'
            tipo = 'null'
            print(json)
        myData.append([sha256,md5,name_archivo,resultado,Antivirus_Panda,Antivirus,tipo])
        contador = contador + 1
        print(contador)
        

        myFile = open('hashiocemotet03.csv', 'w')
        with myFile:
            writer = csv.writer(myFile)
            writer.writerows(myData) 
        if contador%30==0:
            time.sleep(60)
            
        