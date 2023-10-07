FROM python:3.11
WORKDIR /app
COPY . .
RUN pip install -r requirements.txt
ENTRYPOINT [ "uvicorn src.main:app" ]
