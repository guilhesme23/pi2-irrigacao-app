# build environment
FROM node:16-alpine as build

WORKDIR /app

ENV PATH /app/node_modules/.bin:$PATH

COPY package.json /app/package.json

RUN npm install

COPY ./src /app/src

COPY ./public /app/public

RUN npm run build

# production environment
FROM nginx:1.16.0-alpine

COPY --from=build /app/build /usr/share/nginx/html

EXPOSE 80

# CMD [“nginx”, “-g”, “daemon off;”]