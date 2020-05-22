FROM alpine:latest
RUN apk update
RUN apk add curl
EXPOSE 8080
