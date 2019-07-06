FROM python:3.7

RUN apt-get update
RUN apt-get install -y python-pip
RUN pip install --upgrade pip

RUN mkdir -p /usr/local/api
WORKDIR /usr/local/api

COPY api ./
RUN pip install -r requirements.txt -U

# Run the image as a non-root user
RUN useradd -m myuser
USER myuser

RUN ls -a
CMD python manage.py migrate
CMD gunicorn --bind 0.0.0.0:$PORT config.wsgi