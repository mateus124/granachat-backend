# Granachat Backend

API do **Granachat**, um app de controle financeiro por linguagem natural (estilo chat), construída com **FastAPI**, **uv**, **Docker** e **PostgreSQL**.

---

## Tecnologias

* **Python 3.11+**
* **FastAPI**
* **uv** (gerenciador de dependências e venv)
* **Docker & Docker Compose** (PostgreSQL)
* **SQLAlchemy**

## Setup local (passo a passo)

### Clonar o repositório

```bash
git clone https://github.com/mateus124/granachat-backend
cd granachat-backend
```

---

### Instalar o **uv**

```bash
pip install uv
```

---

### Inicializar o ambiente virtual

```bash
uv venv
```

Ativar o ambiente:

```bash
source .venv/bin/activate   # Linux / Mac
# .venv\\Scripts\\activate  # Windows
```

---

### Instalar dependências

```bash
uv sync
```

---

### Configurar variáveis de ambiente

Copie o arquivo de exemplo:

```bash
cp .env.example .env
```

Edite o `.env` conforme necessário:

```env
DATABASE_URL=postgresql://example:example@localhost:5432/example
SECRET_KEY=segredo_secreto
```

---

### Subir o banco de dados

Certifique-se de que o Docker está rodando, então execute:

```bash
docker compose up -d
```

---

### Rodar a API 

```bash
fastapi dev app/main.py
```

A API estará disponível em:

* **[http://127.0.0.1:8000](http://127.0.0.1:8000)**
* **Docs Swagger:** [http://127.0.0.1:8000/docs](http://127.0.0.1:8000/docs)

---