USE data_analysis;
CREATE TABLE
IF
	NOT EXISTS `secretary_info` (
		`info_id` INT UNSIGNED,
		`province_code` CHAR ( 10 ),
		`province_name` CHAR ( 30 ),
		`city_code` CHAR ( 10 ),
		`city_name` CHAR ( 30 ),
		`on_year` YEAR,
		`secretary_name` CHAR ( 30 ),
		`birth_year` CHAR ( 10 ),
		`birth_month` CHAR ( 10 ),
		`native_province_code` CHAR ( 10 ),
		`native_province_name` CHAR ( 30 ),
		`native_city_code` CHAR ( 10 ),
		`native_city_name` CHAR ( 30 ),
		`sex` CHAR ( 5 ),
		`nation` CHAR ( 30 ),
		`education` CHAR ( 20 ),
		`is_party_school` CHAR ( 5 ),
		`speciality_humanities` CHAR ( 5 ),
		`speciality_social` CHAR ( 5 ),
		`speciality_technology` CHAR ( 5 ),
		`speciality_agriculture` CHAR ( 5 ),
		`speciality_medical` CHAR ( 5 ),
		`in_party_year` YEAR,
		`work_years` TINYINT UNSIGNED,
		PRIMARY KEY ( `info_id` ) 
	) ENGINE = INNODB DEFAULT CHARSET = utf8;
	
INSERT INTO secretary_info (
	info_id,province_code,province_name,city_code,city_name,on_year,secretary_name,birth_year,
	birth_month,native_province_code,native_province_name,native_city_code,native_city_name,
	sex,nation,education,is_party_school,speciality_humanities,speciality_social,speciality_technology,
	speciality_agriculture,speciality_medical,in_party_year,work_years 
)
VALUES
	(1, "130000", "河北省", "130100", "石家庄市", "2000", "陈来立", "", "", "", "", "", "", "", "", "硕士", "1", "1", "0", "0", "0", "0", "2000", "2");
	

show databases;