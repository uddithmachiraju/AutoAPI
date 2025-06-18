FROM python:3.11-slim
WORKDIR /app
COPY . .
RUN pip install --no-cache-dir -e .
EXPOSE 5000
CMD ["autoapi", "run", "--config=config.yaml"]
