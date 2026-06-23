# What is Docker?
""" Docker is a containerization platform that allows us to package an application 
along with its dependencies, runtime, libraries, and configuration into a container. 
This ensures the application runs consistently across different environments such as development, 
testing, and production."""

# What is a Dockerfile?
""" A Dockerfile is a text file containing instructions used to build a Docker image. It defines 
the base image, dependencies to install, files to copy, environment variables, and the command 
that should run when the container starts."""

"For Docker File"
# 1. Which base OS/image am I starting from?
# 2. Which directory am I working in?
# 3. Which files am I copying?
# 4. Which commands run during build?
# 5. Which command runs when container starts?
# FastAPI-Docker example
"""
FROM python:3.13-slim
WORKDIR /app
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt
COPY . .
EXPOSE 8000
CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8000"]
"""

# What is Docker Compose?
""" Docker Compose is a tool used to define and manage multi-container applications 
using a YAML file. Instead of running multiple containers manually, we can define services 
such as FastAPI, PostgreSQL, Redis, and Celery in a single compose file and start them together.

Command to start sercices: docker compose up
"""

"For Docker Compose"
# 1. What containers are being created?
# 2. How do they communicate?
# 3. Which ports are exposed?
# 4. Which environment variables are injected?
# 5. Which data is persisted using volumes?
# Docker compose Example
"""
services:

  app:
    build: .
    ports:
      - "8000:8000"

    environment:
      DATABASE_URL: postgresql://postgres:root@db:5432/postgres

    depends_on:
      - db

  db:
    image: postgres:17

    environment:
      POSTGRES_DB: postgres
      POSTGRES_USER: postgres
      POSTGRES_PASSWORD: root

    volumes:
      - postgres_data:/var/lib/postgresql/data

volumes:
  postgres_data:
"""

#Difference Between Docker and Docker Compose
"""| Docker                              | Docker Compose                           |
| ----------------------------------- | ---------------------------------------- |
| Creates and runs a single container | Manages multiple containers              |
| Uses Dockerfile                     | Uses docker-compose.yml                  |
| `docker run`                        | `docker compose up`                      |
| Suitable for individual containers  | Suitable for complete application stacks |
"""

#What is a Docker Image?
""" A Docker image is a read-only template that contains the application code, runtime, 
libraries, dependencies, and configuration required to run an application. 
Containers are created from images.
Command to create image: docker build -t fastapi-app ."""

# What is a Docker Container?
"""A container is a running instance of a Docker image. Multiple containers can be created 
from the same image, each running independently.
Command to start container: docker run fastapi-app"""