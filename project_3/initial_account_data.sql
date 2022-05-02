# create database

create database mini_chat;

# switch database
use mini_chat



# create user table
CREATE TABLE users (
 user_id INT(11) NOT NULL AUTO_INCREMENT,
 user_name VARCHAR(30) CHARACTER SET utf8 NOT NULL,
 user_password VARCHAR(30) CHARACTER SET utf8 NOT NULL,
 user_nickname VARCHAR(20) CHARACTER SET utf8 NOT NULL,
 PRIMARY KEY(user_id)
) ENGINE=InnoDB AUTO_INCREMENT=5 DEFAULT CHARSET=latin1;




# add two account
insert into users values(0,'user1','123456','CMPE-148 Tester1');
insert into users values(0,'user2','123456','CMPE-148 Tester2');
insert into users values(0,'user3','123456','CMPE-148 Tester3');
select * from users;


#delete database
#drop database mini_chat;