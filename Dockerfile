FROM ubuntu:18.04

MAINTAINER Rohit Kaushik "rohit.koush@gmail.com"

RUN apt-get update -y && \
    apt-get install -y python-pip python-dev

# We copy just the requirements.txt first to leverage Docker cache
COPY ./requirements.txt /app/requirements.txt

WORKDIR /app

RUN pip install -r requirements.txt

COPY . .

EXPOSE 5001

ENTRYPOINT [ "python" ]

CMD [ "./src/top_trumps.py" ]
