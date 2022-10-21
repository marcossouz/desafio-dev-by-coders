# Challenge bycoders_

### O desafio consiste em fazer upload de um arquivo CNAB com os dados das movimentações finanaceira de várias lojas e exibir esses dados em outra tela. mais detalhes no arquivo "Instruções.md"

<br>

Tabela de conteúdos
=================

* [Sobre](#sobre)
* [Pre Requisitos](#pré-requisitos)
    * [Com Docker](#rodar-com-docker-compose)
    * [Em Localhost](#rodar-em-localhost)
* [Instalação](#instalação)
* [Snapshots](#snapshots)
* [Endpoints](#endpoints)
* [Tests](#testes)
    * [Frontend](#frontend)
    * [Backend](#backend)
* [Tecnologias](#tecnologias)


## Sobre

Desafio solicitado por Bianca Santos (bycoders_) em 19/10/2022. O intuito é construir uma aplicação que consiga demonstrar minhas habilidades envolvendo vários níveis de complexidade de diferentes áreas de desenvolvimento. Partindo do backend com rest, passando pelo frontend com documentação e testes, até chegar em devops com docker-compose.

## Pré-requisitos

### Rodar com docker-compose
Antes de começar, você vai precisar ter instalado em sua máquina as seguintes ferramentas:

- <a href="https://docs.docker.com/engine/install/">Docker Engine (versão utilizada: Docker Desktop 4.12.0)</a>
- <a href="https://docs.docker.com/compose/install/">Docker Compose (versão utilizada: v2.10.2)</a>

### Rodar em localhost
Antes de começar, você vai precisar ter instalado em sua máquina as seguintes ferramentas:

- <a href="https://www.python.org/downloads/">Python v3.9</a>
- <a href="https://nodejs.org/en/download/">Node v16</a>
- <a href="https://www.postgresql.org/download/">Postgres v14</a>


## Instalação

> Obs.: Em carater de simplificação, vou seguir com a documentação para instalação utilizando docker-compose


```bash
# Clone este repositório
$ git clone <https://github.com/marcossouz/desafio-dev-by-coders>

# Acesse a pasta do projeto no terminal/cmd
$ cd desafio-dev-by-coders

# Criar arquivo .env
$ cp .env.local .env

# Construir containers e baixar imagens
$ docker compose up -d

```
> Obs.: Deve-se aguardar cerca de 2 minutos até o banco de dados fique totalmente disponível e a api conecte ao banco de dados.
> Obs_2.: Adicionei apenas 1 transação de cada loja no dump para possibilitar testes de importação com o sistema rodando.

## Snapshots

#### Listagem de transação por loja
![Listagem de transação por loja](https://user-images.githubusercontent.com/18218791/197261102-1a78f8f7-35c6-426a-a231-025cc94822a5.png)

#### Arquivo selecionado
![Arquivo Selecionado](https://user-images.githubusercontent.com/18218791/197260730-21a5bccc-e8f7-49ce-ac1a-cf9fb84af0aa.png)

#### Upload de arquivo realizado
![Upload Realizado](https://user-images.githubusercontent.com/18218791/197260846-652e4583-90b8-4a33-b729-6e020ad718d5.png)

## Endpoints

- Para melhor utilização da api, foi disponibilizado a documentação nos endpoints:
   - `http://localhost:8000/swagger/`
   ![Swagger](https://user-images.githubusercontent.com/18218791/197261820-89d4d039-3e98-4b55-bd58-347ebb67c22a.png)
   
   - `http://localhost:8000/redoc/`
   ![redoc](https://user-images.githubusercontent.com/18218791/197261957-d0bd9e73-3453-43a9-b43b-ae7a9686b7cd.png)

   - > Para facilitar a reprodução do uso da api, também foi disponibilizado o arquivo exportado do postman:
     - > `devops/challenge_api.postman_collection.json`

 - Endpoints da api
   - `http://localhost:8000/cnab/`
   - `http://localhost:8000/transacao/`

- Aplicação
   - `http://localhost:3000/`

## Testes

### Frontend

Os testes de frontend foram construídos com cypress

para executá-los:

- Em 1 terminal execute: 
```
$ cd challenge_app
$ yarn install
$ yarn dev
```

- Em outro terminal em paralelo execute:
```
$ cd challenge_app
$ yarn cypress run
```

### cypress run
![cypress run](https://user-images.githubusercontent.com/18218791/197264753-ac9a4961-82cb-435c-ab2f-b2b1e414bb63.png)

### cypress open
![cypress](https://user-images.githubusercontent.com/18218791/197263944-f6cf5808-ebbb-4a43-8d7c-04d05ce3ceba.png)


### Backend

Os testes de backend foramcontruídos com pytest
para executá-los:
```
$ cd challenge_api
$ pytest
```
### Pytest
![pytest](https://user-images.githubusercontent.com/18218791/197265355-f71c28fa-a569-4afb-868e-6118f7e57f54.png)


## Tecnologias

As seguintes ferramentas foram usadas na construção do projeto:

- [Python](https://www.python.org/downloads/)
- [Django](https://www.djangoproject.com/download/)
- [Django Rest Framework](https://www.django-rest-framework.org/)
- [Next.Js](https://nextjs.org/)
- [Fetch Api](https://developer.mozilla.org/en-US/docs/Web/API/Fetch_API)
- [Docker](https://www.docker.com/)
- [docker-compose](https://docs.docker.com/compose/)
- [Yarn](https://yarnpkg.com/)
- [Swagger](https://swagger.io/)
- [cypress](https://www.cypress.io/)
- [pytest](https://docs.pytest.org/en/7.1.x/)
- [postgres](https://www.postgresql.org/)
