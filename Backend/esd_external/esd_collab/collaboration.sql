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
('100', '103', 'Max Data Collaboration', 'Pending'),
('100', '105', 'Media Marketing Campaign', 'In-progress'),
('100', '107', 'Brandify Health & Wellness Event', 'Pending'),
('100', '109', 'Tech Product Launch', 'Pending'),
('100', '111', 'Video Series Production', 'In-progress'),
('100', '113', 'Acme Endorsement Deal', 'Review'),
('100', '114', 'Tech Review Video', 'Review'),
('100', '116', 'Warner Media Content Creation', 'Pending'),
('100', '117', 'Starbucks Website Campaign', 'Pending'),
('100', '118', 'Tesla Campaign', 'In-progress'),
('100', '120', 'Brandify Charity Event', 'Review'),
('123', '117', 'Fashion Line Promotion', 'Pending'),
('127', '117', 'Michael Jackson Music Album Launch', 'In-progress'),
('128', '117', 'Olivia Jones Lifestyle Blog Feature', 'In-progress'),
('130', '117', 'Apple Product Launch Event', 'In-progress'),
('131', '117', 'Acme Corporation Partnership', 'Review'),
('138', '117', 'Ava Taylor Fitness Apparel Sponsorship', 'Review'),
('139', '117', 'Alexander Andersons Podcast Collaboration', 'Pending'),
('141', '117', 'William Davis Travel Vlog Partnership', 'Review'),
('142', '117', 'James Johnson Food Recipe Series', 'Pending');

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
