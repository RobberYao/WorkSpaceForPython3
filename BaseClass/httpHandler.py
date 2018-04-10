import requests

if __name__ == '__main__':
    http = 'http://'
    https = 'https://'
    host_4g = '192.168.199.28'
    host_vip = '10.155.61.188'
    port = '9999'
    url = '/test?'
    sendDictParams = {'q': '打开音乐'}
    Url = http + host_vip + ':' + port + url
    print(' ------- ' + Url + str(sendDictParams))
    response = requests.get(Url, params=sendDictParams)
    print(' ======= ' + response.url)
