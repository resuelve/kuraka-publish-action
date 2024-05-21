FROM alpine:3.19

RUN apk --update add curl bash

COPY entrypoint.sh /entrypoint.sh

ENTRYPOINT ["/entrypoint.sh"]
