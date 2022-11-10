FROM node:18-alpine

WORKDIR /app/mool_dwar/

COPY package*.json ./

RUN npm install 

COPY . .

EXPOSE 4000

CMD ["npm", "run", "start"]