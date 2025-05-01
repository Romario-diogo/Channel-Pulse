
from dotenv import load_dotenv
import requests
import os
import json

load_dotenv()
key = os.getenv("KEYS_YOUTUBE")


url = "https://www.googleapis.com/youtube/v3/search"

params = {
    "part": "snippet", # Solicita as informações (img, descrição, data de criação)
    "q": "Manual do Mundo",
    "type": "channel",
    "maxResults": 5,
    "key": key
}
res = requests.get(url, params=params)
dados = res.json()


canais_ids = []
for item in dados['items']:
    canais_ids.append(item['id']['channelId'])


canais_url = "https://www.googleapis.com/youtube/v3/channels"

canais_params = {
    "part": "snippet,statistics", # Solicita as informações e as metricas (numeros de (inscritos, views e vídeo))
    "id": ",".join(canais_ids),
    "key": key
}

canais_res = requests.get(canais_url, params=canais_params)
canais_data = canais_res.json()

canal_oficial = None
maior_numero = 0

for canal in canais_data["items"]:
    inscritos = int(canal["statistics"].get("subscriberCount", 0))
    if inscritos > maior_numero:
        maior_numero = inscritos
        canal_oficial = canal

if canal_oficial:
    nome = canal_oficial["snippet"]["title"]
    canal_id = canal_oficial["id"]
    inscritos = canal_oficial["statistics"]["subscriberCount"]
    descricao = canal_oficial["snippet"]["description"]
    inscritos = int(inscritos)
    print("Canal mais relevantes encontrados:")
    print(f"Nome: {nome}")
    print(f"ID: {canal_id}")
    print(f"Inscritos: {inscritos:,}".replace(",", "."))
    print(f"Descrição: {descricao}")
else:
    print("Nada encontrado ")

#with open("dados.json", 'w') as f:
    #json.dump(dados, f , indent=2)