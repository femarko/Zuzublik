FROM python:3.10-alpine
COPY . .
RUN pip install -r requirements.txt
ENV PYTHONPATH /:$PYTHONPATH
CMD ["sh", "-c", "python3 -m app.dp.create_db && python3 -m app.entrypoints.bot"]
