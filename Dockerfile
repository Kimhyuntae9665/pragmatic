FROM python:3.9.0

WORKDIR /home/

RUN git clone https://github.com/Kimhyuntae9665/pragmatic.git

WORKDIR /home/pragmatic/

RUN pip install -r requirements.txt

RUN pip install gunicorn

RUN echo "SECRET_KEY= django-insecure-%)y6b2=%%&+^&a38!a83k0@%!egosn@e$0io8s6^ve52w5+_@k" > .env

RUN python manage.py migrate

RUN python manage.py collectstatic

EXPOSE 8000

CMD ["gunicorn", "pragmatic.wsgi", "--bind", "0.0.0.0:8000"]