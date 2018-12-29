import os
import requests
import requests_cache

requests_cache.install_cache('../cache')
url = 'https://adventofcode.com/' + os.path.abspath(__file__).split('/')[-2] + '/day/' + __file__.split('.')[0] + '/input'
input1 = requests.get(url, cookies={"session": os.environ['SESSION']}).text

print(sum(map(int, input1.splitlines())))

seen = set()
current = 0
while True:
    for line in map(int, input1.splitlines()):
        seen.add(current)
        current += line
        if current in seen:
            print(current)
            exit()
