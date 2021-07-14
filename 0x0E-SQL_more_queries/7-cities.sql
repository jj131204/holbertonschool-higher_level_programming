-- MYSQL
CREATE DATABASE IF NOT EXISTS hbtn_0d_usa;
CREATE TABLE IF NOT EXISTS hbtn_0d_usa.cities(
	id INT UNIQUE AUTO_INCREMENT NOT NULL,
	state_id INT NOT NULL,
	name VARCHAR(256),
	PRIMARY KEY(id),
	FOREIGN KEY(`state_id`) REFERENCES states(`id`));

--CREATE DATABASE IF NOT EXISTS hbtn_0d_usa;
--CREATE TABLE IF NOT EXISTS hbtn_0d_usa.cities(
--	id INT NOT NULL AUTO_INCREMENT PRIMARY KEY,
--	state_id INT,
--	name VARCHAR(256) NOT NULL,
--       	FOREIGN KEY (state_id) REFERENCES states(id)
--);


