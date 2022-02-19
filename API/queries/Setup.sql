CREATE TABLE players (
    uuid varchar(100),
    username varchar(100),

    PRIMARY KEY (uuid)
);

CREATE TABLE profiles (
    uuid varchar(100),
    profileid varchar(100),

    PRIMARY KEY (uuid, profileid)
);

CREATE TABLE stats (
    uuid varchar(100),
    profileid varchar(100),
    collecttime datetime,
    farming NUMERIC, 
    mining NUMERIC, 
    combat NUMERIC, 
    foraging NUMERIC, 
    fishing NUMERIC, 
    enchanting NUMERIC, 
    alchemy NUMERIC, 
    taming NUMERIC, 
    zombie NUMERIC, 
    spider NUMERIC, 
    wolf NUMERIC,  
    enderman NUMERIC,  
    minions NUMERIC, 
    collections NUMERIC,

    PRIMARY KEY (uuid, profileid, collecttime),
    FOREIGN KEY (uuid, profileid) REFERENCES profiles(uuid, profileid)
);

CREATE TABLE weights (
    version int,
    farming_weight NUMERIC, 
    farming_max NUMERIC,
    mining_weight NUMERIC, 
    mining_max NUMERIC, 
    combat_weight NUMERIC, 
    combat_max NUMERIC, 
    foraging_weight NUMERIC, 
    foraging_max NUMERIC, 
    fishing_weight NUMERIC, 
    fishing_max NUMERIC, 
    enchanting_weight NUMERIC, 
    enchanting_max NUMERIC, 
    alchemy_weight NUMERIC, 
    alchemy_max NUMERIC, 
    taming_weight NUMERIC, 
    taming_max NUMERIC, 
    zombie_weight NUMERIC, 
    zombie_max NUMERIC, 
    spider_weight NUMERIC, 
    spider_max NUMERIC, 
    wolf_weight NUMERIC,  
    wolf_max NUMERIC,  
    enderman_weight NUMERIC,  
    enderman_max NUMERIC,  
    minions_weight NUMERIC, 
    minions_max NUMERIC, 
    collections_weight NUMERIC,
    collections_max NUMERIC,

    PRIMARY KEY (version)
);

CREATE TABLE api_users (
    email varchar(100),
    username varchar(100) UNIQUE,
    password varchar(128),
    is_admin boolean,
    allowed_to_use_api boolean,

    PRIMARY KEY (email)
);

/*
THE FOLLOWING CODE IS TEST-DATA. REMOVE THIS BEFORE PRODUCTION!
*/


INSERT INTO weights VALUES (0, 0.000051926, 100, 0.000102955, 100, 0.000076098, 100, 0.000117758, 100, 0.000196823, 100, 0.000031334, 100, 0.000036231, 100, 0.000057971, 100, 0.005, 100, 0.008, 100, 0.01, 100, 0.0125, 100, 17, 100, 800, 100);

INSERT INTO players VALUES 
('abcdefgh', 'testUser'),
('aaaaaa', 'user2');

INSERT INTO profiles VALUES ('abcdefgh', 'testprofile');
INSERT INTO profiles VALUES ('aaaaaa', 'aprofile');
INSERT INTO profiles VALUES ('aaaaaa', 'aaprofile');
INSERT INTO profiles VALUES ('aaaaaa', 'aaaprofile');
INSERT INTO profiles VALUES ('aaaaaa', 'aaaaprofile');

INSERT INTO stats VALUES ('abcdefgh', 'testprofile', '17-02-2022', 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14);
INSERT INTO stats VALUES ('aaaaaa', 'aprofile', '17-02-2022', 1, 2, 3, 4, 10, 6, 7, 8, 9, 10, 11, 12, 13, 14);
INSERT INTO stats VALUES ('aaaaaa', 'aaprofile', '17-02-2022', 1, 2, 3, 4, 20, 6, 7, 8, 9, 10, 11, 12, 13, 14);
INSERT INTO stats VALUES ('aaaaaa', 'aaaprofile', '17-02-2022', 1, 2, 3, 4, 13, 6, 7, 8, 9, 10, 11, 12, 13, 14);
INSERT INTO stats VALUES ('aaaaaa', 'aaaaprofile', '17-02-2022', 1, 2, 3, 4, 15, 6, 7, 8, 9, 10, 11, 12, 13, 14);
