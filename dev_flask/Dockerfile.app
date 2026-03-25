# Opção 1: Se for outro Python app
FROM python:3.11-alpine

ENV PYTHONUNBUFFERED=1
ENV PYTHONPATH=/app

WORKDIR /app

# Copiar todo o projeto
COPY . .

# Comando
CMD ["python", "app.py"]