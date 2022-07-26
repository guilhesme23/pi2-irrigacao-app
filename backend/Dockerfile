FROM python:3.10

ENV TZ=America/Sao_Paulo

WORKDIR /backend

RUN apt-get update && \
	apt-get -qq -y install netcat-openbsd

COPY requirements.txt .

RUN pip install -r requirements.txt

COPY . .

RUN chmod +x start.sh

EXPOSE 5000

CMD ./start.sh