FROM rastasheep/ubuntu-sshd

RUN apt-get update -y && \
    apt-get install -y python3-pip python3

COPY ./webapp/requirements.txt /app/requirements.txt

WORKDIR /app

RUN pip3 install -r requirements.txt

COPY ./webapp /app
COPY ./startup.sh /

RUN chmod 0755 /startup.sh

ENTRYPOINT ["/bin/bash" ,"/startup.sh"]