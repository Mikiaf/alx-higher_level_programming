-- creating table
-- queries database
CREATE TABLE if not exists second_tabl (
    id int not null auto_increment,
    name varchar(256),
    score int
);
--adding data into it
insert into second_table(name,score)
value ("John",10),
    ("Alex",3),
    ("Bob",14),
    ("George",8)