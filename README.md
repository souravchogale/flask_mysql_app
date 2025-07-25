# FLASK_MYSQL_APP

Project Description – Flask + MySQL Two-Tier Application (Dockerized)
 I built a simple two-tier web application that demonstrates containerized application deployment using Flask (Python) for the application layer and MySQL as the database layer — all managed using Docker Compose.
The application connects to a MySQL database and dynamically displays data on a web page using a Flask server..
Key Features:
 Flask backend connecting to MySQL


 Dockerized with multi-container architecture


 Auto DB initialization via init.sql


 Deployed and tested on AWS EC2 (Ubuntu)



Technologies Used:
Python (Flask)


MySQL


Docker


Docker Compose


EC2 (AWS)


Linux (Ubuntu 22.04)



 
Screenshots:

 GitHub Repository:
https://github.com/souravchogale/flask_mysql_app

 How to Use:
git clone https://github.com/yourusername/flask-mysql-app.git
cd flask-mysql-app
docker-compose up --build

Visit: http:52.91.65.29:5000 or your EC2 public IP