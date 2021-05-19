FROM node:14

ADD package.json /tmp/package.json

RUN cd /tmp && npm install

RUN mkdir -p /opt/app && cp -a /tmp/node_modules /opt/app

WORKDIR /opt/app

COPY . .

# TODO: "yarn build" will only do a production build, it has be deployed manually.So the ENTRYPOINT should be customised.
# RUN yarn build

EXPOSE 3000

ENTRYPOINT ["npm", "start"]