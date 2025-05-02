-- Creates table users with id, email, name attributes
-- id is primary key, auto increment
-- email is unique and not null
-- name is optional string
-- Script shouldn't fail if table exists
CREATE TABLE IF NOT EXISTS users (
    id INT AUTO_INCREMENT PRIMARY KEY,
    email VARCHAR(255) NOT NULL UNIQUE,
    name VARCHAR(255)
);
