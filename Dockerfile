FROM python:3.10-buster


RUN apt-get update

RUN mkdir -p /home/myapp/app
WORKDIR /home/myapp/app

ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1
ENV PATH $PATH:/home/myapp/.local/bin

COPY requirements.txt .
RUN pip install pip --upgrade
RUN pip install -r requirements.txt
ADD . .
RUN python manage.py collectstatic --no-input --clear


EXPOSE 8000

