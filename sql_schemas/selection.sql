select *
from employee
limit 5;

select distinct emp_sex
from employee;

select count(emp_id) as amount_of_employee
from employee;

# expect 2 persons
select count(emp_id) as amount_of_employee
from employee
where super_id IS NOT NULL
  and emp_sex = 'F'
  and emp_birthdate > '1970-01-01';

select avg(emp_salary) as average_salary
from employee;

select count(emp_sex) as amount, emp_sex
from employee
group by emp_sex;

select *
from employee;

select count(total_sales), sum(total_sales) as amount, emp_id
from works_with
group by emp_id;

# total sale for ech salesman
select count(total_sales), ww.emp_id, emp_firstname, sum(total_sales)
from employee
         join works_with ww on employee.emp_id = ww.emp_id
group by ww.emp_id;

# how many client is spend
select client_id, sum(total_sales) as client_spend
from works_with
group by client_id;


# wild card for looking (some regex) -> find client with LLC
# % -- any number of chars, _ -- one char
select *
from client
where client_name like '%LLC';
SELECT *
FROM branch_supplier
WHERE supplier_name like '%lables'
   or supplier_name like '%labels';

# emp that born in February
select *
from employee
where emp_birthdate like '____-02%';


