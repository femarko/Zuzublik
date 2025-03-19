FROM python:3.10-alpine
COPY . .
RUN pip install -r requirements.txt
WORKDIR /app
CMD ["sh", "-c", "python3 -m db.create_db && python3 -m entrypoints.bot"]