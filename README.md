# API SQL de Perguntas com FastAPI

Este projeto é uma aplicação FastAPI que permite aos usuários fazer perguntas relacionadas a consultas SQL. A aplicação se conecta a um banco de dados PostgreSQL e utiliza uma classe personalizada para gerar e executar consultas SQL com base na entrada do usuário.

## Estrutura do Projeto

```
fastapi-sql-question-api
├── src
│   ├── app.py                # Ponto de entrada da aplicação FastAPI
│   ├── database
│   │   ├── __init__.py       # Inicializador vazio para o módulo database
│   │   └── vanna_client.py   # Lógica para conexão com PostgreSQL e execução de consultas SQL
│   ├── api
│   │   ├── __init__.py       # Inicializador vazio para o módulo api
│   │   └── routes.py         # Rotas da API para lidar com perguntas e execução SQL
│   ├── models
│   │   ├── __init__.py       # Inicializador vazio para o módulo models
│   │   └── query.py          # Modelos de dados ou schemas para requisições e respostas da API
│   └── config.py             # Configurações para a aplicação
├── requirements.txt          # Lista de dependências do projeto
├── .env                      # Variáveis de ambiente para configuração
├── .env.example              # Exemplo das variáveis de ambiente necessárias
└── README.md                 # Documentação do projeto
```

## Instruções de Configuração

1. **Clone o repositório:**
   ```
   git clone <repository-url>
   cd fastapi-sql-question-api
   ```

2. **Crie um ambiente virtual:**
   ```
   python -m venv venv
   
   # No Windows:
   venv\Scripts\activate
   
   # No Linux/MacOS:
   source venv/bin/activate
   ```

3. **Instale as dependências:**
   ```
   pip install -r requirements.txt
   ```

4. **Configure as variáveis de ambiente:**
   - Copie o arquivo `.env.example` para `.env` e preencha as credenciais do banco de dados necessárias.
   ```
   copy .env.example .env  # No Windows
   # ou
   cp .env.example .env    # No Linux/MacOS
   ```

5. **Execute a aplicação:**
   ```
   uvicorn src.app:app --reload
   ```

6. **Para desativar o ambiente virtual quando terminar:**
   ```
   deactivate
   ```

## Uso

Uma vez que a aplicação esteja em execução, você pode enviar uma requisição POST para o endpoint `/ask` com um corpo JSON contendo sua pergunta. Por exemplo:

```json
{
  "question": "Me liste os produtos e suas quantidades em estoque"
}
```

A aplicação retornará o resultado da consulta SQL gerada com base na sua pergunta.

## Licença

Este projeto está licenciado sob a Licença MIT.