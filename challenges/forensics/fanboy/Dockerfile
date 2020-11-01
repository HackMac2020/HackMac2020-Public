
FROM node:latest

WORKDIR /app

COPY server.js package.json package-lock.json ./

RUN npm ci

COPY src/ ./src
COPY public/ ./public

RUN npm run build

EXPOSE 1337

CMD [ "node", "server.js" ]
