CREATE USER 'suzukiti'@'%' IDENTIFIED WITH mysql_native_password BY '256133'; -- #TODO セキュリティ
CREATE DATABASE IF NOT EXISTS dev_amtapp;
GRANT ALL on dev_amtapp.* to 'suzukiti'@'%';
FLUSH PRIVILEGES;
