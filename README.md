# Challenge bycoders_

### O desafio consiste em fazer upload de um arquivo CNAB com os dados das movimentações finanaceira de várias lojas e exibir esses dados em outra tela. mais detalhes no arquivo "Instruções.md"

<br>

Tabela de conteúdos
=================

* [Sobre](#Sobre)
* [Pre Requisitos](#pre-requisitos)
    * [Com Docker](#rodar-com-docker-compose)
    * [Em Localhost](#rodar-em-localhost)
* [Instalação](#instalacao)
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

# Construir containers e baixar imagens
$ docker compose up -d

```
> Obs.: Deve-se aguardar cerca de 2 minutos até o banco de dados fique totalmente disponível e a api conecte ao banco de dados.

## Snapshots

## Endpoints

## Testes

### Frontend

Os testes de frontend foram construídos com cypress

para executá-los:
```
$ cd challenge_app
$ yarn cypress run
```

### Backend

Os testes de backend foramcontruídos com pytest
para executá-los:
```
$ cd challenge_api
$ pytest
```

## 🛠 Tecnologias

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
