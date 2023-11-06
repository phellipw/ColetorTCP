FROM python:3.9.18-bullseye
RUN mkdir app
COPY Coletor.py app
ENTRYPOINT [ "python3", "app/Coletor.py" ]
