-- phpMyAdmin SQL Dump
-- version 5.2.0
-- https://www.phpmyadmin.net/
--
-- Host: localhost:8889
-- Generation Time: Mar 19, 2024 at 08:10 AM
-- Server version: 5.7.39
-- PHP Version: 8.2.0

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Database: `review`
--

-- --------------------------------------------------------

--
-- Table structure for table `review`
--
CREATE DATABASE IF NOT EXISTS `review` DEFAULT CHARACTER SET utf8 COLLATE utf8_general_ci;
USE `review`;
CREATE TABLE `review` (
  `review_id` int(11) NOT NULL,
  `cc_id` int(11) NOT NULL,
  `brand_id` int(11) NOT NULL,
  `rating` int(11) NOT NULL,
  `title` varchar(20) NOT NULL,
  `content` varchar(200) NOT NULL,
  `timestamp` datetime DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

--
-- Dumping data for table `review`
--

INSERT INTO `review` (`review_id`, `cc_id`, `brand_id`, `rating`, `title`, `content`, `timestamp`) VALUES
(1, 14, 8, 3, 'Needs Improvement', 'The project did not meet our expectations. Improvement needed.', '2024-01-31 13:57:43'),
(2, 20, 6, 2, 'Great Collaboration', 'There were some communication issues, but overall it was okay.', '2023-09-11 13:57:43'),
(3, 3, 3, 3, 'Not Satisfied', 'There were some communication issues, but overall it was okay.', '2023-04-13 13:57:43'),
(4, 17, 3, 3, 'Not Satisfied', 'The project did not meet our expectations. Improvement needed.', '2023-06-21 13:57:43'),
(5, 7, 3, 1, 'Excellent Work', 'Amazing creativity and delivered on time. Will definitely work together again.', '2023-07-19 13:57:43'),
(6, 11, 4, 5, 'Not Satisfied', 'The collaboration went smoothly, and the output was fantastic.', '2023-12-02 13:57:43'),
(7, 3, 2, 4, 'Great Collaboration', 'There were some communication issues, but overall it was okay.', '2023-06-04 13:57:43'),
(8, 13, 7, 4, 'Great Collaboration', 'There were some communication issues, but overall it was okay.', '2023-06-28 13:57:43'),
(9, 7, 6, 2, 'Needs Improvement', 'There were some communication issues, but overall it was okay.', '2023-12-26 13:57:43'),
(10, 14, 1, 4, 'Not Satisfied', 'Amazing creativity and delivered on time. Will definitely work together again.', '2023-08-25 13:57:43'),
(11, 20, 7, 5, 'Needs Improvement', 'The project did not meet our expectations. Improvement needed.', '2023-05-19 13:57:43'),
(12, 3, 2, 5, 'Needs Improvement', 'Amazing creativity and delivered on time. Will definitely work together again.', '2023-10-13 13:57:43'),
(13, 12, 4, 4, 'Great Collaboration', 'Amazing creativity and delivered on time. Will definitely work together again.', '2023-09-18 13:57:43'),
(14, 20, 10, 4, 'Needs Improvement', 'Had a great time working together. Highly recommended!', '2023-11-19 13:57:43'),
(15, 5, 1, 5, 'Needs Improvement', 'Had a great time working together. Highly recommended!', '2023-04-21 13:57:43'),
(16, 1234567890, 9, 5, 'SO CHOCOLATY!', 'OOMPA LOOMPA DOOPITY DOO.', '2023-08-07 13:57:43'),
(17, 18, 4, 3, 'Excellent Work', 'Had a great time working together. Highly recommended!', '2023-12-11 13:57:43'),
(18, 12, 7, 3, 'Needs Improvement', 'The collaboration went smoothly, and the output was fantastic.', '2023-05-13 13:57:43'),
(19, 3, 1, 1, 'Excellent Work', 'The collaboration went smoothly, and the output was fantastic.', '2023-05-10 13:57:43'),
(20, 11, 4, 2, 'Great Collaboration', 'Amazing creativity and delivered on time. Will definitely work together again.', '2023-08-01 13:57:43'),
(21, 1234567890, 4, 1, 'Wonderful Experience', 'There were some communication issues, but overall it was okay.', '2023-04-16 13:57:43'),
(22, 20, 2, 2, 'Great Collaboration', 'The project did not meet our expectations. Improvement needed.', '2023-12-21 13:57:43'),
(23, 7, 2, 1, 'Wonderful Experience', 'The project did not meet our expectations. Improvement needed.', '2023-12-23 13:57:43'),
(24, 2, 4, 4, 'Great Collaboration', 'Amazing creativity and delivered on time. Will definitely work together again.', '2023-12-08 13:57:43'),
(25, 5, 1, 2, 'Wonderful Experience', 'Amazing creativity and delivered on time. Will definitely work together again.', '2023-09-11 13:57:43'),
(26, 15, 1, 2, 'Great Collaboration', 'Had a great time working together. Highly recommended!', '2023-11-07 13:57:43'),
(27, 5, 6, 4, 'Needs Improvement', 'Amazing creativity and delivered on time. Will definitely work together again.', '2024-03-03 13:57:43'),
(28, 9, 9, 3, 'Not Satisfied', 'The collaboration went smoothly, and the output was fantastic.', '2023-11-15 13:57:43'),
(29, 11, 5, 1, 'Needs Improvement', 'Had a great time working together. Highly recommended!', '2023-11-18 13:57:43'),
(30, 18, 3, 4, 'Not Satisfied', 'There were some communication issues, but overall it was okay.', '2024-02-22 13:57:43'),
(31, 16, 9, 3, 'Needs Improvement', 'The collaboration went smoothly, and the output was fantastic.', '2023-11-12 13:57:43'),
(32, 1234567890, 5, 1, 'Not Satisfied', 'Amazing creativity and delivered on time. Will definitely work together again.', '2023-10-05 13:57:43'),
(33, 8, 6, 5, 'Needs Improvement', 'The collaboration went smoothly, and the output was fantastic.', '2023-09-08 13:57:43'),
(34, 11, 9, 1, 'Needs Improvement', 'Amazing creativity and delivered on time. Will definitely work together again.', '2023-12-24 13:57:43'),
(35, 10, 4, 1, 'Not Satisfied', 'The collaboration went smoothly, and the output was fantastic.', '2023-03-30 13:57:43'),
(36, 8, 6, 4, 'Needs Improvement', 'Had a great time working together. Highly recommended!', '2023-06-09 13:57:43'),
(37, 1234567890, 9, 4, 'Not Satisfied', 'Amazing creativity and delivered on time. Will definitely work together again.', '2024-02-22 13:57:43'),
(38, 13, 7, 3, 'Great Collaboration', 'Had a great time working together. Highly recommended!', '2023-12-19 13:57:43'),
(39, 2, 6, 2, 'Excellent Work', 'Had a great time working together. Highly recommended!', '2023-06-17 13:57:43'),
(40, 12, 1, 1, 'Excellent Work', 'Amazing creativity and delivered on time. Will definitely work together again.', '2023-09-08 13:57:43'),
(41, 9, 7, 1, 'Excellent Work', 'The project did not meet our expectations. Improvement needed.', '2024-03-07 13:57:43'),
(42, 16, 9, 1, 'Not Satisfied', 'There were some communication issues, but overall it was okay.', '2023-05-30 13:57:43'),
(43, 16, 1, 4, 'Great Collaboration', 'There were some communication issues, but overall it was okay.', '2024-02-02 13:57:43'),
(44, 13, 3, 3, 'Needs Improvement', 'The collaboration went smoothly, and the output was fantastic.', '2024-02-04 13:57:43'),
(45, 13, 1, 3, 'Wonderful Experience', 'Had a great time working together. Highly recommended!', '2023-06-28 13:57:43'),
(46, 17, 10, 5, 'Great Collaboration', 'The project did not meet our expectations. Improvement needed.', '2023-07-02 13:57:43'),
(47, 17, 7, 3, 'Needs Improvement', 'Had a great time working together. Highly recommended!', '2023-10-13 13:57:43'),
(48, 18, 6, 5, 'Not Satisfied', 'Had a great time working together. Highly recommended!', '2023-11-11 13:57:43'),
(49, 18, 9, 2, 'Wonderful Experience', 'There were some communication issues, but overall it was okay.', '2023-07-25 13:57:43'),
(50, 12, 6, 4, 'Great Collaboration', 'The collaboration went smoothly, and the output was fantastic.', '2024-03-12 13:57:43'),
(51, 2, 5, 2, 'Wonderful Experience', 'The collaboration went smoothly, and the output was fantastic.', '2023-11-22 13:57:43'),
(52, 6, 1, 4, 'Great Collaboration', 'The collaboration went smoothly, and the output was fantastic.', '2023-09-04 13:57:43'),
(53, 2, 10, 1, 'Needs Improvement', 'There were some communication issues, but overall it was okay.', '2023-08-07 13:57:43'),
(54, 4, 2, 4, 'Not Satisfied', 'Had a great time working together. Highly recommended!', '2023-06-02 13:57:43'),
(55, 13, 1, 1, 'Wonderful Experience', 'The project did not meet our expectations. Improvement needed.', '2024-03-14 13:57:43'),
(56, 13, 8, 5, 'Not Satisfied', 'There were some communication issues, but overall it was okay.', '2023-03-27 13:57:43'),
(57, 10, 2, 1, 'Not Satisfied', 'Had a great time working together. Highly recommended!', '2023-05-11 13:57:43'),
(58, 7, 4, 2, 'Great Collaboration', 'Amazing creativity and delivered on time. Will definitely work together again.', '2023-06-15 13:57:43'),
(59, 20, 2, 3, 'Wonderful Experience', 'Amazing creativity and delivered on time. Will definitely work together again.', '2024-01-12 13:57:43'),
(60, 1234567890, 7, 4, 'Wonderful Experience', 'Amazing creativity and delivered on time. Will definitely work together again.', '2023-07-20 13:57:43'),
(61, 18, 3, 4, 'Excellent Work', 'There were some communication issues, but overall it was okay.', '2024-02-09 13:57:43'),
(62, 12, 8, 1, 'Needs Improvement', 'The project did not meet our expectations. Improvement needed.', '2023-09-30 13:57:43'),
(63, 6, 9, 4, 'Needs Improvement', 'Had a great time working together. Highly recommended!', '2024-01-03 13:57:43'),
(64, 4, 6, 1, 'Wonderful Experience', 'The collaboration went smoothly, and the output was fantastic.', '2023-09-09 13:57:43'),
(65, 9, 4, 5, 'Needs Improvement', 'The collaboration went smoothly, and the output was fantastic.', '2023-03-21 13:57:43'),
(66, 8, 9, 5, 'Great Collaboration', 'The collaboration went smoothly, and the output was fantastic.', '2023-05-17 13:57:43'),
(67, 6, 3, 2, 'Needs Improvement', 'There were some communication issues, but overall it was okay.', '2023-12-21 13:57:43'),
(68, 18, 7, 5, 'Wonderful Experience', 'There were some communication issues, but overall it was okay.', '2024-01-03 13:57:43'),
(69, 14, 10, 4, 'Excellent Work', 'There were some communication issues, but overall it was okay.', '2023-09-29 13:57:43'),
(70, 3, 7, 5, 'Great Collaboration', 'Amazing creativity and delivered on time. Will definitely work together again.', '2023-10-12 13:57:43'),
(71, 17, 1, 4, 'Great Collaboration', 'Had a great time working together. Highly recommended!', '2023-09-15 13:57:43'),
(72, 16, 2, 1, 'Needs Improvement', 'The project did not meet our expectations. Improvement needed.', '2023-10-13 13:57:43'),
(73, 6, 7, 2, 'Not Satisfied', 'Amazing creativity and delivered on time. Will definitely work together again.', '2023-06-27 13:57:43'),
(74, 6, 4, 5, 'Excellent Work', 'There were some communication issues, but overall it was okay.', '2023-03-19 13:57:43'),
(75, 13, 6, 2, 'Not Satisfied', 'Amazing creativity and delivered on time. Will definitely work together again.', '2023-04-17 13:57:43'),
(76, 16, 9, 3, 'Excellent Work', 'The collaboration went smoothly, and the output was fantastic.', '2023-08-05 13:57:43'),
(77, 14, 10, 2, 'Not Satisfied', 'The project did not meet our expectations. Improvement needed.', '2023-05-12 13:57:43'),
(78, 11, 1, 5, 'Wonderful Experience', 'Had a great time working together. Highly recommended!', '2023-11-02 13:57:43'),
(79, 1234567890, 4, 2, 'Wonderful Experience', 'The project did not meet our expectations. Improvement needed.', '2023-09-16 13:57:43'),
(80, 20, 9, 2, 'Excellent Work', 'The collaboration went smoothly, and the output was fantastic.', '2023-11-05 13:57:43'),
(81, 1234567890, 4, 4, 'Great Collaboration', 'Amazing creativity and delivered on time. Will definitely work together again.', '2023-05-07 13:57:43'),
(82, 13, 2, 4, 'Wonderful Experience', 'Amazing creativity and delivered on time. Will definitely work together again.', '2023-10-09 13:57:43'),
(83, 16, 2, 5, 'Wonderful Experience', 'The project did not meet our expectations. Improvement needed.', '2023-07-26 13:57:43'),
(84, 10, 8, 2, 'Wonderful Experience', 'Had a great time working together. Highly recommended!', '2024-01-26 13:57:43'),
(85, 3, 8, 1, 'Not Satisfied', 'Had a great time working together. Highly recommended!', '2023-06-28 13:57:43'),
(86, 12, 2, 2, 'Wonderful Experience', 'Amazing creativity and delivered on time. Will definitely work together again.', '2023-04-28 13:57:43'),
(87, 11, 9, 1, 'Excellent Work', 'The collaboration went smoothly, and the output was fantastic.', '2023-11-25 13:57:43'),
(88, 7, 4, 2, 'Great Collaboration', 'Had a great time working together. Highly recommended!', '2023-03-22 13:57:43'),
(89, 15, 6, 4, 'Excellent Work', 'Had a great time working together. Highly recommended!', '2023-09-20 13:57:43'),
(90, 2, 2, 4, 'Excellent Work', 'Amazing creativity and delivered on time. Will definitely work together again.', '2023-05-09 13:57:43'),
(91, 15, 2, 4, 'Great Collaboration', 'There were some communication issues, but overall it was okay.', '2023-07-27 13:57:43'),
(92, 17, 3, 1, 'Not Satisfied', 'The project did not meet our expectations. Improvement needed.', '2024-02-19 13:57:43'),
(93, 12, 9, 2, 'Great Collaboration', 'The project did not meet our expectations. Improvement needed.', '2024-02-20 13:57:43'),
(94, 5, 9, 4, 'Excellent Work', 'Had a great time working together. Highly recommended!', '2023-04-24 13:57:43'),
(95, 3, 1, 4, 'Excellent Work', 'The collaboration went smoothly, and the output was fantastic.', '2023-10-29 13:57:43'),
(96, 17, 3, 4, 'Not Satisfied', 'Had a great time working together. Highly recommended!', '2023-12-22 13:57:43'),
(97, 9, 6, 2, 'Wonderful Experience', 'There were some communication issues, but overall it was okay.', '2024-01-06 13:57:43'),
(98, 10, 7, 2, 'Wonderful Experience', 'Had a great time working together. Highly recommended!', '2024-02-11 13:57:43'),
(99, 14, 9, 5, 'Wonderful Experience', 'The project did not meet our expectations. Improvement needed.', '2023-08-01 13:57:43'),
(100, 5, 3, 4, 'Not Satisfied', 'The collaboration went smoothly, and the output was fantastic.', '2024-01-03 13:57:43');

--
-- Indexes for dumped tables
--

--
-- Indexes for table `review`
--
ALTER TABLE `review`
  ADD PRIMARY KEY (`review_id`);

--
-- AUTO_INCREMENT for dumped tables
--

--
-- AUTO_INCREMENT for table `review`
--
ALTER TABLE `review`
  MODIFY `review_id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=101;
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
