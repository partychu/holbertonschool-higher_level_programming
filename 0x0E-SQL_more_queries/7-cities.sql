-- creates database and table
-- cities id INT, uniq, auto-gen, not null, PK, state_id INT, not null, FK, ref id of state, name not null
CREATE DATABASE IF NOT EXISTS hbtn_0d_usa;
USE hbtn_0d_usa;
CREATE TABLE IF NOT EXISTS cities (
	id INT NOT NULL UNIQUE AUTO_INCREMENT,
	PRIMARY KEY (id),
	state_id INT NOT NULL,
	FOREIGN KEY (state_id) REFERENCES states(id),
	name VARCHAR(256) NOT NULL);
