import requests
url = 'http://www.image-net.org/api/text/imagenet.synset.get'
response = requests.get(url)
HTML = response.text
URLS = HTML.split('\n')

for url in URLS:
    response = requests.get(url)
    content = response.content
    name = url.split('/')[-1]
    with open(name,'wb') as f:
        f.write(content)