# Use the official Python 3.12 image.
FROM python:3.8-slim-buster


# Set the working directory inside the container.
WORKDIR /app

COPY . /app

RUN pip install --upgrade pip

COPY requirements.txt .

RUN pip install --no-cache-dir -r requirements.txt

EXPOSE 5000

CMD ["python", "app.py"]