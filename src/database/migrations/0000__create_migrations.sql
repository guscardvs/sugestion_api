CREATE TABLE IF NOT EXISTS migrations(
    id SERIAL PRIMARY KEY,
    `filename` TEXT,
    created_at DATETIME
)