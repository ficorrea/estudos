FROM python:3.13-alpine

ENV PYTHONUNBUFFERED=1 \
	PIP_NO_CACHE_DIR=1 \
	DEBIAN_FRONTEND=noninteractive

WORKDIR /app

COPY requirements.txt ./
RUN pip install --upgrade pip setuptools wheel \
	&& pip install --no-cache-dir -r requirements.txt

COPY . .

RUN adduser --disabled-password --gecos "" appuser \
	&& chown -R appuser:appuser /app
USER appuser

EXPOSE 8501

CMD ["streamlit", "run", "app.py", "--server.port", "8501", "--server.address", "0.0.0.0"]

