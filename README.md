
# Channel Pulse

## Descrição

Este projeto tem como objetivo analisar canais do YouTube de forma automatizada, inteligente e orientada a dados, respondendo seis perguntas essenciais sobre performance, engajamento, temas e comportamento da audiência. Ele utiliza a API oficial do YouTube e, quando necessário, complementa com scraping via Selenium, permitindo extrair dados em maior volume e profundidade.

A partir dessas coletas, o projeto aplica técnicas de NLP para análise de sentimento, extração de tópicos, classificação de temas e avaliação de engajamento. As respostas são estruturadas por módulo, cada uma focada em uma pergunta-chave, com critérios objetivos, escaláveis e justificáveis.

Entre os principais recursos:

- Diagnóstico de crescimento do canal com base em múltiplos indicadores
- Análise de sentimento dos comentários por vídeo
- Extração de críticas e elogios recorrentes
- Identificação de temas que mais geram engajamento
- Avaliação de risco de queda com base em histórico recente
- Detecção de padrões de engajamento atípico

## Motivação

No cenário atual, onde dados sociais influenciam decisões de marketing, parcerias e conteúdo, entender a performance real de um canal do YouTube vai muito além de contar inscritos ou visualizações. A motivação deste projeto é preencher essa lacuna: oferecer análises aprofundadas, confiáveis e automatizadas que ajudem a interpretar engajamento, avaliar crescimento e identificar padrões reais de audiência — tudo com base em dados públicos e técnicas modernas de NLP e automação.

## Como funciona

O projeto funciona em etapas modulares. Primeiro, coleta dados públicos dos canais usando a API oficial do YouTube e complementa com Selenium para extrair comentários em larga escala. Esses dados são armazenados, tratados e analisados com técnicas de NLP para gerar respostas estruturadas a perguntas específicas sobre crescimento, engajamento, sentimento e temas. Cada análise é executada de forma independente, permitindo respostas diretas e justificadas a partir dos dados mais recentes disponíveis.

## Tecnologias e ferramentas previstas

- Python 3.12+
- API oficial do YouTube (Google API Client)
- Selenium (com controle de perfil e delays configurados)
- Pandas e NumPy para manipulação de dados
- SpaCy, scikit-learn e NLTK para NLP
- Matplotlib ou Plotly para visualização
- OpenAI ou Gemini API (para classificação de temas via prompt)
- SQLite

## Diferenciais

- Projeto modular por função de análise
- Integração de coleta via API e scraping
- Análise de sentimento e extração de tópicos
- Respostas justificadas por métricas reais
- Potencial de expansão para dashboards e alertas automáticos

## Licença

Este projeto está licenciado sob a MIT License. Veja o arquivo `LICENSE` para mais detalhes.

## Contato

Para dúvidas, sugestões ou contribuições futuras, entre em contato:

Romário Diogo  [LinkedIn](https://www.linkedin.com/in/2606roma/)  
