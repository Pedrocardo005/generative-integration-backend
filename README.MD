# Treino integração IA generativa

Este repositório tem por objetivo criar uma integração com alguma ia generativa.

## Como rodar o projeto

1. Crie um ambiente virtual
```bash
python -m venv env
```

2. Ative o ambiente virtual
```bash
source env/bin/activate
```

3. Instale as dependências do arquivo `requirements.txt`
```bash
pip install requirements.txt
```

4. Aplique as migrações
```bash
python backend/manage.py migrate
```

5. Adicione sua chave da api gemini nas variável de ambiente `GEMINI_API_KEY`, ou se preferir, altere o arquivo `backend > backend > settings.py` na seguinte linha:
```python
GEMINI_API_KEY = os.getenv('GEMINI_API_KEY', '<suaChave>')
```
