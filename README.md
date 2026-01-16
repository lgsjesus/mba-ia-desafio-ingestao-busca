# Desafio MBA Engenharia de Software com IA - Full Cycle

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