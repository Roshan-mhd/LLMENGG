
# not complete




from openai import OpenAI
import os
from dotenv import load_dotenv
from scrapper import contents , links
import requests
import json

ollama = OpenAI(base_url=os.getenv("OLLAMA_API_URL"), api_key="ollama")

load_dotenv()
#url = "https://en.wikipedia.org/wiki/World_War_I"
url = "https://www.mi.com/in/?srsltid=AfmBOoqDtlPW6MSZ-hKSs7Oj7XcQmgB8jqXw0zP4Uq1OZyTJhpyQivRm"

titles, text =contents(url)
links = links(url)

#print(titles)
#print(text)
#print(links)

link_system_prompt = """
You are provided with a list of links found on a webpage.
You are able to decide which of the links would be most relevant to include in a brochure about the company,
such as links to an About page, or a Company page, or Careers/Jobs pages.
You should respond in JSON as in this example:

{
    "links": [
        {"type": "about page", "url": "https://full.url/goes/here/about"},
        {"type": "careers page", "url": "https://another.full.url/careers"}
    ]
}
"""
link_user_prompt = f"""
Here is the list of links on the website {url} -
Please decide which of these are relevant web links for a brochure about the company, 
respond with the full https URL in JSON format.
Do not include Terms of Service, Privacy, email links.

Links (some might be relative links): {links}

"""

links_response = requests.post(
  url=os.getenv("URL"),
  headers={
    "Authorization": f"Bearer {os.getenv('API_KEY')}",
    "Content-Type": "application/json"
  },
  data=json.dumps({
    #"model": "openai/gpt-oss-20b:free",
    #"model": "deepseek/deepseek-v4-flash:free",
    "model":"nvidia/nemotron-3-nano-omni-30b-a3b-reasoning:free",
    "messages": [
        {
        "role": "system",
        "content": link_system_prompt
        },
        {
        "role": "user",
        "content": link_user_prompt
        }
    ],
    "reasoning": {"enabled": False}
  })
)
print(links_response.json()["choices"][0]["message"]["content"])
#print(links_response.json())


