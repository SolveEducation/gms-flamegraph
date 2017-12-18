FROM alpine:3.7

RUN apk update && apk upgrade && apk add perl python3

RUN mkdir -p /opt/gms-flamegraph

ADD https://github.com/brendangregg/FlameGraph/raw/master/flamegraph.pl /opt/gms-flamegraph
COPY stackcollapse-gms.py /opt/gms-flamegraph

WORKDIR /opt/gms-flamegraph

ENTRYPOINT ["sh", "-c", "python3 stackcollapse-gms.py | perl ./flamegraph.pl"]
