-- create database bank;
USE bank;

-- CREATE TABLE category(
--     name VARCHAR(20) NOT NULL PRIMARY KEY
-- );
-- CREATE TABLE transactions(
--     id INT NOT NULL AUTO_INCREMENT PRIMARY KEY,
--     user_id INT NOT NULL,
--     vendor VARCHAR(50),
--     amount FLOAT NOT NULL,
--     category_name VARCHAR(20),
--     is_deleted BIT DEFAULT false,
--     FOREIGN KEY(category_name) REFERENCES category(name),
--     FOREIGN KEY(user_id) REFERENCES user(id)
-- );

-- CREATE TABLE USER(
--     id INT NOT NULL AUTO_INCREMENT PRIMARY KEY,
--     first_name VARCHAR(20),
--     last_name VARCHAR(20),
--     current_balance FLOAT
-- );

-- drop TABLE transactions;



-- delete  from transactions where id=13;
-- Select * from transactions where is_deleted=1;
-- Select * from category;
-- delete  from category where name='food';
-- INSERT into category( name) values('Fun');
-- INSERT into category( name) values('Education');
-- INSERT into category( name) values('Travel');
-- INSERT into category( name) values('Insurance');



-- delete from transactions where id=3;
-- insert into transactions(id,user_id, vendor, amount, category_name, is_deleted) values(null,1, 'trainer', 100, 'Gym', 0);
-- Select * from transactions where is_deleted=1;

-- update transactions set is_deleted=0 where id=4; 
-- Select * from transactions where category_name='Fun'; 
-- select * from transactions where is_deleted=false;

-- Select current_balance from user;

-- insert into user(id, first_name, last_name, current_balance) values(null, "Avi", "Eyal", 100);
-- select * from user; 

-- update user set current_balance=current_balance+50;
-- select * from user; 

-- select SUM(amount), category_name from transactions where is_deleted='false' group by category_name ;
-- Select current_balance from user where id=1;
-- select SUM(amount) as amount, category_name from transactions where is_deleted='false' group by category_name;

-- Select * from transactions where category_name ='Tax' and is_deleted='false' and user_id=1;
-- select * from transactions where id=18 and is_deleted='false' and user_id=1;

select * from transactions;

-- update transactions set vendor = 'Amazon', amount = 200, category_name = 'Fun' where id = 29;
-- select * from transactions;

-- update transactions set vendor = 'Amazon', amount = 100, category_name = 'Fun' where id = 29;