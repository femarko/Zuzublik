FROM python:3.10-alpine
COPY . .
RUN pip install -r requirements.txt
WORKDIR /app
CMD ["sh", "-c", "python3 db/create_db.py && python3 entrypoints/bot.py"]
