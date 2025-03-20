FROM python:3.10-alpine
COPY . .
RUN pip install -r requirements.txt
#WORKDIR /src
#CMD ["sleep", "infinity"]
CMD ["sh", "-c", "python3 -m src.app.db.create_db && python3 -m src.app.entrypoints.bot"]

#FROM python:3.10-alpine
#COPY . .
#RUN pip install -r requirements.txt
#RUN pwd
#RUN ls -l src
#WORKDIR /src
#CMD ["sh", "-c", "python3 -m app.db.create_db && python3 -m app.entrypoints.bot"]