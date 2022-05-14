FROM python:3.7
USER root
RUN apt-get -y update
RUN apt-get -y install locales && localedef -f UTF-8 -i ja_JP ja_JP.UTF-8
RUN apt-get install -y vim less libpq-dev

ENV LANG ja_JP.UTF-8
ENV LANGUAGE ja_JP:ja
ENV LC_ALL ja_JP.UTF-8
ENV TZ JST-9

RUN mkdir -p /root/src
WORKDIR /root/src

RUN pip install --upgrade pip
RUN pip install --upgrade setuptools
RUN pip install --upgrade pip setuptools
RUN pip install mysqlclient
RUN pip install requests
