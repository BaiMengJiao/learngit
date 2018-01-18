import urllib.request

response = urllib.request.urlopen('http:\\192.168.1.107\Users\000愉快的开始.mp4')
mp4 = response.read()

with open('000愉快的开始.mp4','wb')as f:
    f.write(mp4)

