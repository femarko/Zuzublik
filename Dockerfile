FROM python:3.10-alpine
COPY . .
RUN pip install -r requirements.txt
CMD ["python3", "-m", "app.dp.create_db"]
CMD ["python3", "-m", "app.entrypoints.bot"]