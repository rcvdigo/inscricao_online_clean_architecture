SHOW DATABASES;

CREATE DATABASE clean_arch;

USE clean_arch;

CREATE TABLE registrations
(
    id INT AUTO_INCREMENT,
    name VARCHAR(100) NOT NULL,
    email VARCHAR(100) NOT NULL,
    registration_number CHAR(11) NOT NULL,
    birth_date DATE NOT NULL,
    created_at DATETIME NOT NULL,
    CONSTRAINT table_name_pk
        PRIMARY KEY (id)
);

SHOW TABLES;

INSERT INTO registrations (name, email, registration_number, birth_date, created_at)
VALUES
('Ana Silva', 'ana@example.com', '12345678901', '1990-05-15', NOW()),
('Pedro Santos', 'pedro@example.com', '98765432109', '1985-08-25', NOW()),
('Maria Oliveira', 'maria@example.com', '45678901234', '1995-11-10', NOW());

SELECT *
FROM registrations;