
FROM python:3.6.8

WORKDIR /app

COPY requirements.txt .

EXPOSE 5000

RUN pip install --upgrade pip

RUN pip install -r requirements.txt

ENTRYPOINT ["/usr/local/bin/python", "app.py"]

COPY . .
