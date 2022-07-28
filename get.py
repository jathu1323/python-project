import requests
import json 

url = 'https://en.wikipedia.org/wiki/GIF'

x = requests.get(url=url)
print(x.status_code)
print()

y=requests.get(url=url)
d={y.text}
#print(d)
z=json.loads(d)
print(z)


f=open("j.json","a")
f.write(z)
f.close()

print()
