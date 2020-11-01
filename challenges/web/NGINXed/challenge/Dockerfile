# Builder
FROM node AS dependencies

WORKDIR /build

COPY ./src/package.json ./src/package-lock.json ./

RUN npm set progress=false && \
    npm config set depth 0 && \
    npm install --only=production

# Runner
FROM nginx:1.19.2

RUN apt-get update && apt-get install -y nodejs

WORKDIR /app

COPY --from=dependencies /build/node_modules ./src/node_modules

COPY ./src/nginx.conf /etc/nginx/nginx.conf

COPY . . 

EXPOSE 1337

CMD [ "./docker-entrypoint.sh" ]
