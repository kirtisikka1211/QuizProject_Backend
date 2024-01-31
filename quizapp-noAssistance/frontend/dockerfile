FROM node:18.2.0

WORKDIR /usr/src/frontend1

COPY package*.json ./

RUN npm install

COPY . .

RUN npm run build

EXPOSE 3001

CMD ["npm", "start"]
