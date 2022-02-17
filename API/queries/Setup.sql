CREATE TABLE players (
    UUID varchar(100),
    username varchar(100),

    PRIMARY KEY (UUID)
);

CREATE TABLE profiles (
    UUID varchar(100),
    profileID varchar(100),

    PRIMARY KEY (UUID, profileID)
);

CREATE TABLE stats (
    UUID varchar(100),
    profileID varchar(100),
    collectTime datetime,
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

    PRIMARY KEY (UUID, profileID, collectTime),
    FOREIGN KEY (UUID, profileID) REFERENCES profiles(UUID, profileID)
);

CREATE TABLE weights (
    version int,
    Farming NUMERIC, 
    Farming_max NUMERIC,
    Mining NUMERIC, 
    Mining_max NUMERIC, 
    Combat NUMERIC, 
    Combat_max NUMERIC, 
    Foraging NUMERIC, 
    Foraging_max NUMERIC, 
    Fishing NUMERIC, 
    Fishing_max NUMERIC, 
    Enchanting NUMERIC, 
    Enchanting_max NUMERIC, 
    Alchemy NUMERIC, 
    Alchemy_max NUMERIC, 
    Taming NUMERIC, 
    Taming_max NUMERIC, 
    zombie NUMERIC, 
    zombie_max NUMERIC, 
    spider NUMERIC, 
    spider_max NUMERIC, 
    wolf NUMERIC,  
    wolf_max NUMERIC,  
    enderman NUMERIC,  
    enderman_max NUMERIC,  
    minions NUMERIC, 
    minions_max NUMERIC, 
    collections NUMERIC,
    collections_max NUMERIC,

    PRIMARY KEY (version)
);

INSERT INTO weights VALUES (0, 0.000051926, 100, 0.000102955, 100, 0.000076098, 100, 0.000117758, 100, 0.000196823, 100, 0.000031334, 100, 0.000036231, 100, 0.000057971, 100, 0.005, 100, 0.008, 100, 0.01, 100, 0.0125, 100, 17, 100, 800, 100);

INSERT INTO players VALUES 
('abcdefgh', 'testUser'),
('aaaaaaaa', 'user2');

INSERT INTO profiles VALUES ('abcdefgh', 'testProfile');

INSERT INTO stats VALUES ('abcdefgh', 'testProfile', '17-02-2022', 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14);