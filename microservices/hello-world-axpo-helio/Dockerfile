FROM python:3.7-alpine
EXPOSE 9090

WORKDIR /app

COPY hello_world_axpo_helio /app
COPY requirements.txt /app

RUN pip install --no-cache-dir -r requirements.txt

CMD ["python", "app.py"]