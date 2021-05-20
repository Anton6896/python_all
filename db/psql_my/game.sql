create table vgs
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

