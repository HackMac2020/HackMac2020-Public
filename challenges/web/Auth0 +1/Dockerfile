FROM node:latest

COPY src/ .

RUN npm ci

EXPOSE 1337

CMD [ "node", "index.js" ]