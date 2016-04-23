import requests
from bs4 import BeautifulSoup
search_query="stanford university";
i=requests.get("https://www.youtube.com/results?q="+search_query+"&sp=CAM%253D")
soup=BeautifulSoup(i.text)
youtubelinks=soup.find_all("a")
count=0;
super_count=0;
listofhref=[];	
for links in youtubelinks:
	youtubehref=links.get('href')
	youtubehrefstring=str(youtubehref)
	if "/watch?v=" in youtubehrefstring:
		if youtubehrefstring not in listofhref:		
			listofhref.append(youtubehrefstring)
			super_count=super_count+1
			if(super_count<=3):
				print("the link to the  video is which is sorted according to rating "+"www.youtube.com"+youtubehrefstring)
				for s in youtubehrefstring:
					count=count+1;
					if s=="=":
						embedlink="https://www.youtube.com/embed/"+youtubehrefstring[count:]
						print('<iframe width="420" height="315" src="'+embedlink+'"frameborder="0" allowfullscreen></iframe>')
