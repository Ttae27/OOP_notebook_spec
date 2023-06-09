CREATE TABLE IF NOT EXISTS psu (
    id INTEGER,
    series TEXT,
    model TEXT,
    form_factor TEXT,
    max_pw TEXT,
    modular TEXT,
    fans TEXT,
    certificates TEXT,
    efficiency TEXT,
    input_volt TEXT,
    input_frequency TEXT,
    dimension TEXT,
    main_connect TEXT,
    pci_ex TEXT,
    sata_connect INTEGER,
    molex TEXT,
    warranty INTEGER,
    brand_name TEXT,
    full_name TEXT,
    price INTEGER,
    thumbnail_url TEXT
);
INSERT INTO psu VALUES (31,'TR2 S','TR2 S 550W','ATX','550W','N/A','1 x 120mm Fan','80 PLUS','82-86% efficiency','230 V','50-60Hz','150 mm x 140 mm x 86 mm','20+4-Pin','2 x 6+2-Pin',5,'-',3,'THERMALTAKE','THERMALTAKE TR2 S 550W',1505,'img/psu_31.png'),
	(32,'TR2 S','TR2 S 650W','ATX','650W','N/A','1 x 120mm Fan','80 PLUS','82-86% efficiency','230 V','47/63 Hz','150mm x 140mm x 86mm','20+4 Pin','2 x 6+2-Pin',5,'-',3,'THERMALTAKE','THERMALTAKE TR2 S 650W',1890,'img/psu_32.png'),
	(33,'HX Series','HX850','ATX','850W','Fully Modular','1 x 135mm Fan','80 PLUS Platinum','MEET 80 Plus PLATINUM at 115Vac input.','100 - 240 V','47/63 Hz','150mm x 180mm x 86mm','20+4 Pin','6 x 6+2-Pin',8,'-',10,'CORSAIR','CORSAIR HX850',4765,'img/psu_33.png'),
	(34,'500W','PW007 500W','ATX','500W','N/A','1 x 120mm Fan','-','78% Efficiency','90 - 264 V','50~60 Hz','150mm x 140mm x 86mm','20+4 Pin','1 x 6+2-Pin',2,'-',3,'DTECH','DTECH PW007 500W',640,'img/psu_34.png'),
	(35,'Gamemaster Pro','Gamemaster Pro 700W','ATX','700W','Fully Modular','1 x 120mm Fan','-','>75%','110 - 230 V','50-60Hz','150mm x 140mm x 86mm','20+4 Pin','1 x 6+2-Pin',3,'-',3,'NEOLUTION','NEOLUTION Gamemaster Pro 700W',700,'img/psu_35.png');
