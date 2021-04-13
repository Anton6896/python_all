select emp_firstname as All_Names
from employee
union
select branch_name
from branch;