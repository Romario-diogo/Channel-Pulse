from dotenv import load_dotenv
from dateutil.parser import parse  
import os
import requests
import json 

load_dotenv()
key = os.getenv("KEYS_YOUTUBE")
name_channel = input("Nome do canal: ").strip()

# 1. Buscar ID do canal pelo nome
url = "https://www.googleapis.com/youtube/v3/search"
params = {
    "part": "snippet",
    "type": "channel",
    "q": name_channel,
    "maxResults": 5,
    "key": key
}
res = requests.get(url, params=params)
dados_params = res.json()

if not dados_params.get("items"):
    print("Nenhum canal encontrado na busca.")
    exit()

# 2. Obter estatísticas dos canais retornados
coleta_channel = [item['id']['channelId'] for item in dados_params['items']]

url_channel = "https://www.googleapis.com/youtube/v3/channels"
params = {
    "part": "snippet,statistics",
    "id": ",".join(coleta_channel),
    "key": key
}
res_channel = requests.get(url_channel, params=params)
dados_channel = res_channel.json()

if not dados_channel.get("items"):
    print("Não foi possível obter dados dos canais.")
    exit()

# 3. Escolher o canal com mais visualizações
canal_mais_visto = max(
    dados_channel['items'],
    key=lambda ch: int(ch['statistics'].get("viewCount", 0))
)

# 4. Extrair dados
nome = canal_mais_visto["snippet"]['title']
id_channel = canal_mais_visto['id']
escritos = int(canal_mais_visto["statistics"]["subscriberCount"])
visualizacao = int(canal_mais_visto["statistics"]["viewCount"])
videos_total = int(canal_mais_visto["statistics"]["videoCount"])
canal_publicado = canal_mais_visto["snippet"]["publishedAt"]
data_formatada = parse(canal_publicado).strftime("%d de %B de %Y às %H:%M:%S")

# 5. Exibir e salvar
print(f"\nNome: {nome}")
print(f"ID: {id_channel}")
print(f"Criação do canal: {data_formatada}")
print(f"Escritos: {escritos:,}".replace(",", "."))
print(f"Visualizações: {visualizacao:,}".replace(",", "."))
print(f"Total de vídeos: {videos_total:,}".replace(",", "."))

# Evitar caracteres inválidos no nome do arquivo
#nome_arquivo = "".join(c if c.isalnum() or c in " -_" else "_" for c in nome)

# with open(f"{nome_arquivo}.json", "w", encoding="utf-8") as f:
#     json.dump(canal_mais_visto, f, indent=2, ensure_ascii=False)

# 6.  Critérios de Seleção de Vídeos 

if videos_total <= 100:
    print("Coleta todos os 100")
elif videos_total >= 101 or videos_total <= 1000:
    print("Coletar 500 videos")
elif videos_total >= 1001 or videos_total <= 5000:
    print("coletar 1000 videos")
elif videos_total > 5001:
    print("coletar 1500 videos")

# url_channel = "https://www.googleapis.com/youtube/v3/channels"
# params = {
#     "part": "statistics",
#     "id": id_channel,
#     "key": key
# }
# res_id = requests.get(url_channel, params=params)
# dados_id = res_id.json()



# for dados

    # nome_arquivo = nome # Nome do canal
    # pasta_destino = "dados/brutos" # caminho do arquivo
    # os.makedirs(pasta_destino, exist_ok=True) # Define o diretório 
    # caminho_final = os.path.join(pasta_destino, nome_arquivo) # Junta caminho + nome do arquivo
    # with open (caminho_final, 'w', encoding="utf-8") as f:
    #     json.dump(channel_views, f, indent=2)
    # print(f"Arquivo salvo em: {caminho_final}")





