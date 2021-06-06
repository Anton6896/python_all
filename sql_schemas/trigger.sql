select *
from employee;

# for ech new person add entry that person was added
create table trigger_test
(
    data_test varchar(30)
);


# in mySql must be created in terminal (connect $mysql -u ant1 -p)
delimiter $$ # change delimiter to $$
create
    trigger addon_users
    before insert
    on employee
    for each row
begin
    insert into trigger_test values ('new user added');
end $$
delimiter ; # get ; delimiter back

INSERT INTO employee
VALUES(1010, 'newName', 'newLastName', '1971-06-25', 'F', 63000, 102, 1);


select * from trigger_test;

INSERT INTO employee
VALUES(1020, 'newName1', 'newLastName1', '1971-06-25', 'F', 63000, 102, 1);
