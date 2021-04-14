select emp_firstname as All_Names
from employee
union
select branch_name
from branch;

# what is company profit  -270500
select sum(total_sales) as in_and_out
from works_with
union
select sum(emp_salary) as b
from employee;

select (sum(total_sales) - sum(emp_salary)) as total
from employee, works_with;

