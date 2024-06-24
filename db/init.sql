CREATE TABLE messages (
    id SERIAL PRIMARY KEY,
    content TEXT NOT NULL
);
INSERT INTO messages (content) VALUES ('hello world');
INSERT INTO messages (content) VALUES ('hi world');
INSERT INTO messages (content) VALUES ('sup world');
INSERT INTO messages (content) VALUES ('bye world');