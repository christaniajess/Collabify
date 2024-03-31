-- phpMyAdmin SQL Dump
-- version 5.2.0
-- https://www.phpmyadmin.net/
--
-- Host: localhost:8889
-- Generation Time: Mar 30, 2024 at 07:22 AM
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
-- Database: `account`
--

-- --------------------------------------------------------

--
-- Table structure for table `account`
--

DROP TABLE IF EXISTS `account`;
CREATE DATABASE IF NOT EXISTS `account`;
USE `account`;




CREATE TABLE `account` (
  `user_id` int(10) UNSIGNED NOT NULL,
  `username` text NOT NULL,
  `acc_type` text NOT NULL,
  `full_name` text NOT NULL,
  `email` text NOT NULL,
  `password` text NOT NULL,
  `user_photo` text,
  `interests` text,
  `stripe_key` text
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

--
-- Dumping data for table `account`
--

INSERT INTO `account` (`user_id`, `username`, `acc_type`, `full_name`, `email`, `password`, `user_photo`, `interests`, `stripe_key`) VALUES
(100, 'john_doe', 'cc', 'John Doe', '1915408967@qq.com', '100', 'user1.jpg', 'food,cars', 'sk_test_51OuGi52KwIS1b45LvlM5Q8z0AaTmdNohKDWk3pOEKhNbvOmHJmCEU9DWbSab871Yal3Qw5H2QMXDynjOuQC6NLXB00NBUhtZne'),
(101, 'brand_inc', 'brand', 'Brand Inc', '1915408967@qq.com', '101', 'user2.jpg', 'sports,food', 'sk_test_51OuGi52KwIS1b45LvlM5Q8z0AaTmdNohKDWk3pOEKhNbvOmHJmCEU9DWbSab871Yal3Qw5H2QMXDynjOuQC6NLXB00NBUhtZne'),
(102, 'alex_jones', 'cc', 'Alex Jones', '1915408967@qq.com', '102', 'user3.jpg', 'food,travel', 'sk_test_51OuGi52KwIS1b45LvlM5Q8z0AaTmdNohKDWk3pOEKhNbvOmHJmCEU9DWbSab871Yal3Qw5H2QMXDynjOuQC6NLXB00NBUhtZne'),
(103, 'brand_max', 'brand', 'Max Corporation', '1915408967@qq.com', '103', 'user4.jpg', 'food,cars', 'sk_test_51OuGi52KwIS1b45LvlM5Q8z0AaTmdNohKDWk3pOEKhNbvOmHJmCEU9DWbSab871Yal3Qw5H2QMXDynjOuQC6NLXB00NBUhtZne'),
(104, 'michael_wilson', 'cc', 'Michael Wilson', '1915408967@qq.com', '104', 'user5.jpg', 'technology,food', 'sk_test_51OuGi52KwIS1b45LvlM5Q8z0AaTmdNohKDWk3pOEKhNbvOmHJmCEU9DWbSab871Yal3Qw5H2QMXDynjOuQC6NLXB00NBUhtZne'),
(105, 'brand_media', 'brand', 'Media Enterprises', '1915408967@qq.com', '105', 'user6.jpg', 'food,books', 'sk_test_51OuGi52KwIS1b45LvlM5Q8z0AaTmdNohKDWk3pOEKhNbvOmHJmCEU9DWbSab871Yal3Qw5H2QMXDynjOuQC6NLXB00NBUhtZne'),
(106, 'david_miller', 'cc', 'David Miller', '1915408967@qq.com', '106', 'user7.jpg', 'food,cars', 'sk_test_51OuGi52KwIS1b45LvlM5Q8z0AaTmdNohKDWk3pOEKhNbvOmHJmCEU9DWbSab871Yal3Qw5H2QMXDynjOuQC6NLXB00NBUhtZne'),
(107, 'brandify', 'brand', 'Brandify', '1915408967@qq.com', '107', 'user8.jpg', 'food,travel', 'sk_test_51OuGi52KwIS1b45LvlM5Q8z0AaTmdNohKDWk3pOEKhNbvOmHJmCEU9DWbSab871Yal3Qw5H2QMXDynjOuQC6NLXB00NBUhtZne'),
(108, 'chris_anderson', 'cc', 'Chris Anderson', '1915408967@qq.com', '108', 'user9.jpg', 'movies,food', 'sk_test_51OuGi52KwIS1b45LvlM5Q8z0AaTmdNohKDWk3pOEKhNbvOmHJmCEU9DWbSab871Yal3Qw5H2QMXDynjOuQC6NLXB00NBUhtZne'),
(109, 'brand_tech', 'brand', 'Tech Solutions', '1915408967@qq.com', '109', 'user10.jpg', 'food,shopping', 'sk_test_51OuGi52KwIS1b45LvlM5Q8z0AaTmdNohKDWk3pOEKhNbvOmHJmCEU9DWbSab871Yal3Qw5H2QMXDynjOuQC6NLXB00NBUhtZne'),
(110, 'paul_rodriguez', 'cc', 'Paul Rodriguez', '1915408967@qq.com', '110', 'user11.jpg', 'food,technology', 'sk_test_51OuGi52KwIS1b45LvlM5Q8z0AaTmdNohKDWk3pOEKhNbvOmHJmCEU9DWbSab871Yal3Qw5H2QMXDynjOuQC6NLXB00NBUhtZne'),
(111, 'brand_co', 'brand', 'Co Enterprises', '1915408967@qq.com', '111', 'user12.jpg', 'food,cars', 'sk_test_51OuGi52KwIS1b45LvlM5Q8z0AaTmdNohKDWk3pOEKhNbvOmHJmCEU9DWbSab871Yal3Qw5H2QMXDynjOuQC6NLXB00NBUhtZne'),
(112, 'kevin_garcia', 'cc', 'Kevin Garcia', '1915408967@qq.com', '112', 'user13.jpg', 'music,food', 'sk_test_51OuGi52KwIS1b45LvlM5Q8z0AaTmdNohKDWk3pOEKhNbvOmHJmCEU9DWbSab871Yal3Qw5H2QMXDynjOuQC6NLXB00NBUhtZne'),
(113, 'acme_corp', 'brand', 'Acme Corporation', '1915408967@qq.com', '113', 'user14.jpg', 'food,cars', 'sk_test_51OuGi52KwIS1b45LvlM5Q8z0AaTmdNohKDWk3pOEKhNbvOmHJmCEU9DWbSab871Yal3Qw5H2QMXDynjOuQC6NLXB00NBUhtZne'),
(114, 'tech_data', 'brand', 'Tech Data Corporation', '1915408967@qq.com', '114', 'user15.jpg', 'sports,food', 'sk_test_51OuGi52KwIS1b45LvlM5Q8z0AaTmdNohKDWk3pOEKhNbvOmHJmCEU9DWbSab871Yal3Qw5H2QMXDynjOuQC6NLXB00NBUhtZne'),
(115, 'united_nations', 'brand', 'United Nations', '1915408967@qq.com', '115', 'user16.jpg', 'food,travel', 'sk_test_51OuGi52KwIS1b45LvlM5Q8z0AaTmdNohKDWk3pOEKhNbvOmHJmCEU9DWbSab871Yal3Qw5H2QMXDynjOuQC6NLXB00NBUhtZne'),
(116, 'warner_media', 'brand', 'Warner Media', '1915408967@qq.com', '116', 'user17.jpg', 'food,cars', 'sk_test_51OuGi52KwIS1b45LvlM5Q8z0AaTmdNohKDWk3pOEKhNbvOmHJmCEU9DWbSab871Yal3Qw5H2QMXDynjOuQC6NLXB00NBUhtZne'),
(117, 'starbucks', 'brand', 'Starbucks Corporation', '1915408967@qq.com', '117', 'user18.jpg', 'technology,food', 'sk_test_51OuGi52KwIS1b45LvlM5Q8z0AaTmdNohKDWk3pOEKhNbvOmHJmCEU9DWbSab871Yal3Qw5H2QMXDynjOuQC6NLXB00NBUhtZne'),
(118, 'tesla', 'brand', 'Tesla, Inc.', '1915408967@qq.com', '118', 'user19.jpg', 'food,books', 'sk_test_51OuGi52KwIS1b45LvlM5Q8z0AaTmdNohKDWk3pOEKhNbvOmHJmCEU9DWbSab871Yal3Qw5H2QMXDynjOuQC6NLXB00NBUhtZne'),
(119, 'amazon', 'brand', 'Amazon.com, Inc.', '1915408967@qq.com', '119', 'user20.jpg', 'food,cars', 'sk_test_51OuGi52KwIS1b45LvlM5Q8z0AaTmdNohKDWk3pOEKhNbvOmHJmCEU9DWbSab871Yal3Qw5H2QMXDynjOuQC6NLXB00NBUhtZne'),
(120, 'nike', 'brand', 'Nike, Inc.', '1915408967@qq.com', '120', 'user21.jpg', 'food,travel', 'sk_test_51OuGi52KwIS1b45LvlM5Q8z0AaTmdNohKDWk3pOEKhNbvOmHJmCEU9DWbSab871Yal3Qw5H2QMXDynjOuQC6NLXB00NBUhtZne'),
(121, 'microsoft', 'brand', 'Microsoft Corporation', '1915408967@qq.com', '121', 'user22.jpg', 'movies,food', 'sk_test_51OuGi52KwIS1b45LvlM5Q8z0AaTmdNohKDWk3pOEKhNbvOmHJmCEU9DWbSab871Yal3Qw5H2QMXDynjOuQC6NLXB00NBUhtZne'),
(122, 'apple', 'brand', 'Apple Inc.', '1915408967@qq.com', '122', 'user23.jpg', 'food,shopping', 'sk_test_51OuGi52KwIS1b45LvlM5Q8z0AaTmdNohKDWk3pOEKhNbvOmHJmCEU9DWbSab871Yal3Qw5H2QMXDynjOuQC6NLXB00NBUhtZne'),
(123, 'lucy_smith', 'cc', 'Lucy Smith', '1915408967@qq.com', '123', 'user24.jpg', 'food,cars', 'sk_test_51OuGi52KwIS1b45LvlM5Q8z0AaTmdNohKDWk3pOEKhNbvOmHJmCEU9DWbSab871Yal3Qw5H2QMXDynjOuQC6NLXB00NBUhtZne'),
(124, 'james_johnson', 'cc', 'James Johnson', '1915408967@qq.com', '124', 'user25.jpg', 'sports,food', 'sk_test_51OuGi52KwIS1b45LvlM5Q8z0AaTmdNohKDWk3pOEKhNbvOmHJmCEU9DWbSab871Yal3Qw5H2QMXDynjOuQC6NLXB00NBUhtZne'),
(125, 'sophia_williams', 'cc', 'Sophia Williams', '1915408967@qq.com', '125', 'user26.jpg', 'food,travel', 'sk_test_51OuGi52KwIS1b45LvlM5Q8z0AaTmdNohKDWk3pOEKhNbvOmHJmCEU9DWbSab871Yal3Qw5H2QMXDynjOuQC6NLXB00NBUhtZne'),
(126, 'liam_brown', 'cc', 'Liam Brown', '1915408967@qq.com', '126', 'user27.jpg', 'food,cars', 'sk_test_51OuGi52KwIS1b45LvlM5Q8z0AaTmdNohKDWk3pOEKhNbvOmHJmCEU9DWbSab871Yal3Qw5H2QMXDynjOuQC6NLXB00NBUhtZne'),
(127, 'olivia_jones', 'cc', 'Olivia Jones', '1915408967@qq.com', '127', 'user28.jpg', 'technology,food', 'sk_test_51OuGi52KwIS1b45LvlM5Q8z0AaTmdNohKDWk3pOEKhNbvOmHJmCEU9DWbSab871Yal3Qw5H2QMXDynjOuQC6NLXB00NBUhtZne'),
(128, 'william_davis', 'cc', 'William Davis', '1915408967@qq.com', '128', 'user29.jpg', 'food,books', 'sk_test_51OuGi52KwIS1b45LvlM5Q8z0AaTmdNohKDWk3pOEKhNbvOmHJmCEU9DWbSab871Yal3Qw5H2QMXDynjOuQC6NLXB00NBUhtZne'),
(129, 'emma_miller', 'cc', 'Emma Miller', '1915408967@qq.com', '129', 'user30.jpg', 'food,cars', 'sk_test_51OuGi52KwIS1b45LvlM5Q8z0AaTmdNohKDWk3pOEKhNbvOmHJmCEU9DWbSab871Yal3Qw5H2QMXDynjOuQC6NLXB00NBUhtZne'),
(130, 'michael_jackson', 'cc', 'Michael Jackson', '1915408967@qq.com', '130', 'user31.jpg', 'music,food', 'sk_test_51OuGi52KwIS1b45LvlM5Q8z0AaTmdNohKDWk3pOEKhNbvOmHJmCEU9DWbSab871Yal3Qw5H2QMXDynjOuQC6NLXB00NBUhtZne'),
(131, 'ava_taylor', 'cc', 'Ava Taylor', '1915408967@qq.com', '131', 'user32.jpg', 'food,shopping', 'sk_test_51OuGi52KwIS1b45LvlM5Q8z0AaTmdNohKDWk3pOEKhNbvOmHJmCEU9DWbSab871Yal3Qw5H2QMXDynjOuQC6NLXB00NBUhtZne'),
(132, 'alexander_anderson', 'cc', 'Alexander Anderson', '1915408967@qq.com', '132', 'user33.jpg', 'food,technology', 'sk_test_51OuGi52KwIS1b45LvlM5Q8z0AaTmdNohKDWk3pOEKhNbvOmHJmCEU9DWbSab871Yal3Qw5H2QMXDynjOuQC6NLXB00NBUhtZne');

--
-- Indexes for dumped tables
--

--
-- Indexes for table `account`
--
ALTER TABLE `account`
  ADD PRIMARY KEY (`user_id`);
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
