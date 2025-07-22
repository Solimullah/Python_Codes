FROM node:18-alpine

WORKDIR /app

COPY package*.json ./
RUN npm install

COPY . .

# Build the production version
RUN npm run build

# Install serve to serve built files
RUN npm install -g serve

EXPOSE 4173

# Serve the built static files on the port Railway expects
CMD ["serve", "-s", "dist", "-l", "4173"]
