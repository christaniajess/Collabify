-- phpMyAdmin SQL Dump
-- version 5.2.0
-- https://www.phpmyadmin.net/
--
-- Host: localhost:8889
-- Generation Time: Mar 30, 2024 at 07:24 AM
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
-- Database: `review`
--

-- --------------------------------------------------------

--
-- Table structure for table `review`
--

CREATE TABLE `review` (
  `review_id` int(11) NOT NULL,
  `cc_id` int(11) NOT NULL,
  `brand_id` int(11) NOT NULL,
  `rating` int(11) NOT NULL,
  `title` varchar(50) NOT NULL,
  `content` varchar(200) NOT NULL,
  `timestamp` datetime DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

--
-- Dumping data for table `review`
--

INSERT INTO `review` (`review_id`, `cc_id`, `brand_id`, `rating`, `title`, `content`, `timestamp`) VALUES
(101, 123, 103, 5, 'Fantastic Collaboration Experience', 'Working with Tech Data was amazing. They delivered outstanding results and were a pleasure to work with.', '2024-04-01 09:30:00'),
(102, 123, 105, 4, 'Successful Marketing Campaign', 'Starbucks marketing campaign was successful. It helped drive engagement and increase brand visibility.', '2024-04-02 11:45:00'),
(103, 123, 107, 5, 'Great Charity Event', 'The United Nations charity event organized by Starbucks was a great success. It made a positive impact on the community.', '2024-04-03 13:20:00'),
(104, 124, 109, 4, 'Impressive Product Launch', 'Tesla product launch event was impressive. The new products generated excitement among customers.', '2024-04-04 15:10:00'),
(105, 124, 111, 5, 'Exceptional Video Production', 'Amazon Prime Video series produced by Tesla was exceptional. The content was engaging and well-received.', '2024-04-05 10:55:00'),
(106, 124, 113, 4, 'Successful Endorsement Deal', 'The Nike endorsement deal executed by Tesla was successful. It boosted brand recognition and sales.', '2024-04-06 14:25:00'),
(107, 125, 115, 5, 'Innovative Software Development', 'Microsoft software development project was innovative. It introduced new features that improved user experience.', '2024-04-07 12:45:00'),
(108, 125, 117, 4, 'Well-Executed Product Launch Event', 'Apple product launch event organized by Microsoft was well-executed. It showcased the latest innovations effectively.', '2024-04-08 09:15:00'),
(109, 125, 119, 5, 'Successful Partnership Experience', 'Our collaboration with Acme Corporation was successful. It brought mutual benefits and achieved our goals.', '2024-04-09 16:30:00'),
(110, 126, 121, 4, 'Creative Content Creation', 'Warner Media content creation project led by Microsoft was creative. It delivered unique and engaging content.', '2024-04-10 08:20:00'),
(111, 126, 116, 5, 'Outstanding Tech Reviews', 'Tech reviews produced by Warner Media were outstanding. They provided valuable insights and information.', '2024-04-11 09:30:00'),
(112, 126, 122, 4, 'Engaging Podcast Series', 'Podcast series created by Warner Media were engaging and informative. They covered relevant topics and kept listeners hooked.', '2024-04-12 11:45:00');

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
  MODIFY `review_id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=113;
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
