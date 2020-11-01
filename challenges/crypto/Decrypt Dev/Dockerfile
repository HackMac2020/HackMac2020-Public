# sudo docker build -t crypto .
# docker run --privileged -d -p 1337:1337 --rm --name crypto crypto

FROM ubuntu:18.04

COPY --from=jordanbertasso/nsjail /usr/bin/nsjail /usr/bin/nsjail

RUN apt-get update && \
    apt-get install -y libprotobuf10 libnl-route-3-200 openssh-server && \
    rm -rf /var/lib/apt/lists/*
RUN mkdir /var/run/sshd

COPY user_shell.sh root_shell.sh /bin/
RUN chsh -s /bin/root_shell.sh

RUN echo 'root:ClaudeShannon' | chpasswd
RUN sed -i 's/#*PubkeyAuthentication yes/PubkeyAuthentication no/g' /etc/ssh/sshd_config
RUN sed -i 's/#*PermitRootLogin prohibit-password/PermitRootLogin yes/g' /etc/ssh/sshd_config
# SSH login fix. Otherwise user is kicked off after login
RUN sed -i 's@session\s*required\s*pam_loginuid.so@session optional pam_loginuid.so@g' /etc/pam.d/sshd
RUN sed -i 's/#Port 22/Port 1337/g' /etc/ssh/sshd_config

#Place flag
COPY ./FLAG.txt /root/FLAG.txt

#Configure user
RUN useradd -d /home/ctf/ -m -p ctf -s /bin/user_shell.sh ctf
RUN echo "ctf:ctf" | chpasswd

WORKDIR /home/ctf
EXPOSE 1337

COPY challenge .
RUN chown -R root:root /home/ctf

COPY docker-entrypoint.sh /docker-entrypoint.sh

ENTRYPOINT [ "/docker-entrypoint.sh" ]
