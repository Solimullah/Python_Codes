#FROM python:3.9-slim

#WORKDIR /app

#COPY requirements.txt .
#RUN pip install --no-cache-dir -r requirements.txt

#COPY ./app .

#CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]


FROM python:3.10-slim

WORKDIR /app

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY . .

# Optional: Make start.sh executable (if using it)
RUN chmod +x start.sh

# Expose the correct port
EXPOSE $PORT

# Run FastAPI app
CMD ["./start.sh"]

CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "$PORT"]
