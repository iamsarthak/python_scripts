import os
import requests
from bs4 import BeautifulSoup
from urllib.parse import urljoin
import sys
def download(url):
    domain = url.split('//')[-1].split('/')[0]
    os.makedirs(domain)
    response = requests.get(url)
    if response.status_code != 200:
        return
    soup = BeautifulSoup(response.text)
    img_tags = soup.find_all('img')
    img_src_paths = set()
    for i in img_tags:
        src = i.get('src')
        if not src:
            continue
        if src[:7] == 'http://' or src[:8] == 'https://':
            img_src_paths.add(src)
        else:
            img_src_paths.add(urljoin(url, src))
    i = 0
    for img_url in img_src_paths:
        try:
            re = requests.get(img_url)
        except:
            continue
        i  = i + 1
        filename = str(i) + "." + img_url.split('.')[-1]
        f = open(domain+'/'+filename, 'wb')
        f.write(re.content)
        f.close()

if __name__ == '__main__':
    if len(sys.argv) < 2:
        print("Enter a website url to fetch images")
    else:
        download(sys.argv[1])
