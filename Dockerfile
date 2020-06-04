FROM python:3.7.7


# OUR WORKING DIRECTORY
RUN mkdir /code

# INSTALL REQUIREMENTS
ADD requirements.txt /code/requirements.txt
WORKDIR /code
RUN pip3 install -r requirements.txt

RUN pip3 install jupyterlab

ADD . /code/

EXPOSE 8888

ENV LANG=ru_RU.UTF-8
ENV LC_ALL=ru_RU.UTF-8
ENV LANGUAGE=ru_RU.UTF-8
ENV PYTHONIOENCODING=utf-8
