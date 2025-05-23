from dotenv import load_dotenv
import os
import requests
import json 
load_dotenv()

key = os.getenv("KEYS_YOUTUBE")
name_channel = str(input("Nome do canal !!!"))


def buscar_canal(name_channel, salvar_em_arquivo=False):
    url = "https://www.googleapis.com/youtube/v3/search"
    params = {
        "part":"snippet",
        "type": "channel",
        "q": name_channel,
        "maxResults": 5,
        "key": key
    }

    resultado_params = requests.get(url, params=params) 
    dados_params = resultado_params.json()

    if not dados_params.get("items"):
        print("Nenhum canal encontrado na busca.")
        return

    coleta_channel = []
    for id_channel in dados_params['items']:
        coleta_channel.append(id_channel['id']['channelId'])

    url_channel = "https://www.googleapis.com/youtube/v3/channels"
    params = {
        "part": "snippet,statistics",
        "id":",".join(coleta_channel),
        "key": key
    }
    resultado_channel  = requests.get(url_channel, params=params)
    dados_channel = resultado_channel.json()

    if not dados_params.get("items"):
        print("Nenhum canal encontrado na busca.")
        return

    channel_views = None
    cont_views = 0
    for channel in dados_channel['items']:
        views = int(channel['statistics'].get("viewCount", 0))
        if views > cont_views:
            cont_views = views
            channel_views = channel
        if channel_views:
           nome = channel_views["snippet"]['title']
           id_channel = channel_views['id']
           descricao = channel_views["snippet"]["description"]
           print(f"Nome: {nome}")
           print(f"ID: {id_channel}")
           print(f"View: {cont_views:,}".replace(",", "."))
           print(f"Descrição: {descricao}")
        else:
            print("Nenhum canal com visualizações foi identificado.")

    if salvar_em_arquivo:
        nome_arquivo = nome # Nome do canal
        pasta_destino = "dados/brutos" # caminho do arquivo
        os.makedirs(pasta_destino, exist_ok=True) # Define o diretório 
        caminho_final = os.path.join(pasta_destino, nome_arquivo) # Junta caminho + nome do arquivo
        with open (caminho_final, 'w', encoding="utf-8") as f:
            json.dump(channel_views, f, indent=2)
        print(f"Arquivo salvo em: {caminho_final}")


buscar_canal(name_channel, salvar_em_arquivo=True)



