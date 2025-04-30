
# Estrutura de Pastas — Channel Pulse
```
📁 Channel Pulse/
├── 📁 coleta/                          # Scripts de coleta de dados
│   ├── coleta_api.py                  # Coleta pela API do YouTube
│   ├── coleta_selenium.py            # Scraping com Selenium (comentários, dados extras)
│   └── socialblade_scraper.py        # Coleta de histórico externo (se necessário)
│
├── 📁 perguntas/                      # Módulos separados por pergunta
│   ├── crescimento_canal.py          # Pergunta 1: Canal está em crescimento?
│   ├── sentimento_por_video.py       # Pergunta 2: Comentários positivos/negativos por vídeo
│   ├── criticas_elogios.py           # Pergunta 3: Extração de críticas/elogios
│   ├── temas_mais_engajam.py         # Pergunta 4: Temas com maior engajamento
│   ├── risco_de_queda.py             # Pergunta 5: Risco de queda do canal
│   └── comportamento_atipico.py      # Pergunta 6: Detecção de engajamento atípico
│
├── 📁 dados/
│   ├── 📁 brutos/                     # Dados brutos (JSON, CSV)
│   ├── 📁 tratados/                   # Dados tratados e prontos para análise
│   └── 📁 exemplos/                   # Amostras pequenas para teste ou GitHub
│
├── 📁 database/
│   ├── init_db.py                    # Script de criação das tabelas SQLite
│   └── conexao.py                    # Função utilitária de conexão
│
├── 📁 analise/
│   ├── nlp_sentimento.py             # Função de análise de sentimento
│   ├── topicos_lda.py                # Extração de tópicos com LDA
│   └── classifica_tema.py           # Classificação de tema via IA/API
│
├── 📁 utils/                          # Funções auxiliares reutilizáveis
│   ├── limpeza_texto.py             # Limpeza e normalização de texto
│   ├── helpers.py                   # Funções genéricas (ex: checagem de canal)
│   └── email_alerta.py              # Envio de alerta por e-mail (futuro)
│
├── main.py                           # Script principal para execução do projeto
├── requirements.txt                  # Dependências do projeto
├── README.md                         # Documentação principal
└── LICENSE                           # Licença do projeto
```