--DROP TABLE IF EXISTS users;

CREATE TABLE IF NOT EXISTS users (
    name TEXT,
    age INTEGER
);

INSERT INTO users
VALUES
    ('Bob', 15),
    ('Tom', 57),
    ('Ken', 73)
;
