CREATE TABLE "user" (
    id SERIAL PRIMARY KEY,
    username VARCHAR(20) UNIQUE NOT NULL,
    password TEXT NOT NULL
);

CREATE INDEX idx_username ON "user" (username);