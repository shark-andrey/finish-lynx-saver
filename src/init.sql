create table if not exists TABLE_NAME (
    event_number int not null,
    round_number int not null,
    heat_number int not null,
    place int,
    athlete_id int not null,
    lane int,
    time varchar(255),
    react_time varchar(255),
    wind varchar(255),
    photo_file_name varchar(255),
    primary key (event_number, round_number, heat_number, athlete_id)
);

