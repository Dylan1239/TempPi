#pip install requests
#pip install json

import requests
#import json


urlPost =  "" 


def postData(json_Data):
	r=requests.post(urlPostjsonData, json_Data)
	if r.status_code == requests.codes.ok:
		print("ok")
		print(str(r.status_code))
		return r.status_code
	else: 
		print("not ok")
		print(str(r.status_code))
		return r.status_code


def formatJson(piId,sensorId,dateTime, temp):
	
	json_data = {"deviceId":piId,"sensorId": sensorId,"event_occurred":dateTime,"temp":temp}
	#print json.dumps(json_data)	
	return json_data
