CREATE TABLE `database_cityhall`.`AdminUser` (
`id` int(11) not null auto_increment,
`email_address` varchar(255) not null,
`name` varchar(255) default null,
`approved` tinyint(1) default 0,
`department_id` int(11) default null,
`sidedish_num` int(11) default null,
`dessert_num` int(11) default null,
`target_calories` int default null,
`meal_price` int default null,
PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

CREATE TABLE `databse_cityhall_dev`.`new_table` (
`idnew_table` INT NOT NULL AUTO_INCREMENT,
`new_tablecol` VARCHAR(45) NULL,
PRIMARY KEY (`idnew_table`),
UNIQUE INDEX `new_tablecol_UNIQUE` (`new_tablecol` ASC));
