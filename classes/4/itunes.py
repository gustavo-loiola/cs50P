import json #comes with python
import requests #needs to pip
import sys #comes with python

if len(sys.argv) != 2:
    sys.exit()

response = requests.get("https://itunes.apple.com/search?entity=song&limit=20&term=" + sys.argv[1])

o = response.json()
for result in o["results"]:
    print(result["trackName"])
