import requests
url = 'http://www.baidu.com/s?'
def baidu(wds):
    count = 1
    for wd in wds:
        res = requests.get(url,params={'wd':wd})
        path = 'res%d.txt'%count
        with open(path,'w',encoding='utf8') as f:
           f.write(res.text)
        count +=1
if __name__ == "__main__":
    wds =('Joker','美女','丑女')  
    baidu(wds)  
    
url = '<"res_top_banner .res_top_banner_icon_windows"><a brcg="http://s1.bdstatic.com/r/www/cache/static/global/img/winlogo_e925689.png">'
response = requests.get(url)
res = url.split('<')
print(res)
for url in res:
    if 'brcg' in url:
        res2 = url.split('>')[0]
        print(res2)
        res3 = res2.split('=')
        print(res3)
content = response.content
with open(res,'wb')as f:
    f.write(content)
