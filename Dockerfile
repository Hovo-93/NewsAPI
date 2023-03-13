FROM python:3.9.6

RUN python -m pip install --upgrade pip
COPY ./ ./
RUN pip install -r requirements.txt
CMD gunicorn NewsService.wsgi -b 0.0.0.0:8080
COPY ./docker-entrypoint.sh /docker-entrypoint.sh
RUN  chmod +x /docker-entrypoint.sh
ENTRYPOINT ["/docker-entrypoint.sh"]