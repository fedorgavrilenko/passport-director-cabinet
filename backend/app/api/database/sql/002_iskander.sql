CREATE TABLE users (
    id SERIAL PRIMARY KEY,
    email TEXT UNIQUE NOT NULL,
    name TEXT
);

INSERT INTO users (email, name)
VALUES 
    ('test1@example.com', 'Alice'),
    ('test2@example.com', 'Bob');