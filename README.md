# Dockerized API w/ Postgres 

This project demonstrates a simple deployment of two Docker containers that communicate with each other. The first container hosts an API service that returns a string, which it retrieves from a second service connected to a PostgreSQL database. The database is seeded with the string "hello world".

## Requirements

- [Docker](https://docs.docker.com/get-docker/)
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

## Setup and Installation

### 1. Initial setup
- Clone the repo locally and cd into the directory 
```bash
git clone https://github.com/UPatel12/flask-postgres.git 
cd flask-postgres
```
### 2. Run Docker container
- There should be 3 running containers. You can check this by running `docker ps --all`

```bash
docker-compose up --build
```

### 3. Test

#### Fetch the first database entry 

```bash
curl http://localhost:5001
``` 

OUTPUT: `hello world`

#### Fetch all the entries 

```bash 
curl http://localhost:5001/messages
``` 

OUTPUT: `[[1,"hello world"],[2,"hi world"],[3,"sup world"],[4,"bye world"]]`


