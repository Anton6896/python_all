use Northwind;

/*
    using MSSQL
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
order by 1 desc;
-- desc order for first column


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

-- 9
select cast(EmployeeID as varchar) + ' ' + LastName as entry
from Employees;

-- 10
select upper(LastName) as Lname, format(BirthDate, 'dd/MM/yy') as date
from Employees
where substring(LastName, 1, 1) in ('K', 'D');


-- 11
select cast(ProductID as varchar) + ' and ' + cast(SupplierID as varchar) as product,
       FLOOR(UnitPrice * 1.165)                                           as fullPrice
from Products
where FLOOR(UnitPrice * 1.165) > 40;

-- 12
select cast(len(FirstName) as varchar) + ' ' + FirstName as Fname,
       cast(len(LastName) as varchar) + ' ' + LastName   as Fname
from Employees;

-- 15
select *
from Employees;

select LastName + ' ' + cast(BirthDate as varchar)      as name,
       convert(varchar, HireDate, 104)                  as hired,
       isnull(cast(ReportsTo as varchar), 'no manager') as manager
from Employees;


-- join ======================================================================================

-- 1
select *
from Products
         join Categories
              on Products.CategoryID = Categories.CategoryID;

-- 2
select ProductName, CompanyName
from Products p
         join Suppliers S on p.SupplierID = S.SupplierID;

-- 3
select OrderID, CompanyName
from Orders o
         join Customers C on o.CustomerID = C.CustomerID
where CompanyName like 'a%';

-- 4
select r.RegionDescription, t.TerritoryDescription
from Region r
         join Territories t on r.RegionID = t.RegionID;

-- 5
select top 5 p.ProductName, p.UnitPrice, c.CategoryName
from Products p
         join Categories c on p.CategoryID = c.CategoryID
where p.UnitPrice > 50;

-- 6
select *
from Products p
         inner join Categories C on p.CategoryID = C.CategoryID
where ProductID = 3;

-- 7
select SupplierID, sum(UnitPrice) as totProfit
from Products p
         join Categories C on p.CategoryID = C.CategoryID
group by SupplierID
order by totProfit desc;

-- 8
select Orders.OrderID,
       Orders.CustomerID,
       ProductID,
       UnitPrice,
       Quantity,
       Discount,
       (UnitPrice * Quantity) - Discount as totPrice
from Orders
         join [Order Details] on Orders.OrderID = [Order Details].OrderID
where Orders.OrderID between 10250 and 10260
order by totPrice desc;

-- 9
select od.OrderID, od.Quantity, ProductName
from [Order Details] od
         join Products P on od.ProductID = P.ProductID
where Quantity > 50;

-- 10
select OrderID, ShipperID, CompanyName
from Orders o
         join Shippers S on o.ShipVia = S.ShipperID
where CompanyName like '[S,U]%'

-- 11
select *
from Orders o
         join Employees E on o.EmployeeID = E.EmployeeID
where City in ('London', 'Redmond')
order by OrderID;

-- 12
select *
from Orders o
         join Shippers S on o.ShipVia = S.ShipperID
where ShipRegion is not null
  and datepart(year, ShippedDate) = 1997;


-- order is os null means that they newer ordered
-- to customers add orders and show orders that have null (left join will add null if not exists)
select *
from Customers c
         left join Orders o on c.CustomerID = o.CustomerID
where OrderID is null;


-- 14  -- order on same address as costumes
select o.OrderID, o.ShipAddress, c.Address
from Orders o
         join Customers C on o.CustomerID = C.CustomerID
where o.ShipAddress = C.Address;

-- 16
select OrderID, CompanyName
from Customers c
         left join Orders o on c.CustomerID = o.CustomerID;


-- group by =====================================================================================

select LastName -- smallest name that employee have (by amount of chars)
from (
         select top 1 len(LastName) as leng, LastName
         from Employees
         order by leng
     ) as tmp;


-- 6
select max(UnitPrice) as maxPrice, avg(UnitPrice) as avePrice
from Products;


--7
select convert(varchar, min(BirthDate), 113) as min,
       convert(varchar, max(BirthDate), 113) as max
from Employees;

-- 9
select count(distinct CustomerID) as idAmount
from Orders;

-- 10
select CategoryID, max(UnitPrice) as maxPrice, min(UnitPrice) as minPrice, avg(UnitPrice) as avgPrice
from Products
group by CategoryID;

-- 11
select SupplierID, max(UnitPrice) as maxPrice
from Products
group by SupplierID
order by maxPrice desc;


-- 16
select max(UnitPrice)   maxPrice,
       min(UnitPrice)   minPrice,
       avg(UnitPrice)   avgPrice,
       count(ProductID) prodAmount
from Products
group by CategoryID, SupplierID;

-- 17
select max(UnitPrice) as maxPrice, CategoryID
from Products
group by CategoryID
having max(UnitPrice) > 40;

-- 18
select avg(UnitPrice) avgPrice
from Products
group by SupplierID
having avg(UnitPrice) > 40;


-- 19
select sum(UnitsOnOrder) uio, sum(UnitsInStock) uis, Categories.CategoryID, Categories.CategoryName
from Products
         join Categories on Products.CategoryID = Categories.CategoryID
where CategoryName like '%C%' -- reg check
group by Categories.CategoryID, Categories.CategoryName
having sum(Products.UnitsOnOrder) > 100 -- using aggregate with having
order by CategoryName;

-- 20
select City, Region, count(CustomerID) as idSum
from Customers
where City like '%[M,L]%'
  and Region is not null
group by Region, City
having count(CustomerID) = 2
    or count(CustomerID) > 2;

-- 21
select LastName, count(*) as totOrders, max(OrderDate) lastOrder
from Employees E
         join Orders O on E.EmployeeID = O.EmployeeID
group by E.EmployeeID, LastName
having count(*) > 100;


-- subquery ======================================================================================


-- 1
select *
from Products
where UnitPrice < (
    select UnitPrice
    from Products
    where ProductID = 8
);

-- 2
select *
from Products
where UnitPrice > (
    select UnitPrice
    from Products
    where ProductName = 'Tofu'
);

-- 3
select FirstName, HireDate
from Employees
where HireDate > (
    select HireDate
    from Employees
    where EmployeeID = 6
);


-- 4
select ProductID, ProductName, UnitPrice
from Products
where UnitPrice > (
    select avg(UnitPrice) as avgUp
    from Products
);

-- 5
select ProductName, UnitsInStock
from Products
where UnitsInStock < (
    select min(UnitsInStock) as uis
    from Products
    where CategoryID = 5
)
  and UnitsInStock > 0;

-- 6
select *
from Products
where CategoryID = (
    select CategoryID
    from Products
    where ProductName = 'Chai'
)
order by UnitPrice;


-- 7
select *
from Products
where UnitPrice in (
    select UnitPrice
    from Products
    where CategoryID = 5
);

-- 8
select OrderID, OrderDate
from Orders
where OrderID in (
    select OrderID
    from Orders
    where ShipCountry in ('France', 'Germany', 'Sweden')
      and datepart(year, OrderDate) = 1997
);

-- 9
select *
from Products
where UnitPrice > (
    select avg(UnitPrice) up
    from Products
    where UnitsInStock > 50
);

-- 10  -- what is productive way ?
select *
from Products p
         join Categories c on p.CategoryID = c.CategoryID
         join Suppliers S on p.SupplierID = S.SupplierID
where c.CategoryName in ('Beverages', 'Condiments')
  and Region is null;

select *
from Products
where CategoryID in (
    select CategoryID
    from Categories
    where CategoryName in ('Beverages', 'Condiments')
)
  and SupplierID in (
    select Suppliers.SupplierID
    from Suppliers
    where Region is null
);


-- 11
select distinct CompanyName
from Products p
         join Categories C on p.CategoryID = C.CategoryID
         join Suppliers S on p.SupplierID = S.SupplierID
where CategoryName = 'Beverages';


select CompanyName -- without distinct so its faster !
from Suppliers
where SupplierID in (
    select Products.SupplierID
    from Products
    where CategoryID in (
        select Categories.CategoryID
        from Categories
        where CategoryName = 'Beverages'
    )
);

-- DML ================================================================================================
Begin transaction

CREATE TABLE my_employees
(
    id     INt PRIMARY KEY,
    name   VARCHAR(50),
    title  VARCHAR(50),
    deptid INT,
    salary MONEY DEFAULT 3500
);

select *
from my_employees;

insert into my_employees
values (2, 'miriam', 'manager', 20, 3750),
       (3, 'aion', 'oper manager ', 30, null),
       (4, 'baruh', null, 30, 3500),
       (5, 'danny', 'sales', 30, 7000);


update my_employees
set salary=4500
where id = 2;

update my_employees
set name='new4name'
where id = 4;

update my_employees
set deptid=10
where deptid = 30;

delete my_employees
where name = 'aion';


insert into my_employees (id, name, title)
select EmployeeID, FirstName, title
from Employees
where EmployeeID > 5;

Commit




