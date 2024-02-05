FROM python:3.9-slim-bullseye

ENV PYTHONUNBUFFERED=1
ENV PYTHONDONTWRITEBYTECODE=1

RUN apt-get update && apt-get install -y libpq-dev gcc && rm -rf /var/lib/apt/lists/*

WORKDIR /app

COPY requirements /app/requirements
RUN pip install -r /app/requirements/development.txt

COPY . /app

CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]
