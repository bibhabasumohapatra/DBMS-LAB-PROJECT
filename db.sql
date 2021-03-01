create table if not exists cust_detail(
   id int primary key auto_increment,
   cust_name varchar(64) not null,
   car varchar(32),
   part_damaged varchar(32);
   date_of_service varchar(32) not null,
   date_comp varchar(32) not null,
   payment int(10)
);


create table if not exists stock_spare_parts(
   id int primary key auto_increment,
   parts_name varchar(16),
   parts_available int(18),
   price int(18),
   
);