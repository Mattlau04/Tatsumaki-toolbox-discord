import sys
import requests
import random

link = sys.argv[1]
token = sys.argv[2]
useproxies = False
print(token)
print(link)

def proxyjoin():
    try:
        proxy = random.choice(proxy_list)
        requests.post(apilink, headers=headers, proxies={"http": proxy, "https": proxy})
    except Exception:
        proxyjoin()
apilink = "https://discordapp.com/api/v6/invite/" + str(link)
headers = {
    'Authorization': token
}
if useproxies == 'True':
    proxyjoin()
else:
    requests.post(apilink, headers=headers)


apilink = "https://discordapp.com/api/v6/invite/" + str(link)
headers = {
    'Authorization': token
}
requests.post(apilink, headers=headers)
