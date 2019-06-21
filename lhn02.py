proxy_handle = {
    'http':'183.51.190.51:33913',
    'http':'122.193.245.44:9999'
}
proxy = urllib.request.ProxyHandler(proxy_handle)
opener = urllib.request.build_opener(proxy)
request = urllib.request.Request(url=url)
response = urllib.request.urlopen(request)
print(response.read().decode('utf8'))
while 1:
    print(response.status)
    # print(proxy_handle)    
    if (response.status != 200):
        print('爬虫失败')
    break



    import http.cookiejar,urllib.request
    cookie = http.cookiejar.Cookiejar()
    handler = urllib.request.HTTPCookieProcessor(cookie)
    opener = urllib.request.build_opener(handler)
    response = opener.open('http://www.17k.com/chapter/2933095/36699279.htm')
    for item in cookie:
        print(item.name+'='+ item.value)

    cookie.save(filename=filename.ignore_discard=True,ignore_expires=True)