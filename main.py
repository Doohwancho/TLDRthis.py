import sys
import requests
from pprint import pprint



def summarize_and_translate(article_url, min_length=100, max_length=300):
    url = "https://tldrthis.p.rapidapi.com/v1/model/abstractive/summarize-url/"
    rapidapi_key = '42f0f78019msh451116660e685ebp188696jsne8a291794f8c' 

    payload = {
        "url": article_url, 
        "min_length": min_length, 
        "max_length": max_length, 
        "is_detailed": False 
    }

    headers = {
        "content-type": "application/json",
        "X-RapidAPI-Key": rapidapi_key,
        "X-RapidAPI-Host": "tldrthis.p.rapidapi.com"
    }

    response = requests.request("POST", url, json=payload, headers=headers)
    #print(response.json())

    summary = response.json()['summary'][0].strip()

    print(summary)

def main(url):
    summarize_and_translate(url, 50, 100)


if __name__ == '__main__':
    main(sys.argv[1])
