-- phpMyAdmin SQL Dump
-- version 4.7.4
-- https://www.phpmyadmin.net/
--
-- Host: 127.0.0.1:3306
-- Generation Time: Jun 12, 2020 at 02:17 AM
-- Server version: 5.7.19
-- PHP Version: 7.1.9

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
SET AUTOCOMMIT = 0;
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Database: `collaboration`
--
DROP TABLE IF EXISTS `collaboration`;
CREATE DATABASE IF NOT EXISTS `collaboration` DEFAULT CHARACTER SET utf8 COLLATE utf8_general_ci;
USE `collaboration`;

-- --------------------------------------------------------

--
-- Table structure for table `collaboration`
--


CREATE TABLE IF NOT EXISTS `collaboration` (
  `cc_id` VARCHAR(100),
  `brand_id` VARCHAR(100),
  `collab_title` varchar(20),
  `collab_status` varchar(20),
  PRIMARY KEY (`cc_id`, `brand_id`,`collab_title`)
) ENGINE=InnoDB AUTO_INCREMENT=1 DEFAULT CHARSET=utf8;


--
-- Dumping data for table `collaboration`
--

INSERT INTO `collaboration` (`cc_id`, `brand_id`, `collab_title`, `collab_status`) VALUES
('0101', '0201', 'Nike Collab', 'Pending');


/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
