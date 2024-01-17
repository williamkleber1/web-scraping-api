# Projeto de Extração e Análise de Dados
### Descrição
#### Este projeto é uma aplicação web que realiza a extração de dados de um site específico, processa esses dados e gera gráficos informativos com as informações extraídas. Utiliza Python com bibliotecas como Pandas para análise de dados e Matplotlib/Seaborn para plotagem de gráficos.

### Pré-requisitos

- Docker

### Instalação e Execução
#### Clonar o Repositório

 Clone o repositório do projeto para o seu sistema local:

```bash
git clone https://github.com/williamkleber1/web-scraping-api.git
cd web-scraping-api
```
#### Executar com Docker Compose
Dentro do diretório do projeto, execute:

```
docker-compose up
```
Acessar a Aplicação
Após iniciar, acesse:
```
http://localhost:8080/
``````

#### Executar sem docker

É possível executar a aplicação sem o docker compose, basta abrir o diretório do projeto rodar os seguintes comandos:
```
pip install -r requirements.txt
uvicorn main:app --host 0.0.0.0 --port 8080 --reload
```
Desse modo a aplicação funcionará normalmente no host citado anteriormente.

#### Funcionalidades
- Extração de Dados: Extração eficiente e estruturada de dados.
- Análise de Dados: Processamento e análise com Pandas.
- Visualização de Dados: Gráficos e tabelas com Matplotlib e Seaborn.
- Interface Web: Interface para visualização dos resultados.
- Criação de planilha excel com os dados da extração
- Criação de CSV com os dados da extração
- Criação de relatório em PDF 
- Criação de imagens com os gráficos

### Diretório output
Além do relatório visualizado em "localhost:8080/", é gerada uma pasta chamada output que contém todas as informações sobre a extração.





#### Tecnologias Utilizadas
- Python

- FastAPI
- beautifulsoup4

- Pandas

- Matplotlib/Seaborn

- Docker
/Docker Compose


