FROM ayiinxd/lintaralfarozi:buster

RUN git clone -b lintaralfarozi https://github.com/Lintaralfarozi/lintaralfarozi /home/lintaralfarozi/ \
    && chmod 777 /home/lintaralfarozi \
    && mkdir /home/lintaralfarozi/

COPY ./sample_config.env ./config.env* /home/lintaralfarozi/

WORKDIR /home/lintaralfarozi/

CMD ["bash","start"]
