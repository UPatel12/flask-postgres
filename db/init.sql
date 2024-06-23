CREATE TABLE messages (
    id SERIAL PRIMARY KEY,
    content TEXT NOT NULL
);
INSERT INTO messages (content) VALUES ('hello world');
INSERT INTO messages (content) VALUES ('hello everyone');
INSERT INTO messages (content) VALUES ('hello all');