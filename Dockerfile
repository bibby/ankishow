FROM ubuntu:14.04

RUN apt-get update && apt-get install -y \
  python-pip

ENV PIP_NO_CACHE_DIR off
ENV PIP_DISABLE_PIP_VERSION_CHECK on

RUN pip install -U 'pip<9'

WORKDIR /usr/src
COPY . .

RUN pip install -r requirements.txt

EXPOSE 8000
ENV COLLECTION_ID 1
ENV FIELDS 1,2,3

CMD python app.py
