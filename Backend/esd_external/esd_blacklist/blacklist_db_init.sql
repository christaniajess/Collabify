DROP DATABASE IF EXISTS blacklist;

CREATE DATABASE blacklist;

USE blacklist;

CREATE TABLE blacklist (
    account VARCHAR(100),
    banned_account VARCHAR(100),
    date TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    PRIMARY KEY (account, banned_account)
);