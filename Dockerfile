FROM python:3.9.6

WORKDIR /code
COPY . .
RUN python -m pip install --upgrade pip
RUN pip install -r requirements.txt
CMD gunicorn NewsService.wsgi:application --bind 0.0.0.0:8000
COPY ./docker-entrypoint.sh /docker-entrypoint.sh
RUN chmod +x /docker-entrypoint.sh
ENTRYPOINT ["/docker-entrypoint.sh"]