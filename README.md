# Desafio OnFly

## **1. Tecnologias Utilizadas**

- **Python 3.13**
- **Pandas** – Manipulação de dados
- **Matplotlib & Seaborn** – Visualização de dados
- **Requests** – Consumo da API
- **Logging** – Gerenciamento de logs
- **Docker & Docker Compose** – Contêinerização do projeto
---

## **2. Configuração do Ambiente (Sem Docker)**

### 🔹 **1. Clone o repositório**
```bash
git clone https://github.com/OtavioMendes12/DesafioTecnicoOnfly.git
```

### 🔹 **2. Crie um ambiente virtual e ative**
```bash
python -m venv .venv 
source .venv/bin/activate  # macOS/Linux
.venv\Scripts\activate  # Windows
```

### 🔹 **3. Instale as dependências**
```bash
pip install -r requirements.txt
```

### 🔹 **4. Execute o pipeline**
```bash
python main.py
```

---

## **3. Executando com Docker**

### 🔹 **1. Construir a imagem do Docker**
```bash
docker build -t pokemon-pipeline .
```

### 🔹 **2. Rodar o container manualmente**
```bash
docker run --rm pokemon-pipeline
```

### 🔹 **3. Executar via `docker-compose`**
```bash
docker-compose up --build
```

### 🔹 **4. Parar e remover o container**
```bash
docker-compose down
```

