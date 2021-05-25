create table if not exists vgs
(
    id           serial,
    name         text,
    platform     text,
    year         int,
    genre        text,
    publisher    text,
    na_sales     numeric,
    eu_sales     numeric,
    jp_sales     numeric,
    other_sales  numeric,
    global_sales numeric,
    critic_score numeric,
    critic_count int,
    user_score   numeric,
    user_count   int,
    developer    text,
    rating       text
);

select *
from vgs;

copy vgs (name, platform, year, genre, publisher, na_sales, eu_sales,
          jp_sales, other_sales, global_sales, critic_score,
          critic_count, user_score, user_count, developer, rating)
    -- https://www.kaggle.com/sidtwr/videogames-sales-dataset
    -- after i got data i changed at exel cells that have no data or bad data
    FROM 'D:\Downloads\archive\Video_Games_Sales_as_at_22_Dec_2016.csv'
    WITH (FORMAT CSV, NULL 'NULL', HEADER);


select sum(global_sales) glob_sale, genre
from vgs
group by genre;


-- platform appearance that have at least 100 titles/names
select platform, sum(global_sales) sum
from vgs
group by platform
having count(*) > 100
order by sum desc
limit 10;


create index platform_index on vgs (platform);
drop index platform_index;

select count(*)
from vgs
where platform = 'GB';

-- D:\Downloads\annual.csv
create table if not exists annual
(
    year            int,
    ind_aggregation text,
    ind_code        text,
    ind_name        text,
    units           text,
    var_code        text,
    var_name        text,
    var_category    text,
    value_dat       text,
    ind_code_ANZ    text
);

copy annual (year, ind_aggregation, ind_code, ind_name, units, var_code, var_name, var_category, value_dat,
             ind_code_ANZ)
    from 'D:\Downloads\annual.csv'
    with (format csv, header );

create index unitsindex on annual (units);

select distinct units, ind_code, count(*) as sum
from annual
group by units, ind_code
having count(*) > 40
order by ind_code;

select * from  annual;