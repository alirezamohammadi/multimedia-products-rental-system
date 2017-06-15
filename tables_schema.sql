CREATE TABLE 'user'(
    'username'      VARCHAR(50),
    'password'      VARCHAR(50) NOT NULL,
    'fullname'      VARCHAR(50) NOT NULL,
    PRIMARY KEY     ('username')
);

CREATE TABLE 'customer'(
    'id'        INTEGER         PRIMARY KEY AUTOINCREMENT,
    'name'      VARCHAR(50)     NOT NULL,
    'address'   VARCHAR(200)    NOT NULL,
    'phonenum'  VARCHAR(50)     NOT NULL
);

UPDATE sqlite_sequence SET seq = 10000 WHERE name = 'customer';

CREATE TABLE 'settings'(
    'rentperiod'    INTEGER,
    'rentamount'    INTEGER,
    'penaltyperiod' INTEGER,
    'penaltyamount' INTEGER
);

INSERT INTO 'settings' VALUES(0,0,0,0);

CREATE TRIGGER config_no_insert
BEFORE INSERT ON 'settings'
WHEN (SELECT COUNT(*) FROM 'settings') >= 1
BEGIN
    SELECT RAISE(FAIL, 'only one row!');
END;