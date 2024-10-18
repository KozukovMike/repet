FROM python:3.11.0

WORKDIR /app

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

RUN apt-get update \
    && apt-get install netcat -y
RUN apt-get upgrade -y && apt-get install postgresql gcc python3-dev musl-dev -y
RUN pip install --upgrade pip

RUN pip install --upgrade pip

COPY ./requirements.txt .

RUN pip install -r requirements.txt

COPY . .

COPY entrypoint.sh /entrypoint.sh
RUN chmod +x /entrypoint.sh

ENTRYPOINT ["/entrypoint.sh"]



#FROM python:3.11.0
#
#ENV PYTHONDONTWRITEBYTECODE 1
#ENV PYTHONUNBUFFERED 1
#
#WORKDIR /usr/src/mike
#
#COPY ./requirements.txt /usr/src/requirements.txt
#
#RUN pip install -r /usr/src/requirements.txt
#
#COPY . /usr/src/mike
#
#EXPOSE 8000
#CMD ["python","manage.py","runserver","0.0.0.0:8000"]
