CREATE TABLE IF NOT EXISTS pc_case (
    id INTEGER,
    model TEXT,
    mat TEXT,
    color TEXT,
    weight TEXT,
    dimension TEXT,
    io TEXT,
    warranty INTEGER,
    active INTEGER,
    brand_name TEXT,
    full_name TEXT,
    price INTEGER,
    thumbnail_url TEXT
);
INSERT INTO pc_case VALUES (1,'Carbide SPEC-03 Red LED','Plastic, Steel','Black','5.0 kg','215 x 493 x 426','(x2) USB 3.0  (x1) Headphone Port  (x1) Microphone Port',NULL,1,'CORSAIR','CORSAIR Carbide SPEC-03 Red LED',1050,'img/case_1.png'),
	(2,'909 Full Tower (Black)','Aluminum Tempered Glass','Black','17 kg','231 x 575 x 540','USB 3.1 (TYPE-C, 19-pin Connector) x 1 USB 3.0 x 3  HD Audio',NULL,1,'IN WIN','IN WIN 909 Full Tower (Black)',11190,'img/case_2.png'),
	(3,'MasterBox MB500','Plastic, Steel','Black','-','211 x 494 x 475','USB 3.0 x 2 Audio In / Out',NULL,1,'COOLER MASTER','COOLER MASTER MasterBox MB500',2590,'img/case_3.png'),
	(4,'MasterBox E300L Black-Red','Plastic, Steel','Black','-','180 x 448 x 364','USB 3.0 x 2, Audio In / Out',NULL,1,'COOLER MASTER','COOLER MASTER MasterBox E300L Black-Red',1390,'img/case_4.png'),
	(5,'MasterBox E300L Black-Sliver','Plastic, Steel','Black','-','180 x 448 x 364','USB 3.0 x 2, Audio In / Out',NULL,1,'COOLER MASTER','COOLER MASTER MasterBox E300L Black-Sliver',1290,'img/case_5.png');
