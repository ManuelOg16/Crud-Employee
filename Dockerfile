FROM python:3.8.5-alpine
RUN apk update
RUN apk add gcc libc-dev g++ libffi-dev libxml2 unixodbc-dev mariadb-dev postgresql-dev
WORKDIR /app
COPY . /app
RUN pip3 install -r requirements.txt

CMD ["python3", "main.py"]