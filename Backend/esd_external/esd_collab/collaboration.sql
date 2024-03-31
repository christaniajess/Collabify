-- phpMyAdmin SQL Dump
-- version 5.2.0
-- https://www.phpmyadmin.net/
--
-- Host: localhost:8889
-- Generation Time: Mar 30, 2024 at 07:23 AM
-- Server version: 5.7.39
-- PHP Version: 7.4.33

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Database: `collaboration`
--
DROP DATABASE IF EXISTS `collaboration`;
CREATE DATABASE IF NOT EXISTS `collaboration` DEFAULT CHARACTER SET utf8 COLLATE utf8_general_ci;
USE `collaboration`;

-- --------------------------------------------------------

--
-- Table structure for table `collaboration`
--

CREATE TABLE `collaboration` (
  `cc_id` varchar(100) NOT NULL,
  `brand_id` varchar(100) NOT NULL,
  `collab_title` varchar(100) DEFAULT NULL,
  `collab_status` varchar(20) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

--
-- Dumping data for table `collaboration`
--

INSERT INTO `collaboration` (`cc_id`, `brand_id`, `collab_title`, `collab_status`) VALUES
('123', '103', 'Tech Data Collaboration', 'Pending'),
('124', '105', 'Starbucks Marketing Campaign', 'In-progress'),
('125', '107', 'United Nations Charity Event', 'Review'),
('126', '109', 'Tesla Product Launch', 'Pending'),
('127', '111', 'Amazon Prime Video Series Production', 'In-progress'),
('128', '113', 'Nike Endorsement Deal', 'Review'),
('129', '115', 'Microsoft Software Development', 'Pending'),
('130', '117', 'Apple Product Launch Event', 'In-progress'),
('131', '119', 'Acme Corporation Partnership', 'Review'),
('132', '121', 'Warner Media Content Creation', 'Pending'),
('133', '123', 'Lucy Smith Fashion Line Promotion', 'Pending'),
('134', '125', 'Sophia William Beauty Campaign', 'In-progress'),
('135', '127', 'Liam Brown Tech Review Video', 'Review'),
('136', '129', 'Emma Miller Health & Wellness Event', 'Pending'),
('137', '131', 'Michael Jackson Music Album Launch', 'In-progress'),
('138', '133', 'Ava Taylor Fitness Apparel Sponsorship', 'Review'),
('139', '135', 'Alexander Andersons Podcast Collaboration', 'Pending'),
('140', '137', 'Olivia Jones Lifestyle Blog Feature', 'In-progress'),
('141', '139', 'William Davis Travel Vlog Partnership', 'Review'),
('142', '141', 'James Johnson Food Recipe Series', 'Pending');

--
-- Indexes for dumped tables
--

--
-- Indexes for table `collaboration`
--
ALTER TABLE `collaboration`
  ADD PRIMARY KEY (`cc_id`,`brand_id`);
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
