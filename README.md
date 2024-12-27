# Flask-MySQL Dockerized Application

A Flask-based web application with MySQL integration, fully containerized using Docker. 
This project provides a simple setup to run a Flask application connected to a MySQL database, leveraging Docker Compose for ease of deployment.

## Features
1. Flask Application: Powered by Python's lightweight Flask framework.
2. MySQL Database: Integrated MySQL database for persistent data storage.
3. Dockerized Application: Seamless containerization with Docker and Docker Compose.
4. Environment-Based Configuration: Centralized configuration using .env file for sensitive data.
5. Email Notifications: Integrated SMTP settings for sending emails.

## Prerequisites

Before you begin, ensure you have the following installed on your machine:

1. **Git**  
   Download and install Git: [Git Downloads](https://git-scm.com/downloads)

2. **Docker**  
   Download and install Docker: [Docker Desktop](https://www.docker.com/products/docker-desktop/)

3. **Docker Compose**  
   Included with Docker Desktop. Check version with:
   ```bash
   docker-compose --version
   ```

## Clone The Repository
To get started with the project, clone the repository using Git:
```bash
git clone https://github.com/riddhigupta1110/first-docker-playground.git
```
Navigate to the project directory:
```bash
cd first-docker-playground
```


## Create a .env File

The application relies on environment variables stored in a .env file. Create the .env file in the root directory with the following content:  
DB_HOST=mysql  
DB_PORT=3306  
DB_USER=root  
DB_PASSWORD=yourpassword  
DB_NAME=testdb  

SMTP_SERVER=smtp.gmail.com  
SMTP_PORT=465  
SMTP_USE_TLS=False  
SMTP_USE_SSL=True  
SMTP_USER=your-email@example.com  
SMTP_PASSWORD=your-email-password  
SMTP_DEFAULT_SENDER=your-email@example.com  

## Build the Docker Containers:
```bash
docker-compose up --build
```
This will build both the Flask and MySQL containers, ensuring that MySQL creates the correct database (testdb). It will also create volumes if they are defined in the docker-compose.yml file and do not already exist. If the volumes are already present, Docker Compose will reuse them.   
The command also starts the containers as necessary.

## Check MySQL Container Status
This will list all running containers.
```bash
docker ps
```

## Check Database Creation in MySQL   
If MySQL is running, you can check if the database was created successfully. To do this:  
1. Access the MySQL container:
```bash
docker exec -it mysql-db bash
```
2. Open the MySQL CLI:
```bash
mysql -u root -p
```
3. When prompted for the password, enter the password you set in the "MYSQL_ROOT_PASSWORD" environment variable.
4. Once logged in, list the databases:
```sql
SHOW DATABASES;
```

## Access Flask App
Finally, you can try accessing your Flask app by visiting http://localhost:5000/ in your browser.

## Stop and Remove Containers:
1. Stop and remove the containers:
```bash
docker-compose down
```
3. Remove any existing volumes (this will erase all data stored in MySQL):
```bash
docker-compose down -v
```
This command will remove the containers and the associated volumes, so any old database data will be removed, and MySQL will re-initialize next time you use the `docker-compose up --build` command.
