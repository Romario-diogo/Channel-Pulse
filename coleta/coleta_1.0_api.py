# Busca canais no YouTube com base em uma palavra-chave.

# Retorna os 5 primeiros canais relacionados.

# Coleta informações detalhadas sobre cada um.

# Compara o número de vídeos postados por cada canal.

# Identifica qual canal tem mais vídeos publicados.

#Exibe:

#Nome do canal

#ID do canal

#Quantidade de vídeos (com separador de milhar)

#Descrição

from dotenv import load_dotenv
import os
import requests
import json

load_dotenv() # Carrga as variaveis 
key = os.getenv("KEYS_YOUTUBE")

channel = input("Qual o nome do canal ? ")

url = "https://www.googleapis.com/youtube/v3/search"

params = {
    "part": "snippet",
    "type": "channel",
    "q": channel,
    "maxResults": 4,
    "key": key
}

res = requests.get(url, params=params)

# Salvar em um json 
dados = res.json()

dados_info = []
for info in dados["items"]:
    dados_info.append(info["id"]["channelId"])

url_channel = "https://www.googleapis.com/youtube/v3/channels"

params = {
    "part": "snippet, statistics",
    "id": ','.join(dados_info),
    "key": key
}
res_id = requests.get(url_channel, params=params)
info = res_id.json()


channel_info = None
maior_video = 0

for channel_video in info["items"]:
    video = int(channel_video["statistics"].get("videoCount", 0))
    if video > maior_video:
        maior_video = video
        channel_info = channel_video


if channel_info:
    nome = channel_info["snippet"]["title"]
    id = channel_info["id"]
    video = int(channel_info["statistics"]["videoCount"])
    descricao = channel_info["snippet"]["description"]
#Exibe:

#Nome do canal
print(f"Nome: {nome}")
#ID do canal
print(f"ID: {id}")
#Quantidade de vídeos (com separador de milhar)
print(f"Videos publicado: {video:,}".replace(",","."))
#Descrição
print(f"Descrição: {descricao}")
# with open("res_id.json", 'w') as f:
#     json.dump(info, f , indent=2)