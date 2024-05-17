[![-----------------------------------------------------](https://raw.githubusercontent.com/andreasbm/readme/master/assets/lines/colored.png)](#innovachat)

# ➤ InnovaChat

InnovaChat é uma aplicação de chatbot sofisticada que utiliza o poder do Python, FastAPI e da IA Generativa do Google, além do pipeline Transformers no backend, juntamente com um frontend dinâmico em ReactJS. Este projeto combina tecnologias web modernas e modelos de aprendizado de máquina avançados para oferecer uma experiência de chat inteligente e interativa.


[![-----------------------------------------------------](https://raw.githubusercontent.com/andreasbm/readme/master/assets/lines/colored.png)](#ndice)

## ➤ Índice

- [➤ InnovaChat](#-innovachat)
  - [➤ Índice](#-índice)
  - [➤ Recursos](#-recursos)
  - [➤ Tecnologias Utilizadas](#-tecnologias-utilizadas)
  - [➤ Instalação](#-instalação)
    - [Pré-requisitos](#pré-requisitos)
    - [Configuração do Backend](#configuração-do-backend)
    - [Configuração do Frontend](#configuração-do-frontend)
  - [➤ Uso](#-uso)
  - [➤ Endpoints da API](#-endpoints-da-api)
    - [Endpoints Disponíveis](#endpoints-disponíveis)
    - [Exemplo de Requisição](#exemplo-de-requisição)
  - [➤ Contribuindo](#-contribuindo)
  - [➤ Docker](#-docker)


[![-----------------------------------------------------](https://raw.githubusercontent.com/andreasbm/readme/master/assets/lines/colored.png)](#recursos)

## ➤ Recursos

- **Backend**: Python com FastAPI para lidar com as requisições da API.
- **Modelos de IA**: Integração com a IA Generativa do Google e o pipeline Transformers para respostas inteligentes.
- **Frontend**: Desenvolvido em ReactJS, utilizando NodeJS (20+) e react-chat-bot para uma experiência de chat fluida.
- **Comunicação em Tempo Real**: Capacidades de chat em tempo real entre os usuários e a IA.


[![-----------------------------------------------------](https://raw.githubusercontent.com/andreasbm/readme/master/assets/lines/colored.png)](#tecnologias-utilizadas)

## ➤ Tecnologias Utilizadas

**Backend:**
- Python
- FastAPI
- Google Generative AI
- Transformers

**Frontend:**
- ReactJS
- NodeJS (20+)
- react-chat-bot


[![-----------------------------------------------------](https://raw.githubusercontent.com/andreasbm/readme/master/assets/lines/colored.png)](#instalao)

## ➤ Instalação

### Pré-requisitos

Certifique-se de ter os seguintes itens instalados:

- Python 3.8+
- NodeJS 20+
- Yarn ou NPM

### Configuração do Backend

1. Clone o repositório:
    ```sh
    git clone https://github.com/vitasso13/InnovaChat.git
    ```
   
2. Navegue até o diretório do backend:
    ```sh
    cd InnovaChat/backend
    ```

3. Crie e ative um ambiente virtual:
    ```sh
    python -m venv venv
    source venv/bin/activate  # No Windows use `venv\Scripts\activate`
    ```

4. Instale os pacotes necessários:
    ```sh
    pip install -r requirements.txt
    ```

5. Inicie o servidor FastAPI:
    ```sh
    uvicorn main:app --reload
    ```

### Configuração do Frontend

1. Navegue até o diretório do frontend:
    ```sh
    cd InnovaChat/frontend
    ```

2. Instale as dependências:
    ```sh
    npm install
    ```

3. Inicie o servidor de desenvolvimento do React:
    ```sh
    npm start
    ```


[![-----------------------------------------------------](https://raw.githubusercontent.com/andreasbm/readme/master/assets/lines/colored.png)](#uso)

## ➤ Uso

1. Certifique-se de que os servidores backend e frontend estejam em execução.
2. Abra seu navegador e navegue para `http://localhost:3000`.
3. Comece a conversar com o InnovaChat!


[![-----------------------------------------------------](https://raw.githubusercontent.com/andreasbm/readme/master/assets/lines/colored.png)](#endpoints-da-api)

## ➤ Endpoints da API

### Endpoints Disponíveis

- `POST /ask`: Lida com mensagens dos usuários e retorna respostas da IA.
- `POST /ask_gemini`: Lida com mensagens dos usuários e retorna respostas da IA.

### Exemplo de Requisição

```sh
curl -X POST "http://localhost:8000/chat" -H "Content-Type: application/json" -d "{\"message\": \"Olá\"}"
```


[![-----------------------------------------------------](https://raw.githubusercontent.com/andreasbm/readme/master/assets/lines/colored.png)](#contribuindo)

## ➤ Contribuindo

Contribuições são bem-vindas! Siga estes passos para contribuir:

1. Faça um fork do repositório.
2. Crie uma nova branch (`git checkout -b feature/SuaFeature`).
3. Faça suas alterações.
4. Commite suas alterações (`git commit -m 'Adicionei um novo recurso'`).
5. Faça o push para a branch (`git push origin feature/SuaFeature`).
6. Abra um Pull Request.


[![-----------------------------------------------------](https://raw.githubusercontent.com/andreasbm/readme/master/assets/lines/colored.png)](#licena)

## ➤ Docker

Este projeto está configurado para rodar com docker e docker-compose 
`docker-compose up`

---

Feliz chat com o InnovaChat! Se você tiver alguma dúvida ou problemas, por favor entre em contato pelo email [seu-email@exemplo.com].