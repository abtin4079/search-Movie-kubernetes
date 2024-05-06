FROM python:3.9.19-alpine

WORKDIR /app
COPY . /app

RUN pip install fastapi
RUN pip install requests
RUN pip install pydantic
RUN pip install uvicorn
RUN pip install redis
RUN pip install elasticsearch
RUN pip install python-dotenv

EXPOSE 8000


CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000", "--reload"]