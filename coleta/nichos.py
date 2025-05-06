import os
import json
from collections import defaultdict, Counter

pasta_json = r"E:\Pasta (R)\Projetos\ChannelPulse\Channel-Pulse\nichos"

ocorrencias_globais = defaultdict(set)
repetidos_internos = {}

for arquivo in os.listdir(pasta_json):
    if not arquivo.endswith(".json"):
        continue

    caminho = os.path.join(pasta_json, arquivo)
    with open(caminho, encoding="utf-8") as f:
        dados = json.load(f)
        nomes = []

        for lista in dados.values():
            for canal in lista:
                nome = canal.get("nome")
                if nome:
                    nomes.append(nome)
                    ocorrencias_globais[nome].add(arquivo)

        # Verifica duplicados internos
        contagem = Counter(nomes)
        duplicados = {n: c for n, c in contagem.items() if c > 1}
        if duplicados:
            repetidos_internos[arquivo] = duplicados

#  Exibe repetidos entre arquivos
print("\n🔎 Repetidos ENTRE arquivos diferentes:")
for nome, arquivos in ocorrencias_globais.items():
    if len(arquivos) > 1:
        print(f'→ "{nome}" está nos arquivos: {", ".join(arquivos)}')

#  Exibe repetidos dentro dos próprios arquivos
print("\n🔎 Repetidos DENTRO de arquivos:")
for arquivo, canais in repetidos_internos.items():
    print(f"\nArquivo: {arquivo}")
    for nome, vezes in canais.items():
        print(f'  - "{nome}" aparece {vezes} vezes')
