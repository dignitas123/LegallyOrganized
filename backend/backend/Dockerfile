# backend/Dockerfile
FROM python:3.8
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1
WORKDIR /code

# Copy the requirements.txt from the backend directory
COPY backend/requirements.txt /code/

# Install dependencies
RUN pip install -r requirements.txt

# Copy the entire project (including manage.py at the root)
COPY . /code/
