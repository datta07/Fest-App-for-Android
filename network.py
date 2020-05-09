import requests
import json

def set_firebase(path,data):
	url1='https://test-bfdc9.firebaseio.com/FestApp/'+path+'/.json'
	if path=='':
		url1='https://test-bfdc9.firebaseio.com/FestApp.json'
	r = json.dumps(data)
	to_database = json.loads(r)
	try:
		requests.patch(url = url1 , json = to_database)
	except Exception as e:
		print(str(e))
		return 0

def get_firebase(path):
	url1='https://test-bfdc9.firebaseio.com/FestApp/'+path+'/.json'
	if path=='':
		url1='https://test-bfdc9.firebaseio.com/FestApp.json'
	auth_key = 'yGTJKpUSKfdIznLem10KAK4dm2fqKHSNMJEzagfh'
	try:
		r1=requests.get(url1 + '?auth=' + auth_key)
		return r1.json()
	except Exception as e:
		print(str(e))
		return 0
 

