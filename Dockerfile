FROM python:3.9.6

WORKDIR /code
COPY . .
RUN python -m pip install --upgrade pip
RUN pip install -r requirements.txt
RUN pip install gunicorn

