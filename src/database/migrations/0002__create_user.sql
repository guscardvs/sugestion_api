CREATE TABLE `user`(
    id VARCHAR(36) PRIMARY KEY,
    email VARCHAR(255) UNIQUE NOT NULL,
    first_name VARCHAR(100),
    last_name VARCHAR(100),
    `password` VARCHAR(255) NOT NULL,
    created_at DATETIME NOT NULL,
    last_login DATETIME
)