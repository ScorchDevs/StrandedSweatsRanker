-- CREATE TABLE players (
--     User_ID int,
--     login varchar(100),
--     display_name varchar(100),
--     type varchar(100),
--     broadcaster_type varchar(100),
--     Description varchar(150),
--     profile_image_url varchar(150),
--     offline_image_url varchar(150),
--     view_count varchar(100),
--     email varchar(100),
--     created_at datetime,

--     PRIMARY KEY (User_ID)
-- );


CREATE TABLE weights (
    version int,
    Farming NUMERIC, 
    Mining NUMERIC, 
    Combat NUMERIC, 
    Foraging NUMERIC, 
    Fishing NUMERIC, 
    Enchanting NUMERIC, 
    Alchemy NUMERIC, 
    Taming NUMERIC, 
    zombie NUMERIC, 
    spider NUMERIC, 
    wolf NUMERIC,  
    enderman NUMERIC,  
    minions NUMERIC, 
    collections NUMERIC,

    PRIMARY KEY (version)
);

INSERT INTO weights VALUES (0, 0.000051926, 0.000102955, 0.000076098, 0.000117758, 0.000196823, 0.000031334, 0.000036231, 0.000057971, 0.005, 0.008, 0.01, 0.0125, 17, 800)