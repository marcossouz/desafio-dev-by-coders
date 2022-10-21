FROM python:3.9.6

ENV PYTHONUNBUFFERED 1

WORKDIR /api

COPY requirements.txt ./

RUN pip install --upgrade pip

RUN pip install -r requirements.txt

COPY . .

VOLUME /api

EXPOSE 8080

CMD python manage.py makemigrations && python manage.py migrate && python manage.py runserver 0.0.0.0:8000