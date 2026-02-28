import requests

url = "https://bit.ly/BeasiswaMABA3"

r = requests.head(url, allow_redirects=False)
print(r.headers.get("Location"))