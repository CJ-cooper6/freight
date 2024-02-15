FROM node:16-slim as builder
WORKDIR /app
COPY package*.json ./

RUN npm cache clean --force
RUN npm install --loglevel=verbose

COPY . .

RUN npm run build
EXPOSE 5173

CMD [ "npm", "run", "dev" ]