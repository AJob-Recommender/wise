FROM python:3.9-slim-buster

WORKDIR /app

COPY requirements.txt .

RUN pip install -r requirements.txt
RUN pip install -U scikit-learn

COPY . .

EXPOSE 8080
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8080"]