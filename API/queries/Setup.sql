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
    farming NUMERIC, 
    farming_max NUMERIC,
    mining NUMERIC, 
    mining_max NUMERIC, 
    combat NUMERIC, 
    combat_max NUMERIC, 
    foraging NUMERIC, 
    foraging_max NUMERIC, 
    fishing NUMERIC, 
    fishing_max NUMERIC, 
    enchanting NUMERIC, 
    enchanting_max NUMERIC, 
    alchemy NUMERIC, 
    alchemy_max NUMERIC, 
    taming NUMERIC, 
    taming_max NUMERIC, 
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
