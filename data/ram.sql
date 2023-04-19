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
INSERT INTO ram VALUES (36,NULL,'DDR3 4GB 1333','DDR3','4GB',1333,'9',NULL,NULL,'L/T',1,'BLACKBERRY','BLACKBERRY DDR3 4GB 1333',540,'https://notebookspec.com/storage/pc-ram/ram_78_20160613-004555_bbddr3.jpg'),
	(37,'MAXIMUS','MAXIMUS DDR3 8GB 1600','DDR3','8GB',1600,'9',NULL,NULL,'L/T ',1,'BLACKBERRY','BLACKBERRY MAXIMUS DDR3 8GB 1600',1270,'https://notebookspec.com/storage/pc-ram/ram_241_maximus-ddr3-8gb-1600.jpg'),
	(38,NULL,'DDR3 4GB 1333 16Chip ','DDR3','4GB',1333,'9',NULL,NULL,'L/T',1,'BLACKBERRY','BLACKBERRY DDR3 4GB 1333 16Chip ',550,'https://notebookspec.com/storage/pc-ram/ram_264_16-chip-ddr3-4gb-1333.jpg'),
	(39,'Vengeance LPX','Vengeance LPX DDR4 16GB 2666 (8GBx2) Red','DDR4','16GB (8GBx2)',2666,'16-18-18-35',1.2,NULL,'L/T',2,'CORSAIR','CORSAIR Vengeance LPX DDR4 16GB 2666 (8GBx2) Red',2250,'https://notebookspec.com/storage/pc-ram/ram_345_ddr4-16gb-(8gbx2)-2666-vengeance-lpx-red.jpg'),
	(40,'Vengeance LPX','Vengeance LPX DDR4 16GB 2666 (8GBx2) Black','DDR4','16GB (8GBx2)',2666,'16-18-18-35',1.2,NULL,'L/T',2,'CORSAIR','CORSAIR Vengeance LPX DDR4 16GB 2666 (8GBx2) Black',2250,'https://notebookspec.com/storage/pc-ram/ram_347_corsair-ddr4-16gb-(8gbx2)-2666-vengeance-lpx-black.jpg');
