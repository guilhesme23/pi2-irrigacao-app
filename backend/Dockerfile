FROM python:3.10

ENV TZ=America/Sao_Paulo

WORKDIR /backend

RUN apt-get update && \
	apt-get -qq -y install netcat-openbsd

COPY requirements.txt .

RUN pip install -r requirements.txt

COPY . .

EXPOSE 5000

CMD ["uvicorn", "api.src.main:app", "--host", "0.0.0.0", "--port", "5000"]
