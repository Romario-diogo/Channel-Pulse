from dotenv import load_dotenv
import requests
import os
import json





load_dotenv()
key = os.getenv("KEYS_YOUTUBE")
nome_canal = input("Qual nome do canal com indentificador ").strip()

url = "https://www.googleapis.com/youtube/v3/search"
params = {
    "part": "snippet",
    "q": nome_canal,
    "type": "channel",
    "key": key
}


res_canal = requests.get(url, params=params)
dados_canal = res_canal.json()


with open(f"{nome_canal}.json", "w", encoding="utf-8") as f:
    json.dump(dados_canal, f, indent=2, ensure_ascii=False)