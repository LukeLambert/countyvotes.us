FROM node:17-alpine
RUN npm install -g sass@"<2"
WORKDIR /data
CMD ["sass", "--style", "compressed", "--watch", "scss:css"]
