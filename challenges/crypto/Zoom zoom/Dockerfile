FROM python:3.8

WORKDIR /chal

COPY weak_xor_server.py .
COPY sentences.json .

RUN useradd -r -u 1000 ctf

EXPOSE 1337 
USER ctf
CMD ["python","./weak_xor_server.py"]