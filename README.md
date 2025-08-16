# 🧠 Visão Computacional EPI - Backend

Backend desenvolvido com **Flask** para detecção automática de EPIs (Equipamentos de Proteção Individual) utilizando **visão computacional** e **modelos YOLOv8** customizados.

A aplicação permite processar **imagens, vídeos e câmera ao vivo** via API REST, identificando automaticamente o uso (ou ausência) de capacetes e EPIs.

---

## ⚙️ Tecnologias Utilizadas

- Python 3.11+
- Flask
- OpenCV
- Ultralytics (YOLOv8)
- CVAT (anotação e treino dos dados)
- NumPy

---

## 🚀 Como inicializar o projeto

### 1. Clone o repositório

```bash
git clone https://github.com/LuanderV/visao-computacional-epi-back.git
cd visao-computacional-epi-back
```

### 2. Crie e ative o ambiente virtual

    # Windows
    py -3.11 -m venv venv
    .\venv\Scripts\activate

    # Linux/Mac
    python3.11 -m venv venv
    source venv/bin/activate

### 3. Instale as dependências

    pip install -r requirements.txt

### 4. Execute a aplicação

    python run.py

 - A API estará disponível em: http://localhost:5000

---