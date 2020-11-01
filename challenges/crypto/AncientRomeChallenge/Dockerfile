FROM python:3.9.0-buster

WORKDIR /app

COPY requirements.txt ./

RUN pip install -r requirements.txt

COPY main.py run.sh ./
COPY static ./static
COPY templates ./templates

RUN find .

EXPOSE 1337

ENTRYPOINT [ "./run.sh" ]
