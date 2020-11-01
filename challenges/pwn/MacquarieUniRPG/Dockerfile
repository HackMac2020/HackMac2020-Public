# docker build -t mqurpg .
# docker run --privileged -d -p 1337:1337--rm --name mqurpg mqurpg

FROM jordanbertasso/bin-builder32 AS builder
COPY ./challenge /challenge
WORKDIR /challenge
RUN gcc -m32 -O0 -fno-stack-protector -no-pie -o MacquarieGame MacquarieGame.c

FROM jordanbertasso/nsjail32
COPY --from=builder /challenge/MacquarieGame /home/ctf/chal/
COPY FLAG.txt /home/ctf/chal/flag.txt
EXPOSE 1337/tcp
CMD ["/chal/MacquarieGame"]