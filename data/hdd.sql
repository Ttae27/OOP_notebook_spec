CREATE TABLE IF NOT EXISTS hdd (
    id INTEGER,
    model TEXT,
    form_factor NUMERIC,
    capacity TEXT,
    interface TEXT,
    rpm INTEGER,
    buffer TEXT,
    warranty INTEGER,
    brand_name TEXT,
    full_name TEXT,
    price INTEGER,
    thumbnail_url TEXT
);
INSERT INTO hdd VALUES (16,'Blue 1TB WD10EZEX',3.5,'1TB','SATA 6Gb/s',7200,'64MB',3,'Western Digital','Western Digital Blue 1TB WD10EZEX',1020,'img/hdd_16.png'),
	(17,'Black 1TB WD1003FZEX',3.5,'1TB','SATA 6Gb/s',7200,'64MB',5,'Western Digital','Western Digital Black 1TB WD1003FZEX',3205,'img/hdd_17.png'),
	(18,'BARRACUDA 2TB',3.5,'2TB','SATA 6Gb/s',7200,'64MB',3,'SEAGATE','SEAGATE BARRACUDA 2TB',1840,'img/hdd_18.png'),
	(19,'Black 2TB WD2003FZEX',3.5,'2TB','SATA 6Gb/s',7200,'64MB',5,'Western Digital','Western Digital Black 2TB WD2003FZEX',4880,'img/hdd_19.png'),
	(20,'Purple 3TB 30PURX',3.5,'3TB','SATA 6Gb/s',7200,'64MB',3,'Western Digital','Western Digital Purple 3TB 30PURX',3030,'img/hdd_20.png');
