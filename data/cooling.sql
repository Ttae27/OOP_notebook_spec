CREATE TABLE IF NOT EXISTS cooling (
    id INTEGER,
    series TEXT,
    model TEXT,
    type TEXT,
    cpu_support_intel TEXT,
    cpu_support_amd TEXT,
    dimension TEXT,
    material TEXT,
    fan_built_in TEXT,
    led INTEGER,
    warranty INTEGER,
    price INTEGER,
    brand_name TEXT,
    full_name TEXT,
    thumbnail_url TEXT
);
INSERT INTO cooling VALUES (46,'ICE ','ICE EDGE MINI FS','Air Cooler','LGA 1366 / 1156 / 1155 / 1151 / 1150 / 775 ','FM2+ / FM2 / FM1 / AM3+ / AM3 / AM2','127x62x130','2 Heatpipes / Aluminum Fins','1 x 80mm',NULL,1,270,'DEEPCOOL','DEEPCOOL ICE EDGE MINI FS','img/cooling_46.png'),
	(47,'GAMMAXX','GAMMAXX 400','Air Cooler','LGA 2011-v3 / 2011 / 1366 / 1156 / 1155 / 1151 / 1150 / 775','FM2+ / FM2 / FM1 / AM3+ / AM3 / AM2','135x80x155','4 heatpipes / Aluminum fins','1 x 120mm',NULL,1,610,'DEEPCOOL','DEEPCOOL GAMMAXX 400','img/cooling_47.png'),
	(48,'TSS','TSS 1000 RGB','Air Cooler','LGA 1366 / 1156 / 1155 / 1151 / 1150 / 775 ','AM3+ / AM3 / AM2+ / AM2 / FM1','125x125x70','Aluminum, copper, plastic','120mm x 1',NULL,1,265,'Tsunami','Tsunami TSS 1000 RGB','img/cooling_48.png'),
	(49,'MasterAir ','MasterAir MA620M ','Air Cooler','LGA2066 / 2011-v3 / 2011 / 1366 / 1156 / 1155 / 1151 / 1150','AM4 / AM3+ / AM3 / AM2+ / FM2+ / FM2 / FM1','125x135x165','6 Heatpipes / Aluminum Fins','120mm x 2',NULL,5,2560,'COOLER MASTER','COOLER MASTER MasterAir MA620M ','img/cooling_49.png'),
	(50,'UX','UX200 ARGB','Air Cooler','LGA 1200 / 1156 / 1155 / 1151 / 1150 / 775','AM4 / AM3+ / AM3 / AM2+ / FM2+ / FM2 / FM1','76x120x153','2 Heat Pipes/Aluminum Fins/Copper Plate','120mm x 1',NULL,2,990,'COOLER MASTER','COOLER MASTER UX200 ARGB','img/cooling_50.png');
