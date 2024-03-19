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
-- Database: `collaborations`
--
CREATE DATABASE IF NOT EXISTS `collaborations` DEFAULT CHARACTER SET utf8 COLLATE utf8_general_ci;
USE `collaborations`;

-- --------------------------------------------------------

--
-- Table structure for table `collaborations`
--

DROP TABLE IF EXISTS `collaborations`;
CREATE TABLE IF NOT EXISTS `collaborations` (
  `collab_id` int(10) AUTO_INCREMENT,
  `cc_id` int(10),
  `brand_id` int(10),
  `collab_title` varchar(20),
  `collab_status` varchar(20),
  PRIMARY KEY (`collab_id`)
) ENGINE=InnoDB AUTO_INCREMENT=1 DEFAULT CHARSET=utf8;

--
-- Dumping data for table `collaborations`
--

INSERT INTO `collaborations` (`collab_id`, `cc_id`, `brand_id`, `collab_title`, `collab_status`) VALUES
(1, '0101', '0201', 'Nike Collab', 'Pending');


/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
