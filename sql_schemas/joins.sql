# find all managers for branches  (inner join)
select emp_firstname, emp_lastname, emp_salary, branch_name
from employee
         join branch on emp_id = mgr_id;

# left / right join ( define an basis for the joining , other missing data fill to null )
select emp_firstname, emp_lastname, emp_salary, branch_name
from employee
         left join branch on emp_id = mgr_id;

select emp_firstname, emp_lastname, emp_salary, branch_name
from employee
         right join branch on emp_id = mgr_id;


# got name off all employees if they sold at least 30.000
select distinct emp_firstname
from employee
         join works_with on employee.emp_id = works_with.emp_id
where total_sales > 30000
   or total_sales = 30000;

select *
from works_with;

select *
from employee;

select distinct emp_firstname, emp_lastname
from employee
where emp_id in
      (
          select emp_id
          from works_with
          where total_sales > 30000
             or total_sales = 30000
      );

# select all clients who are handled by branch that Michael Scott manager
select *
from client
where branch_id in (
    select branch_id
    from branch
    where mgr_id in
          (
              select emp_id
              from employee
              where emp_firstname = 'Michael'
                and emp_lastname = 'Scott'
          )
#     one branch is enough for this query
    limit 1
);

select client_name
from client
         join branch on branch.branch_id = client.branch_id
         join employee on emp_id = branch.mgr_id
where emp_firstname = 'Michael'
  and emp_lastname = 'Scott';




describe branch;
