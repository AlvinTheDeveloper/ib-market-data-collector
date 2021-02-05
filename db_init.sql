create table historical_data
(
    source    varchar(100)   not null,
    symbol    varchar(30)    not null,
    frequency varchar(10)    not null,
    time      int            not null,
    open      double(30, 15) null,
    high      double(30, 15) null,
    low       double(30, 15) null,
    close     double(30, 15) null,
    volume    bigint         null,
    adj_close double(30, 15) null,
    primary key (symbol, frequency, time, source)
);

create table ib_request
(
    req_id      int auto_increment
        primary key,
    symbol      varchar(30)   not null,
    action      varchar(40)   not null,
    req_content text          not null,
    status      int default 0 not null
);

create table symbol
(
    symbol   varchar(30) not null,
    name     text        null,
    exchange varchar(15) not null,
    primary key (symbol, exchange)
);


create table watchlist
(
    symbol           varchar(10)       not null,
    instr_type       varchar(10)       not null,
    exchange         varchar(10)       not null,
    priority         tinyint default 0 not null,
    last_update_time int               null,
    primary key (symbol, instr_type, exchange)
);

