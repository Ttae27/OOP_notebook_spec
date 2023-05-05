CREATE TABLE IF NOT EXISTS ram (
    id INTEGER,
    series TEXT,
    model TEXT,
    type TEXT,
    capa TEXT,
    bus INTEGER,
    latency TEXT,
    vol NUMERIC,
    color INTEGER,
    warranty TEXT,
    ram_unit INTEGER,
    brand_name TEXT,
    full_name TEXT,
    price INTEGER,
    thumbnail_url TEXT
);
INSERT INTO ram VALUES (36,NULL,'DDR3 4GB 1333','DDR3','4GB',1333,'9',NULL,NULL,'L/T',1,'BLACKBERRY','BLACKBERRY DDR3 4GB 1333',540,'img/ram_36.png'),
	(37,'MAXIMUS','MAXIMUS DDR3 8GB 1600','DDR3','8GB',1600,'9',NULL,NULL,'L/T ',1,'BLACKBERRY','BLACKBERRY MAXIMUS DDR3 8GB 1600',1270,'img/ram_37.png'),
	(38,NULL,'DDR3 4GB 1333 16Chip ','DDR3','4GB',1333,'9',NULL,NULL,'L/T',1,'BLACKBERRY','BLACKBERRY DDR3 4GB 1333 16Chip ',550,'img/ram_38.png'),
	(39,'Vengeance LPX','Vengeance LPX DDR4 16GB 2666 (8GBx2) Red','DDR4','16GB (8GBx2)',2666,'16-18-18-35',1.2,NULL,'L/T',2,'CORSAIR','CORSAIR Vengeance LPX DDR4 16GB 2666 (8GBx2) Red',2250,'img/ram_39.png'),
	(40,'Vengeance LPX','Vengeance LPX DDR4 16GB 2666 (8GBx2) Black','DDR4','16GB (8GBx2)',2666,'16-18-18-35',1.2,NULL,'L/T',2,'CORSAIR','CORSAIR Vengeance LPX DDR4 16GB 2666 (8GBx2) Black',2250,'img/ram_40.png');
