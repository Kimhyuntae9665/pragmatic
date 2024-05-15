FROM python:3.9.0

WORKDIR /home/

RUN git clone https://github.com/Kimhyuntae9665/pragmatic.git

WORKDIR /home/pragmatic/

RUN pip install -r requirements.txt

RUN pip install gunicorn

RUN echo "bh)%81j&l@&t8lcd#sy-$(rf&xxfz4fw0)(o-39=xn1nv(x8+j" > .env

RUN python manage.py migrate

RUN python manage.py collectstatic

EXPOSE 8000

CMD ["gunicorn", "pragmatic.wsgi", "--bind", "0.0.0.0:8000"]