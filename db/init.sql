CREATE TABLE "user" (
    id SERIAL PRIMARY KEY,
    username VARCHAR(20) UNIQUE NOT NULL,
    password TEXT NOT NULL
);

CREATE INDEX idx_username ON "user" (username);

CREATE TABLE "emotion" (
    id SERIAL PRIMARY KEY,
    user_id INTEGER REFERENCES "user" (id),
    date DATE NOT NULL,
    emotion VARCHAR(20) NOT NULL
);
