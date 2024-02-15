FROM node:16.10.0-alpine as build
WORKDIR /app
COPY package*.json ./

RUN npm config set registry https://registry.npm.taobao.org/
RUN npm install --production

COPY . .

RUN npm run build

CMD [ "npm", "run", "dev" ]