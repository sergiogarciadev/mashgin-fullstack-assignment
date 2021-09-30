FROM node:16 AS builder

WORKDIR /app

COPY package.json .
COPY package-lock.json .

RUN npm ci

COPY . .

RUN npm run build

FROM nginx

WORKDIR /usr/share/nginx/html

COPY --from=builder /app/dist .
COPY deploy/default.conf /etc/nginx/conf.d/
