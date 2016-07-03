FROM ubuntu:14.04
RUN apt-get update && apt-get -y upgrade
RUN apt-get install -y python3 python3-pip
RUN apt-get install -y python3-matplotlib
RUN apt-get install -y libpq-dev python3-dev
RUN apt-get install -y python3-numpy
RUN apt-get install -y python3-scipy
ENV PYTHONUNBUFFERED 1
RUN mkdir /code
RUN mkdir /srv/logs
WORKDIR /code
COPY requirements.txt /code/
COPY . /code
RUN pip3 install -r requirements.txt
