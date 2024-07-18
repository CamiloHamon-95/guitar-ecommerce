FROM python:3.10

ENV PYTHONUNBUFFERED=1

WORKDIR /app

RUN python -m pip install --upgrade pip

RUN apt-get update

RUN apt-get -y install iputils-ping

RUN apt-get -y install vim

COPY requirements.txt requirements.txt

RUN pip install -r requirements.txt

COPY . .

COPY ./entrypoint.sh .

ENTRYPOINT [ "sh", "entrypoint.sh" ]