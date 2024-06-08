
FROM python:3.7.3-alpine
# Ustawienie katalogu roboczego
WORKDIR /app
# Kopiowanie plików do kontenera
COPY requirements.txt .
# Instalacja zależności
RUN pip install -r requirements.txt
#Definiowanie domyślnego polecenia uruchomienia
CMD ["python", "your_app.py"]
