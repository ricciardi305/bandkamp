<h1 align="center">Projeto BandKamp</h1>

<p align="center">Projeto que simula uma produtora de música</p>

<p align="center">
    <img src="https://img.shields.io/github/license/ricciardi305/bandkamp"/>
    <img src="https://img.shields.io/github/stars/ricciardi305/bandkamp"/>
    <img src="https://img.shields.io/github/forks/ricciardi305/bandkamp"/>
    <img src="https://img.shields.io/github/repo-size/ricciardi305/bandkamp"/>
    <img src="https://img.shields.io/github/last-commit/ricciardi305/bandkamp"/>
</p>

<hr/>

<p align="center">
    <a href="#sobre">Sobre</a> •
    <a href="#features">Features</a> •
    <a href="#pré-requisitos">Pré-requisitos</a> •
    <a href="#tecnologias">Tecnologias</a> •
    <a href="#autor">Autor</a>
</p>

# Sobre

Bandkamp é um projeto de avaliação do 2º módulo de back-end da [Kenzie Academy](https://kenzie.com.br/), módulo focado em python. A API Bandkamp simula uma produtora musical onde podemos cadastrar um músico, albúm e músicas, sendo que as músicas estarão relacionadas a um ábul e músico e o album estará relacionado a um músico.<br />
Esse projeto foi construído com base na arquitura MVC - Model-View-Controller e utiliza as fetures de Generic View e Model Serializers do Django Rest Framework, além de outras tecnologias que serão listadas mais adiante.

# Features

- [x] Músicos
  - [x] Cadastro
    ```json
    {
    	"first_name": "John",
    	"last_name": "Frusciante",
    	"instrument": "Guitar"
    }
    ```
  - [x] Listagem
  - [x] Atualização
  - [x] Deleção
- [x] Álbums
  - [x] Criação
    ```json
    {
    	"name": "The Empyrean"
    }
    ```
  - [x] Listagem
- [x] Músicas
  - [x] Criação
        `json { "name": "The Empyrean" } `

# Pré-requisitos

Antes de começar, você vai precisar ter instalado em sua máuina as seguintes ferramentas:<br />
[Git](https://git-scm.com), [Docker](https://docs.docker.com/engine/install/), [Docker Compose](https://docs.docker.com/compose/install/) e [Python](https://www.python.org/downloads/).<br/>
O [Insomnia](https://insomnia.rest/download) é opcional, mas será mais fácil de utilizar a aplicação com ele.

Além disto é bom ter um editor para trabalhar com o código como [VSCode](https://code.visualstudio.com/)<br/>
Renomeie o arquivo `.env.example` para `.env` e preencha as informações necessárias.

# Como rodar a aplicação

```bash
# Clone este repositório
$ git clone <https://github.com/ricciardi305/bandkamp>

# Gerar o ambiente virtual da aplicação (venv) e atualizar as dependências
$ python -m venv venv --upgrade-deps

# Acessar o ambiente virtual de desenvolvimento
Linux/Mac - $ source venv/bin/activate
Windows - $ venv/Script/activate

# Instale as dependências
$ pip install -r requirements.txt

# Inicialize os containers com o Docker
docker-compose up
```

Arquivo do insomnia para interagir com a API [aqui](github/bandkamp-workspace.json).

## Screenshot do Insomnia

<img src="github/Captura%20de%20tela%20de%202022-08-31%2021-40-24.png"/>

# 🛠 Tecnologias

### As seguintes tecnologias foram utilizadas nesse projeto:

- [Python](https://www.python.org/downloads/)
- [Django](https://www.djangoproject.com/)
- [Django Rest Framework](https://www.django-rest-framework.org/)
- [postgreSQL](https://www.postgresql.org/)
- [dotENV](https://pypi.org/project/python-dotenv/)
- [drf-spetacular](https://drf-spectacular.readthedocs.io/)
- [psycopg2-binary](https://pypi.org/project/psycopg2-binary/)<br/>
> Veja o arquivo [requirements.txt](requirements.txt)

# Licença

Este projeto está sob a licença MIT License - Veja o arquivo [License](LICENSE) para mais detalhes.

# Autor

<a href="https://github.com/ricciardi305">
    <img src="https://avatars.githubusercontent.com/u/81863575?v=4&s=150" alt=""/>
    <br />
    <sub style="font-size: 16px"><b>Rafael Ricciardi</b></sub>
</a>

> Feito com ❤️ por Rafael Ricciardi 👋🏽 Entre em contato!

[![Linkedin Badge](https://img.shields.io/badge/-Rafael_Ricciardi-blue?style=flat-square&logo=Linkedin&logoColor=white&link=https://www.linkedin.com/in/tgmarinho/)](https://www.linkedin.com/in/rafaelricciardi/)
[![Gmail Badge](https://img.shields.io/badge/-ricciardi.rafael1997@gmail.com-c14438?style=flat-square&logo=Gmail&logoColor=white&link=mailto:tgmarinho@gmail.com)](mailto:ricciardi.rafael1997@gmail.com)
[![GitHub Badge](https://img.shields.io/badge/-Rafael_Ricciardi-100000?style=flat-square&logo=github&logoColor=white&link=https://github.com/ricciardi305)](https://github.com/ricciardi305)
