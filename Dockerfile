FROM python:latest

SHELL ["/bin/bash", "-c"]

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

RUN pip install --upgrade pip

RUN apt update && apt -qy install gcc libjpeg-dev libxslt-dev \
    libpq-dev libmariadb-dev libmariadb-dev-compat gettext cron openssh-client flake8 locales vim

RUN useradd -rms /bin/bash mike && chmod 777 /opt /run

WORKDIR /mike

RUN mkdir /mike/static && mkdir /mike/media && chown -R mike:mike /mike && chmod 755 /mike

COPY --chown=mike:mike . .

RUN pip install -r requirements.txt

USER mike

CMD ["gunicorn","-b","0.0.0.0:8001","soaqaz.wsgi:application"]
