use Northwind;

/*
    using MSSQL (bad bad idea, but it is what it is)
    because of half in eng and half in Heb is cant be cp properly
    so will bw only q num

*/


/* SELECT part ============================================================= */
-- 1
select *
from Orders;
select *
from Employees;

-- 2
select Country, Region, HireDate, FirstName
from Employees;

-- 5
select ProductID, ProductName, UnitPrice
from Products;

-- 6
select Address, City, Region
from Employees;

-- 7
select CustomerID, (City + ' , ' + Customers.Address) as full_address
from Customers;

-- 8
select (FirstName + ' ' + LastName) as full_name,
       datepart(day, BirthDate) + 8 as birth_day,
       ReportsTo                    as manager
from Employees;
-- where ReportsTo is not NULL;

-- 9
with tmp as (
    select count(EmployeeID) as tot, City
    from Employees
    group by City
)
select City
from tmp
where tot = 1;

-- 10
with tmp as (
    select count(EmployeeID) as tot, Country
    from Employees
    group by Country
)
select Country
from tmp
where tot = 1;

-- 11
select *
from Employees;


-- 12
select distinct Country, City
from Customers;

-- 13
select FirstName, BirthDate, (BirthDate + 5) as bPlusFive
from Employees;

-- 14
select ProductName, UnitPrice, UnitPrice + 10 as UpPlus10
from Products;
select *
from Products

-- 15
select ProductID,
       ProductName,
       UnitPrice,
       (UnitPrice + (UnitPrice / 100) * 16.5) as '+16.5%',
       UnitsInStock,
       UnitsOnOrder,
       (UnitsInStock - Products.UnitsOnOrder) as 'UinS-UinO'
from Products;

-- 16
with tmp as (
    select ProductID,
           ProductName,
           (UnitsInStock - UnitsOnOrder) * UnitPrice as "UnOrdered Units"
    from Products
)
select *
from tmp
where "UnOrdered Units" > 0;

/* Where   ============================================================= */

-- 3
select ProductID, ProductName, UnitPrice
from Products
where UnitPrice > 20
order by UnitPrice;

-- 4
select (FirstName + ' ' + LastName) as name, BirthDate, ReportsTo as manager
from Employees
where EmployeeID = 8;


-- 6
select *
from Products
where UnitPrice not between 50 and 100;

-- 9
select *
from Employees
where EmployeeID in (2, 5, 1);


-- 12
select FirstName, Region
from Employees
where Region IS NULL;


-- 13
select top 3 ProductName, UnitPrice
from Products
order by UnitPrice desc;

-- 14
select OrderID, OrderDate, RequiredDate
from Orders
where RequiredDate >= '1996-10-1';


-- 16
-- all names that contains 'o'
select *
from Categories
where CategoryName like '%o%';


-- 17
-- last char is 'a' in company name
select *
from Customers
where CompanyName like '%a';

-- 18 'a' one before end -> '%a_'

-- 19
select *
from Orders
where OrderDate between '1997-4-1' and '1997-5-1'
order by OrderDate, OrderID desc;

-- 20
select CustomerID, CompanyName, Country, Phone
from Customers
where Country like 'G%'
   or Country like 'M%'
   or Country like 'F%' and Region is NULL;

-- 21
select *
from Employees
where LastName like '%k%'
   or LastName like '%D%' and datepart(year, BirthDate) >= 1963;


-- 23
select OrderID, EmployeeID, OrderDate, RequiredDate, ShipName
from Orders
where OrderID = 7
  and ShipName in ('QUICK-Stop', 'Du mond entire', 'Eastern Connection')
  and OrderDate + 20 < RequiredDate;

-- 24
select ProductID, ProductName
from Products
where SupplierID in (21, 8, 16)
   or UnitPrice > 10
    and UnitsInStock not between 10 and 100
order by UnitPrice;


select FirstName + ' ' + LastName as name, BirthDate as date
from Employees
order by 1 desc; -- desc order for first column


/* scalar functions  ================================================== */

-- 1
select lower(FirstName) as first, upper(LastName) as last, EmployeeID
from Employees
where EmployeeID between 3 and 5;

-- 2
select substring(FirstName, 1, 3) + ' , ' + substring(LastName, 1, 1) as name
from Employees;

-- 3  (great thing replace chars on query in line (not in db))
INSERT into "Products"
("ProductName", "SupplierID", "CategoryID", "QuantityPerUnit", "UnitPrice",
 "UnitsInStock", "UnitsOnOrder", "ReorderLevel",
 "Discontinued")
VALUES ('some ?', 1, 1, '10 boxes x 20 bags', 18, 39, 0, 10, 0);

select ProductName, ProductID, replace(ProductName, '?', '-') as new_name
from Products;


-- 4
select getdate();

-- 6
select FirstName, datepart(year, getdate()) - datepart(year, BirthDate) as age
from Employees;

-- 7 (get day name and year of emp hire date)
select FirstName, format(HireDate, 'dddd') as day_name, datepart(year, HireDate) as year_hire
from Employees;

-- 8 (round data)
select ProductID, cast(UnitPrice * 0.12 as decimal(10, 0)) as "*0.12"
from Products;

select ProductID, round(UnitPrice * 0.12, 0) as "*0.12"
from Products;



