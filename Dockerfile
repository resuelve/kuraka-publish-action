FROM python:3.12-alpine

COPY main.py /main.py

ENTRYPOINT ["/main.py"]
