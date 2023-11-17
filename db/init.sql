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
    emotion VARCHAR(20) UNIQUE NOT NULL
);

CREATE INDEX idx_date ON "emotion" (date);
CREATE INDEX idx_user_id ON "emotion" (user_id);
