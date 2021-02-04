FROM selenium/standalone-chrome

USER root
WORKDIR /testeo

RUN apt-get update -y
RUN apt-get install -y nano
RUN apt-get install -y python3-pip
RUN python3 -m pip install selenium