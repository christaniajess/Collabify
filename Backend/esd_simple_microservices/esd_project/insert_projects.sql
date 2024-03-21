-- -- Database: Project

-- Database: Project
SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
SET AUTOCOMMIT = 0;
START TRANSACTION;
SET time_zone = "+00:00";

CREATE DATABASE IF NOT EXISTS `project` DEFAULT CHARACTER SET utf8 COLLATE utf8_general_ci;
USE `project`;

-- Drop the table if it exists
DROP TABLE IF EXISTS `project`;

-- Creating the table structure
CREATE TABLE IF NOT EXISTS `project`(
    `proj_id` INT(10) UNSIGNED NOT NULL AUTO_INCREMENT PRIMARY KEY,
    `user_id` INT(10) UNSIGNED NOT NULL, 
    `proj_name` TEXT NOT NULL,
    `proj_image` TEXT NOT NULL,
    `proj_description` TEXT NOT NULL
) ENGINE = InnoDB DEFAULT CHARSET = utf8;

-- Insert data into the table
INSERT INTO `project` (`user_id`, `proj_name`, `proj_image`, `proj_description`) VALUES
(1234567890, '66 Days | Change Your Life - Gymshark', 'https://central.gymshark.com/article/66-days-change-your-life',
'They say it takes 66 days to form a habit. We believe it takes 66 days to change your life. This is a collaboration with Gymshark where whether you want to lose weight, become president, or simply drink more water, we want you to do something you feel will change your life for the better'),
(1234567890, 'Move to Zero', 'https://www.nike.com/sustainability','Move to Zero is a project with Nike that helps Nike’s journey towards zero carbon and zero waste, helping to protect the future of sport');

COMMIT; 
