-- creates a database and a user
-- select privs pw, if db exists, if user exists
CREATE DATABASE IF NOT EXISTS HBTN_0D_2;
CREATE USER IF NOT EXISTS 'user_0d_2'@'localhost' IDENTIFIED BY 'user_0d_2_pwd';
GRANT SELECT ON hbtn_0d_2.* TO 'user_0d_2'@'localhost';
