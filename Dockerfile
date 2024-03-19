FROM python:3.11-alpine

# Ustawiamy zmienną środowiskową
ENV APP_HOME /app

# Instalujemy narzędzia deweloperskie PostgreSQL i libpq-dev
RUN apk update && \
    apk add postgresql-dev gcc python3-dev musl-dev

# Kopiujemy pliki do katalogu roboczego kontenera
WORKDIR $APP_HOME
COPY . .

# Instalujemy zależności Pythona
RUN pip install --no-cache-dir -r requirements.txt

# Oznaczamy port, na którym aplikacja działa wewnątrz kontenera
EXPOSE 5000

# Uruchamiamy naszą aplikację wewnątrz kontenera
CMD ["python", "main.py"]
