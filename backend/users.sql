CREATE DATABASE IF NOT EXISTS sistema;
use sistema;

CREATE TABLE IF NOT EXISTS USERS (
    ID INT PRIMARY KEY NOT NULL AUTO_INCREMENT,
    username VARCHAR(50) NOT NULL UNIQUE,
    password VARCHAR(50)
);

INSERT INTO USERS (username, password)
VALUES 
    ('admin', 'admin'),
    ('Adila', '1234');

SELECT * FROM USERS;
