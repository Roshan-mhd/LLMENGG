from bs4 import BeautifulSoup as bs
import requests
import os
import json
from dotenv import load_dotenv
from scrapper import fetch_data

load_dotenv()
website = input("Enter the website you want to summerize: ")
data = fetch_data(website)
#data = fetch_data("https://www.scrapethissite.com/pages/simple/")    
response = requests.post(
  url=os.getenv("URL"),
  headers={
    "Authorization": f"Bearer {os.getenv('API_KEY')}",
    "Content-Type": "application/json"
  },
  data=json.dumps({
    "model": "openai/gpt-oss-20b:free",
    #"model": "deepseek/deepseek-v4-flash:free",
    "messages": [
        {
        "role": "system",
        "content": "you are a flirty woman who likes to tease and flirt with user and make them blush, also you are a website summerizer, you will summarize the content of the website in a flirty way"
      },
      {
        "role": "user",
        "content": "the contents of the wesite which was scrapped is as follows: " + str(data)
      }
    ],
    "reasoning": {"enabled": True}
  })
)
print(response.json()["choices"][0]["message"]["content"])

