FROM python:3.10-alpine
WORKDIR /Zuzublik
COPY . /Zuzublik
RUN pip install -r requirements.txt
CMD ["sh", "-c", "python3 -m app.dp.create_db && python3 -m app.entrypoints.bot"]
