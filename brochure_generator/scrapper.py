from bs4 import BeautifulSoup
import requests

headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36"
}

def contents(url):
    try:
        response = requests.get(url, headers=headers)
        response.raise_for_status()
        soup = BeautifulSoup(response.text, 'html.parser')
        title = soup.title.string if soup.title else 'No Title Found'
        text = soup.find_all('p')
        text = ' '.join([p.get_text() for p in text])
        return (text , title)[:2000]
    except requests.exceptions.RequestException as e:
        print(f"Error fetching the URL: {e}")
        return None
    
def links(url):
        try:
            response = requests.get(url, headers=headers)
            response.raise_for_status()
            soup = BeautifulSoup(response.text, 'html.parser')
            links = [a['href'] for a in soup.find_all('a', href=True)]
            return links [:2000]
        except requests.exceptions.RequestException as e:
            print(f"Error fetching the URL: {e}")
            return None