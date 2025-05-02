-- Creates table users with id, email, name, and country attributes
-- id is primary key, auto increment
-- email is unique and not null
-- name is optional string
-- country is ENUM with US, CO, TN (defaults to US, cannot be null)
-- Script shouldn't fail if table exists
CREATE TABLE IF NOT EXISTS users (
    id INT AUTO_INCREMENT PRIMARY KEY,
    email VARCHAR(255) NOT NULL UNIQUE,
    name VARCHAR(255),
    country ENUM('US', 'CO', 'TN') NOT NULL DEFAULT 'US'
);
