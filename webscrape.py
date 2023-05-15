# importer alle requests
import requests
import re
from bs4 import BeautifulSoup
url = "https://www.linkedin.com"
keyword = "Regnskapsfører"

response = requests.get(url)
soup = BeautifulSoup(response.text, "html.parser")
#koden som går igjennom http og søker etter keywords
for link in soup.find_all("a"):
    link_url = link.get("href")
    if link_url.startswith("http"):
        response = requests.get(link_url)
        content = response.text
        if re.search(keyword, content):
            print(f"(link funnet: {link_url})")
        else :
            print(f"fant ikke{link_url}")
