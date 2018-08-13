FROM python:3.5-alpine
RUN apk add  --update build-base git python-dev bash curl file openssl perl sudo
ENV PYTHONUNBUFFERED 1

WORKDIR /usr/src/mecab/
RUN mkdir -p /temp/mecab_src/ && \
git clone https://github.com/taku910/mecab.git  /temp/mecab_src/ && \
mv -f /temp/mecab_src/mecab/* /usr/src/mecab/ && \
 ./configure  --enable-utf8-only && \
make && \
make install && \
rm -rf  /temp/mecab_src/  && \
rm -rf  /usr/src/mecab/

RUN git clone https://github.com/neologd/mecab-ipadic-neologd.git /usr/src/mecab-ipadic-neologd && \
/usr/src/mecab-ipadic-neologd/bin/install-mecab-ipadic-neologd -n -y && \
rm -rf  /usr/src/mecab-ipadic-neologd && \
pip install mecab-python3

WORKDIR  /root/
