# Genera Intelligence - Backend Core (Sprint 2)

Este diretório contém o coração do ecossistema de Inteligência Artificial da nossa solução, sendo responsável pela ingestão de dados na base vetorial, orquestração de agentes dinâmicos via **LangGraph** e integração com os modelos de linguagem do **Amazon Bedrock**.

## 🏗️ Estrutura de Pastas

A arquitetura foi desenhada seguindo os princípios de modularidade e Clean Architecture para separação de responsabilidades:

```text
backend/
├── agents/          # Definição dos grafos e nós do LangGraph (Supervisor e Especialistas)
├── api/             # Camada de exposição da aplicação (Rotas e Endpoints FastAPI)
│   └── routes/      # Controladores de rotas (ex: chat.py)
├── core/            # Configurações globais, segurança e variáveis de ambiente
├── domain/          # Entidades de negócio e contratos de dados (Schemas Pydantic)
├── services/        # Serviços de suporte (Conexão com a Base Vetorial e RAG)
└── main.py          # Ponto de entrada (Bootstrap) da aplicação FastAPI

```

## 🚀 Como Executar Localmente

Siga os passos abaixo para configurar o ambiente virtual e rodar o servidor de desenvolvimento:

### 1. Pré-requisitos

Certifique-se de ter o Python 3.10 ou superior instalado na sua máquina.

### 2. Configuração do Ambiente Virtual

Navegue até a pasta `src/backend` no seu terminal e execute:

```bash
# Criação do ambiente virtual
python3 -m venv .venv

# Ativação do ambiente (Linux/macOS)
source .venv/bin/activate

# Ativação do ambiente (Windows)
.venv\Scripts\activate

```

### 3. Instalação de Dependências

Com o ambiente virtual ativo, instale as bibliotecas necessárias:

```bash
pip install -r requirements.txt

```

### 4. Executar a API

Para levantar o servidor local com suporte a *hot-reload* (atualização automática ao salvar os arquivos):

```bash
uvicorn main:app --reload

```

A API ficará disponível em: `http://localhost:8000`

A documentação interativa do Swagger poderá ser acessada em: `http://localhost:8000/docs`

## 🔌 Contrato de API Estabelecido

### Endpoint: `POST /api/chat`

Interface de comunicação utilizada pelo Front-end para enviar as dúvidas dos usuários e receber as respostas fundamentadas via RAG.

* **Request Body (Envio):**

```json
{
  "paciente_id": "string (uuid)",
  "mensagem": "string"
}

```

* **Response Body (Retorno):**

```json
{
  "resposta": "string",
  "fontes": [
    {
      "painel": "string",
      "marcador": "string",
      "gene": "string",
      "conclusao_curta": "string"
    }
  ]
}

```
