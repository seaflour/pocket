PRAGMA foreign_keys = ON;

DROP TABLE IF EXISTS mon;
DROP TABLE IF EXISTS monType;

CREATE TABLE mon (
	id         INTEGER PRIMARY KEY AUTOINCREMENT,
	createTime TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP,
	updateTime TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP,
	dex        INTEGER NOT NULL,
	monName    TEXT NOT NULL,
	prime      INTEGER REFERENCES monType(id),
	second     INTEGER REFERENCES monType(id),
	evolves    INTEGER REFERENCES mon(id)
);

CREATE TABLE monType (
	id       INTEGER PRIMARY KEY,
	typeName TEXT NOT NULL
);

/*
INSERT INTO monType(name, id) VALUES ('NORMAL', 1)
INSERT INTO monType(name, id) VALUES ('FIRE', 2)
INSERT INTO monType(name, id) VALUES ('WATER', 3)
INSERT INTO monType(name, id) VALUES ('GRASS', 4)
INSERT INTO monType(name, id) VALUES ('ELECTRIC', 5)
INSERT INTO monType(name, id) VALUES ('ICE', 6)
INSERT INTO monType(name, id) VALUES ('FIGHTING', 7)
INSERT INTO monType(name, id) VALUES ('POISON', 8)
INSERT INTO monType(name, id) VALUES ('GROUND', 9)
INSERT INTO monType(name, id) VALUES ('FLYING', 10)
INSERT INTO monType(name, id) VALUES ('PSYCHIC', 11)
INSERT INTO monType(name, id) VALUES ('BUG', 12)
INSERT INTO monType(name, id) VALUES ('ROCK', 13)
INSERT INTO monType(name, id) VALUES ('GHOST', 14)
INSERT INTO monType(name, id) VALUES ('DRAGON', 15)
*/
