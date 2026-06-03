
from openai import OpenAI
import os
from dotenv import load_dotenv
from scrapper import contents , links
import requests
import json

ollama = OpenAI(base_url=os.getenv("OLLAMA_BASE_URL"), api_key="ollama")

load_dotenv()
#url = "https://en.wikipedia.org/wiki/World_War_I"
#url = "https://www.mi.com/in/?srsltid=AfmBOoqDtlPW6MSZ-hKSs7Oj7XcQmgB8jqXw0zP4Uq1OZyTJhpyQivRm"

url = input("Enter the URL of the company website you want to generate a brochure for: ")

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
        "content":link_user_prompt
        }
    ],
    "reasoning": {"enabled": False}
  })
)
first_op = links_response.json()["choices"][0]["message"]["content"]
#print("checkpoitnt 2")
brochure_system_prompt = """
You are an assistant that analyzes the contents of several relevant pages from a company website
and creates a short brochure about the company for prospective customers, investors and recruits.
Respond in markdown without code blocks.
Include details of company culture, customers and careers/jobs if you have the information.
"""
user_prompt = f"""
Here are the contents of its landing page and other relevant pages;
use this information to build a short brochure of the company in markdown without code blocks.\n\n

"""

ollama_response = ollama.chat.completions.create(
    model="llama3.2",
    messages = [{
        "role": "system",
        "content": brochure_system_prompt
    },{
        "role": "user",
        "content": user_prompt + first_op}])

print(ollama_response.choices[0].message.content)