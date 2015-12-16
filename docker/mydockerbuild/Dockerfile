FROM docker/whalesay:latest
RUN apt-get -y update && apt-get isntall -y fortunes
CMD /usr/games/fortune -a | cowsay
