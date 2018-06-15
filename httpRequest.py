import requests
#import json

urlPost ="http://34.239.113.101:8080/demo/temps"
urlLocal ="http://" 

def postData(json_Data):
	r = requests.post(urlPost,json= json_Data)
	print("in Post")
	if r.status_code == requests.codes.ok:
		print ("OK")
		print (str(r.status_code))
		return r.status_code
	else:
		print("Not OK")
		print(str(r.status_code))
		return r.status_code

def formatJson(piId,sensorId, dateTime, temperature, humidity):

	json_data = {"DeviceId":piId,"SensorId":sensorId,"EventOccured":str(dateTime),"Temperature":temperature,"Humidity":humidity}
#	Json.dumps(json_data)
	return json_data
