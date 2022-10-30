CREATE DATABASE IF NOT EXISTS workoutbuddy;
USE workoutbuddy;

CREATE TABLE IF NOT EXISTS user_login
	(
		user_id INTEGER NOT NULL AUTO_INCREMENT,
		name VARCHAR(255) NOT NULL,
        email VARCHAR(255) NOT NULL,
		hashed_password BLOB NOT NULL,
        date_birth DATE NOT NULL,

        PRIMARY KEY (user_id),
        CHECK (LENGTH(hashed_password) >8)
	);

CREATE TABLE IF NOT EXISTS user_data
	(
		user_id INTEGER NOT NULL,
		display_name VARCHAR(30) NOT NULL,
		about VARCHAR(255),
		is_validated BOOLEAN DEFAULT FALSE,
		location VARCHAR(80),

        PRIMARY KEY (user_id),
        FOREIGN KEY(user_id) REFERENCES user_login(user_id)
    );

CREATE TABLE IF NOT EXISTS matched_users
    (
        current_user_id INTEGER NOT NULL,
        matched_user_id INTEGER NOT NULL,

        PRIMARY KEY (current_user_id, matched_user_id),
        FOREIGN KEY (current_user_id) REFERENCES user_data(user_id),
        FOREIGN KEY (current_user_id) REFERENCES user_data(user_id),
        CHECK (current_user_id != matched_user_id)
    );

DELIMITER $$
CREATE TRIGGER insert_into_user_data
	AFTER INSERT ON user_login
	FOR EACH ROW
BEGIN
	INSERT INTO user_data
    (user_id, display_name)
    VALUES
    (NEW.user_id,
     NEW.name);

END $$
DELIMITER ;
