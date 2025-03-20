FROM python:3.10-alpine
COPY . .
RUN pip install -r requirements.txt
CMD ["sh", "-c", "python3 -m src.app.db.create_db && python3 -m src.app.entrypoints.bot"]
