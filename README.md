# Dockerized API w/ Postgres 

This project demonstrates a simple deployment of two Docker containers that communicate with each other. The first container hosts an API service that returns a string, which it retrieves from a second service connected to a PostgreSQL database. The database is seeded with the string "hello world".

## Requirements

- Docker
- Docker Compose

## Services

### Service1 is the API Service

- **Path**: `./service1`
- **Description**: Exposes an API endpoint. Requests a string from Service 2.
- **Dependencies**: Flask, Requests

### Service2 is Database Service

- **Path**: `./service2`
- **Description**: Connects to a PostgreSQL database and retrieves the string stored in the database.
- **Dependencies**: Flask, psycopg2-binary
- **Database**: PostgreSQL, seeded with "hello world"

# Setup and Running

### Run the following bash commands

```bash
git clone https://github.com/UPatel12/flask-postgres.git
cd flask-postgres
docker-compose up --build
curl http://localhost:5001/messages
```
