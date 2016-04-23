import requests
import json
TAGS='harvard'
FORMAT='json'
METHOD='flickr.photos.search'

KEY='637f99c7944fc94332b8c1159443edb0'

url='https://api.flickr.com/services/rest/?'+'method='+METHOD
parameters={'api_key':KEY,'tags':TAGS,'format':FORMAT}
r = requests.get(url,params=parameters)
result = r.text
print(result[50])
