-- init DB: create required databases
CREATE DATABASE IF NOT EXISTS `study` DEFAULT CHARACTER SET utf8mb4 COLLATE utf8mb4_general_ci;
CREATE DATABASE IF NOT EXISTS `sample` DEFAULT CHARACTER SET utf8mb4 COLLATE utf8mb4_general_ci;

-- (optional) create a couple of sample tables inside `study` for demo
USE `study`;
CREATE TABLE IF NOT EXISTS `students` (
  `id` INT AUTO_INCREMENT PRIMARY KEY,
  `name` VARCHAR(100),
  `university` VARCHAR(100)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

CREATE TABLE IF NOT EXISTS `universities` (
  `id` INT AUTO_INCREMENT PRIMARY KEY,
  `name` VARCHAR(150),
  `city` VARCHAR(100)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

-- sample data for study
INSERT INTO `students` (`name`,`university`) VALUES
('Иван Иванов','ГУ'),
('Пётр Петров','Университет №1');

INSERT INTO `universities` (`name`,`city`) VALUES
('ГУ','Москва'),
('Университет №1','Санкт-Петербург');

-- create sample DB but leave notebook table to be created by ex1.php
USE `sample`;

