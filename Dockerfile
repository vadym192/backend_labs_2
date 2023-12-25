FROM python:3.11.3-slim-bullseye

WORKDIR /app

COPY requirements.txt .

RUN python -m pip install -r requirements.txt

COPY . /app

EXPOSE 5070

CMD flask --app main run -h 0.0.0.0 -p $PORT
