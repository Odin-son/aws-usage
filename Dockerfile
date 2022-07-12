FROM ubuntu:18.04

RUN apt-get update -y
# install selected python (in case that version 3.7)
RUN apt-get install python3.7 -y
RUN apt-get install python3-pip -y

# set symbolic link
RUN ln -s /usr/bin/python3.7 /usr/bin/python && \
    ln -s /usr/bin/pip3 /usr/bin/pip

# install git
RUN apt-get install git -y

# install pip requirements
ADD requirements.txt .
RUN python -m pip install -r requirements.txt

WORKDIR /app
ADD . /app
