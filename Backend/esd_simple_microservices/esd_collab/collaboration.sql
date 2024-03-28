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
CREATE DATABASE IF NOT EXISTS `collaboration` DEFAULT CHARACTER SET utf8 COLLATE utf8_general_ci;
USE `collaboration`;

-- --------------------------------------------------------

--
-- Table structure for table `collaboration`
--

DROP TABLE IF EXISTS `collaboration`;
CREATE TABLE IF NOT EXISTS `collaboration` (
  `cc_id` VARCHAR(100),
  `cc_name` VARCHAR(100),
  `brand_id` VARCHAR(100),
  `brand_name` VARCHAR(100),
  `collab_title` varchar(100),
  `collab_status` varchar(100),
  PRIMARY KEY (`cc_id`, `brand_id`, `collab_title`)
) ENGINE=InnoDB AUTO_INCREMENT=1 DEFAULT CHARSET=utf8;


--
-- Dumping data for table `collaboration`
--

INSERT INTO `collaboration` (`cc_id`, `cc_name`, `brand_id`, `brand_name`, `collab_title`, `collab_status`) VALUES
('4387', 'Alex Johnson', '8912', 'Nike', 'Alex X Nike Spring Collection', 'Pending'),
('5276', 'Mia Wong', '4956', 'Reebok', 'Mia X Reebok Fitness Line', 'In-Progress'),
('6345', 'Carlos Gutierrez', '7623', 'Adidas', 'Carlos X Adidas Soccer Edition', 'Done'),
('7918', 'Samantha Davis', '4067', 'New Balance', 'Samantha X NB Running Tech', 'Completed'),
('8657', 'Emily Zhang', '6734', 'Puma', 'Emily X Puma Lifestyle Series', 'Pending'),
('9726', 'Olivia Smith', '2289', 'Saucony', 'Olivia X Saucony Trail Gear', 'In-Progress'),
('4387', 'Alex Johnson', '7623', 'Adidas', 'Alex X Adidas Winter Capsule', 'Done'),
('5276', 'Mia Wong', '6734', 'Puma', 'Mia X Puma Heritage Collection', 'Completed'),
('6345', 'Carlos Gutierrez', '8912', 'Nike', 'Carlos X Nike Performance Wear', 'Pending'),
('7918', 'Samantha Davis', '2289', 'Saucony', 'Samantha X Saucony Run Series', 'In-Progress'),
('8657', 'Emily Zhang', '4956', 'Reebok', 'Emily X Reebok Classic Revivals', 'Done'),
('2254', 'Izzey Miyake', '6504', 'The North Face', 'Miyake X TNF Exploration Gear', 'In-Progress'),
('9726', 'Olivia Smith', '4067', 'New Balance', 'Olivia X NB Exclusive Drops', 'Completed'),
('4387', 'Alex Johnson', '2289', 'Saucony', 'Alex X Saucony Limited Edition', 'Pending'),
('5276', 'Mia Wong', '8912', 'Nike', 'Mia X Nike Air Max Day Special', 'In-Progress'),
('6345', 'Carlos Gutierrez', '4956', 'Reebok', 'Carlos X Reebok Spartan Series', 'Completed'),
('7918', 'Samantha Davis', '6734', 'Puma', 'Samantha X Puma Fast Track', 'Pending'),
('8657', 'Emily Zhang', '8912', 'Nike', 'Emily X Nike Revolution', 'In-Progress'),
('9726', 'Olivia Smith', '7623', 'Adidas', 'Olivia X Adidas Originals', 'Done'),
('2254', 'Izzey Miyake', '3201', 'Lululemon', 'Miyake X Lululemon Performance Series', 'Completed'),
('4387', 'Alex Johnson', '4067', 'New Balance', 'Alex X NB Urban Explorers', 'Completed'),
('5276', 'Mia Wong', '2289', 'Saucony', 'Mia X Saucony Freedom ISO Launch', 'Pending'),
('6345', 'Carlos Gutierrez', '4067', 'New Balance', 'Carlos X NB Trailblazers', 'In-Progress'),
('7918', 'Samantha Davis', '8912', 'Nike', 'Samantha X Nike Heritage Line', 'Done'),
('8657', 'Emily Zhang', '6734', 'Puma', 'Emily X Puma Classics Reimagined', 'Completed'),
('9726', 'Olivia Smith', '4956', 'Reebok', 'Olivia X Reebok Innovation Lab', 'Pending'),
('4387', 'Alex Johnson', '7623', 'Adidas', 'Alex X Adidas Streetwear Edition', 'In-Progress'),
('5276', 'Mia Wong', '6734', 'Puma', 'Mia X Puma Eco Innovation', 'Done'),
('6345', 'Carlos Gutierrez', '2289', 'Saucony', 'Carlos X Saucony Cohesion', 'Completed'),
('7918', 'Samantha Davis', '4067', 'New Balance', 'Samantha X NB Fresh Foam', 'Pending'),
('9982', 'Noah Lee', '3201', 'Lululemon', 'Noah X Lululemon Athletica Series', 'In-Progress'),
('1143', 'Isabella Martinez', '4302', 'Patagonia', 'Isabella X Patagonia Outdoor Essentials', 'Done'),
('3365', 'Ava Smith', '6504', 'The North Face', 'Ava X TNF Summit Series', 'Completed'),
('4476', 'Matthew Jones', '7605', 'Merrell', 'Matthew X Merrell Trail Run', 'In-Progress'),
('1143', 'Isabella Martinez', '6504', 'The North Face', 'Isabella X TNF Eco Innovation', 'Pending'),
('2254', 'Izzey Miyake', '3201', 'Lululemon', 'Miyake X Lululemon Studio Line', 'Completed'),
('3365', 'Ava Smith', '4302', 'Patagonia', 'Ava X Patagonia Limited Edition', 'In-Progress'),
('4476', 'Matthew Jones', '7605', 'Merrell', 'Matthew X Merrell Hiking Tech', 'Done'),
('2254', 'Izzey Miyake', '7605', 'Merrell', 'Miyake X Merrell Wild Hike', 'Done'),
('9982', 'Noah Lee', '6504', 'The North Face', 'Noah X TNF Advanced Mountain Gear', 'Completed'),
('1143', 'Isabella Martinez', '7605', 'Merrell', 'Isabella X Merrell Adventure Series', 'Pending'),
('2254', 'Izzey Miyake', '4302', 'Patagonia', 'Miyake X Patagonia Sustainable Wear', 'In-Progress'),
('3365', 'Ava Smith', '3201', 'Lululemon', 'Ava X Lululemon Yoga Collection', 'Done');







/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
