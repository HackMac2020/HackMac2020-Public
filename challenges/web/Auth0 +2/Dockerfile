FROM node:latest

COPY . .

WORKDIR /src

RUN npm ci

EXPOSE 1337 

CMD [ "node", "index.js" ]