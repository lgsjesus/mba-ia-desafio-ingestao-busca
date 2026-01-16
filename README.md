# Desafio MBA Engenharia de Software com IA - Full Cycle

## Configurar as váriaveis de ambiente no arquiv .env
```bash
GOOGLE_API_KEY="APIKEI"
GOOGLE_EMBEDDING_MODEL='models/embedding-001'
OPENAI_API_KEY="OPENAPIKEY"
OPENAI_EMBEDDING_MODEL='text-embedding-3-small'
DATABASE_URL="postgresql+psycopg://postgres:postgres@host.docker.internal:5432/rag"
PG_VECTOR_COLLECTION_NAME="gpt5_collection"
PDF_PATH="path_do_projeto\document.pdf"
```

### Instalar o ambiente virtual para usar as dependencias.
```bash
python -m venv venv
```

### Ativar ambiente virtual
```bash
.\venv\Scripts\activate
```

### Instalar todas dependencias do requirements.txt
```bash
pip install -r requirements.txt
```

### Inciar o banco de dados via docker-compose
```bash
docker-compose up -d --build
```

### Realizar a ingestão de dados do PDF
```bash
python src/ingest.py
```

### Iniciar chat e fazer as perguntas
```bash
python src/chat.py
```