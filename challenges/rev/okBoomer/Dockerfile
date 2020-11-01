# make build
# docker run --privileged --rm -d -p 1337:1337 -v $(pwd):/host --name ok-boomer ok-boomer
# make exec
# cp home/ctf/chal/server_exec /host

FROM jordanbertasso/bin-builder AS builder
COPY ./src /challenge
WORKDIR /challenge
RUN gcc -o server_exec server_exec.c -lm
RUN gcc -o boom boom.c -lm

FROM jordanbertasso/nsjail
COPY --from=builder /challenge/server_exec /home/ctf/chal/
COPY --from=builder /challenge/boom /home/ctf/chal/
EXPOSE 1337/tcp
CMD ["/chal/server_exec"]