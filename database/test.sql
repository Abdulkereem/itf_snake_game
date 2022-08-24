CREATE TABLE "Users" (
	id INTEGER NOT NULL, 
	fullname VARCHAR(255), 
	username VARCHAR(255), 
	email VARCHAR(255), 
	PRIMARY KEY (id), 
	UNIQUE (username), 
	UNIQUE (email)
)