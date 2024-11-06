CREATE TABLE IF NOT EXISTS produto(
    code INT(4) UNSIGNED ZEROFILL NOT NULL,
    name CHAR(50),
    stock NOT NULL,
    value INT FLOAT,
    PRIMARY KEY('code')
);

