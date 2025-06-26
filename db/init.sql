CREATE DATABASE IF NOT EXISTS testdb;
USE testdb;

CREATE TABLE IF NOT EXISTS messages (
  id INT AUTO_INCREMENT PRIMARY KEY,
  message VARCHAR(255) NOT NULL
);

INSERT INTO messages (message) VALUES
("Hello from Sourav!"),
("This is my Flask + MySQL + Docker Project with CI-CD Automation!");
