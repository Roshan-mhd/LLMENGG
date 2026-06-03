from bs4 import BeautifulSoup
import requests

headers= {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36"
}

def fetch_data(url):
    response = requests.get(url, headers=headers)
    if response.status_code == 200:
        soup = BeautifulSoup(response.text, "html.parser")
        heading = soup.find_all("h1")
        para = soup.find_all("p")
    else:
        print(f"Failed to retrieve data. Status code: {response.status_code}")
    return(heading, para)

#print(fetch_data("https://www.scrapethissite.com/pages/simple/"))