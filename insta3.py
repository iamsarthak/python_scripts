import requests
import json
query='stanford university'
TOKEN='1257820698.1fb234f.2c34cf637f7f41dbaec58589af50eded'
url = 'https://api.instagram.com/v1/tags/search?q=' +query  
parameters = {'access_token': TOKEN}
r = requests.get(url, params=parameters)
result = json.loads(r.text)
count=0
for res in result['data']:
	count=count+1
	if(count<=5):
		print('name of the hashtag is '+ res['name'] + ' and number of related media is '+str(res['media_count']))
	else:
		break	

