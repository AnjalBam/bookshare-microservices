FROM node:18-alpine

WORKDIR /app/test_server/

COPY package*.json ./

RUN npm install 

COPY . .

CMD ["npm", "run", "start"]