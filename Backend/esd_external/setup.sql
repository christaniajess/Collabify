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
-- Database: `project`
--

DROP DATABASE IF EXISTS `project`;
CREATE DATABASE IF NOT EXISTS `project` DEFAULT CHARACTER SET utf8 COLLATE utf8_general_ci;
USE `project`;

-- --------------------------------------------------------

--
-- Table structure for table `project`
--


CREATE TABLE `project` (
  `proj_id` int(10) UNSIGNED NOT NULL,
  `user_id` int(10) UNSIGNED NOT NULL,
  `proj_name` text NOT NULL,
  `proj_image` text NOT NULL,
  `proj_description` text NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

--
-- Dumping data for table `project`
--

INSERT INTO `project` (`proj_id`, `user_id`, `proj_name`, `proj_image`, `proj_description`) VALUES
(43, 100, 'YouTube Channel Launch: Eco-Friendly Living', 'proj1.jpg', 'Creating engaging videos promoting sustainable lifestyle choices for viewers.'),
(44, 100, 'Instagram Campaign: Reduce, Reuse, Recycle', 'proj2.jpg', 'Launching an Instagram campaign to inspire followers to adopt eco-friendly practices.'),
(45, 100, 'Podcast Series: Green Living Discussions', 'proj3.jpg', 'Starting a podcast series discussing topics related to environmental conservation and green living.'),
(46, 100, 'Blog: Sustainable Fashion Trends', 'proj4.jpg', 'Writing blog posts showcasing sustainable fashion brands and trends for conscious consumers.'),
(47, 100, 'Ebook: Beginner Guide to Zero Waste Living', 'proj5.jpg', 'Writing an ebook providing tips and resources for transitioning to a zero waste lifestyle.'),
(48, 100, 'YouTube Series: Healthy Cooking Made Easy', 'proj6.jpg', 'Creating cooking tutorials focusing on easy and nutritious recipes for health-conscious viewers.'),
(49, 100, 'TikTok Channel: Fitness Challenges', 'proj7.jpg', 'Starting a TikTok channel featuring fun fitness challenges to inspire followers to stay active.'),
(50, 100, 'Instagram Reels: Wellness Tips', 'proj8.jpg', 'Sharing short wellness tips and self-care routines through Instagram Reels to promote mental health.'),
(51, 100, 'Podcast: Mindfulness Meditation Sessions', 'proj9.jpg', 'Hosting guided meditation sessions on a podcast platform to help listeners cultivate mindfulness.'),
(52, 100, 'Blog: Healthy Lifestyle Inspirations', 'proj10.jpg', 'Curating blog content featuring stories and inspirations from individuals who have adopted a healthy lifestyle.'),
(53, 100, 'YouTube Vlogs: Urban Gardening Adventures', 'proj11.jpg', 'Documenting the journey of creating and maintaining urban gardens through engaging vlogs.'),
(54, 100, 'Instagram Reels: DIY Home Decor Ideas', 'proj12.jpg', 'Sharing creative DIY home decor projects and ideas through short and engaging Instagram Reels.'),
(55, 100, 'Podcast: Sustainable Living Interviews', 'proj13.jpg', 'Conducting interviews with experts and influencers in the sustainable living space for a podcast series.'),
(56, 100, 'Blog: Eco-Friendly Travel Guides', 'proj14.jpg', 'Writing travel guides highlighting eco-friendly destinations, accommodations, and activities for eco-conscious travelers.'),
(57, 125, 'Ebook: Plant-Based Recipes Cookbook', 'proj15.jpg', 'Compiling a collection of plant-based recipes into an ebook to encourage more people to adopt a plant-based diet.'),
(58, 126, 'YouTube Channel: Tech Reviews and Tutorials', 'proj16.jpg', 'Creating tech review videos and tutorials to help viewers make informed decisions about gadgets and devices.'),
(59, 126, 'Twitch Streaming: Gaming and Tech Discussions', 'proj17.jpg', 'Streaming live discussions on Twitch about gaming, tech news, and industry trends to engage with the community.'),
(60, 126, 'Instagram Live: Coding Workshops', 'proj18.jpg', 'Hosting live coding workshops on Instagram to teach coding basics and advanced techniques to aspiring developers.'),
(61, 126, 'Podcast: Future Tech Trends Analysis', 'proj19.jpg', 'Analyzing and discussing emerging technology trends and innovations in a podcast series for tech enthusiasts.'),
(62, 126, 'Blog: Tech Productivity Hacks and Tips', 'proj20.jpg', 'Sharing productivity hacks and tips for maximizing efficiency in tech-related tasks through blog posts.');

--
-- Indexes for dumped tables
--

--
-- Indexes for table `project`
--
ALTER TABLE `project`
  ADD PRIMARY KEY (`proj_id`);

--
-- AUTO_INCREMENT for dumped tables
--

--
-- AUTO_INCREMENT for table `project`
--
ALTER TABLE `project`
  MODIFY `proj_id` int(10) UNSIGNED NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=63;
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;

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
('102', '118', 'Tesla Campaign', 'In-progress'),
('102', '120', 'Brandify Charity Event', 'Review'),
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
  ADD PRIMARY KEY (`cc_id`,`brand_id`,`collab_title`);
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;


DROP DATABASE IF EXISTS blacklist;

CREATE DATABASE blacklist;

USE blacklist;

CREATE TABLE blacklist (
    account VARCHAR(100),
    banned_account VARCHAR(100),
    date TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    PRIMARY KEY (account, banned_account)
);



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

DROP DATABASE IF EXISTS `account`;
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
(100, 'john_doe', 'cc', 'John Doe', 'repurika@outlook.com', '100', 'user1.jpg', 'food,cars', 'sk_test_51OuGi52KwIS1b45LvlM5Q8z0AaTmdNohKDWk3pOEKhNbvOmHJmCEU9DWbSab871Yal3Qw5H2QMXDynjOuQC6NLXB00NBUhtZne'),
(101, 'brand_inc', 'brand', 'Brand Inc', 'repurika@outlook.com', '101', 'user2.jpg', 'sports,food', 'sk_test_51OuGi52KwIS1b45LvlM5Q8z0AaTmdNohKDWk3pOEKhNbvOmHJmCEU9DWbSab871Yal3Qw5H2QMXDynjOuQC6NLXB00NBUhtZne'),
(102, 'alex_jones', 'cc', 'Alex Jones', 'repurika@outlook.com', '102', 'user3.jpg', 'food,travel', 'sk_test_51OuGi52KwIS1b45LvlM5Q8z0AaTmdNohKDWk3pOEKhNbvOmHJmCEU9DWbSab871Yal3Qw5H2QMXDynjOuQC6NLXB00NBUhtZne'),
(103, 'brand_max', 'brand', 'Max Corporation', 'repurika@outlook.com', '103', 'user4.jpg', 'food,cars', 'sk_test_51OuGi52KwIS1b45LvlM5Q8z0AaTmdNohKDWk3pOEKhNbvOmHJmCEU9DWbSab871Yal3Qw5H2QMXDynjOuQC6NLXB00NBUhtZne'),
(104, 'michael_wilson', 'cc', 'Michael Wilson', 'repurika@outlook.com', '104', 'user5.jpg', 'technology,food', 'sk_test_51OuGi52KwIS1b45LvlM5Q8z0AaTmdNohKDWk3pOEKhNbvOmHJmCEU9DWbSab871Yal3Qw5H2QMXDynjOuQC6NLXB00NBUhtZne'),
(105, 'brand_media', 'brand', 'Media Enterprises', 'repurika@outlook.com', '105', 'user6.jpg', 'food,books', 'sk_test_51OuGi52KwIS1b45LvlM5Q8z0AaTmdNohKDWk3pOEKhNbvOmHJmCEU9DWbSab871Yal3Qw5H2QMXDynjOuQC6NLXB00NBUhtZne'),
(106, 'david_miller', 'cc', 'David Miller', 'repurika@outlook.com', '106', 'user7.jpg', 'food,cars', 'sk_test_51OuGi52KwIS1b45LvlM5Q8z0AaTmdNohKDWk3pOEKhNbvOmHJmCEU9DWbSab871Yal3Qw5H2QMXDynjOuQC6NLXB00NBUhtZne'),
(107, 'brandify', 'brand', 'Brandify', 'repurika@outlook.com', '107', 'user8.jpg', 'food,travel', 'sk_test_51OuGi52KwIS1b45LvlM5Q8z0AaTmdNohKDWk3pOEKhNbvOmHJmCEU9DWbSab871Yal3Qw5H2QMXDynjOuQC6NLXB00NBUhtZne'),
(108, 'chris_anderson', 'cc', 'Chris Anderson', 'repurika@outlook.com', '108', 'user9.jpg', 'movies,food', 'sk_test_51OuGi52KwIS1b45LvlM5Q8z0AaTmdNohKDWk3pOEKhNbvOmHJmCEU9DWbSab871Yal3Qw5H2QMXDynjOuQC6NLXB00NBUhtZne'),
(109, 'brand_tech', 'brand', 'Tech Solutions', 'repurika@outlook.com', '109', 'user10.jpg', 'food,shopping', 'sk_test_51OuGi52KwIS1b45LvlM5Q8z0AaTmdNohKDWk3pOEKhNbvOmHJmCEU9DWbSab871Yal3Qw5H2QMXDynjOuQC6NLXB00NBUhtZne'),
(110, 'paul_rodriguez', 'cc', 'Paul Rodriguez', 'repurika@outlook.com', '110', 'user11.jpg', 'food,technology', 'sk_test_51OuGi52KwIS1b45LvlM5Q8z0AaTmdNohKDWk3pOEKhNbvOmHJmCEU9DWbSab871Yal3Qw5H2QMXDynjOuQC6NLXB00NBUhtZne'),
(111, 'brand_co', 'brand', 'Co Enterprises', 'repurika@outlook.com', '111', 'user12.jpg', 'food,cars', 'sk_test_51OuGi52KwIS1b45LvlM5Q8z0AaTmdNohKDWk3pOEKhNbvOmHJmCEU9DWbSab871Yal3Qw5H2QMXDynjOuQC6NLXB00NBUhtZne'),
(112, 'kevin_garcia', 'cc', 'Kevin Garcia', 'repurika@outlook.com', '112', 'user13.jpg', 'music,food', 'sk_test_51OuGi52KwIS1b45LvlM5Q8z0AaTmdNohKDWk3pOEKhNbvOmHJmCEU9DWbSab871Yal3Qw5H2QMXDynjOuQC6NLXB00NBUhtZne'),
(113, 'acme_corp', 'brand', 'Acme Corporation', 'repurika@outlook.com', '113', 'user14.jpg', 'food,cars', 'sk_test_51OuGi52KwIS1b45LvlM5Q8z0AaTmdNohKDWk3pOEKhNbvOmHJmCEU9DWbSab871Yal3Qw5H2QMXDynjOuQC6NLXB00NBUhtZne'),
(114, 'tech_data', 'brand', 'Tech Data Corporation', 'repurika@outlook.com', '114', 'user15.jpg', 'sports,food', 'sk_test_51OuGi52KwIS1b45LvlM5Q8z0AaTmdNohKDWk3pOEKhNbvOmHJmCEU9DWbSab871Yal3Qw5H2QMXDynjOuQC6NLXB00NBUhtZne'),
(115, 'united_nations', 'brand', 'United Nations', 'repurika@outlook.com', '115', 'user16.jpg', 'food,travel', 'sk_test_51OuGi52KwIS1b45LvlM5Q8z0AaTmdNohKDWk3pOEKhNbvOmHJmCEU9DWbSab871Yal3Qw5H2QMXDynjOuQC6NLXB00NBUhtZne'),
(116, 'warner_media', 'brand', 'Warner Media', 'repurika@outlook.com', '116', 'user17.jpg', 'food,cars', 'sk_test_51OuGi52KwIS1b45LvlM5Q8z0AaTmdNohKDWk3pOEKhNbvOmHJmCEU9DWbSab871Yal3Qw5H2QMXDynjOuQC6NLXB00NBUhtZne'),
(117, 'starbucks', 'brand', 'Starbucks Corporation', 'repurika@outlook.com', '117', 'user18.jpg', 'technology,food', 'sk_test_51OuGi52KwIS1b45LvlM5Q8z0AaTmdNohKDWk3pOEKhNbvOmHJmCEU9DWbSab871Yal3Qw5H2QMXDynjOuQC6NLXB00NBUhtZne'),
(118, 'tesla', 'brand', 'Tesla, Inc.', 'repurika@outlook.com', '118', 'user19.jpg', 'food,books', 'sk_test_51OuGi52KwIS1b45LvlM5Q8z0AaTmdNohKDWk3pOEKhNbvOmHJmCEU9DWbSab871Yal3Qw5H2QMXDynjOuQC6NLXB00NBUhtZne'),
(119, 'amazon', 'brand', 'Amazon.com, Inc.', 'repurika@outlook.com', '119', 'user20.jpg', 'food,cars', 'sk_test_51OuGi52KwIS1b45LvlM5Q8z0AaTmdNohKDWk3pOEKhNbvOmHJmCEU9DWbSab871Yal3Qw5H2QMXDynjOuQC6NLXB00NBUhtZne'),
(120, 'nike', 'brand', 'Nike, Inc.', 'repurika@outlook.com', '120', 'user21.jpg', 'food,travel', 'sk_test_51OuGi52KwIS1b45LvlM5Q8z0AaTmdNohKDWk3pOEKhNbvOmHJmCEU9DWbSab871Yal3Qw5H2QMXDynjOuQC6NLXB00NBUhtZne'),
(121, 'microsoft', 'brand', 'Microsoft Corporation', 'repurika@outlook.com', '121', 'user22.jpg', 'movies,food', 'sk_test_51OuGi52KwIS1b45LvlM5Q8z0AaTmdNohKDWk3pOEKhNbvOmHJmCEU9DWbSab871Yal3Qw5H2QMXDynjOuQC6NLXB00NBUhtZne'),
(122, 'apple', 'brand', 'Apple Inc.', 'repurika@outlook.com', '122', 'user23.jpg', 'food,shopping', 'sk_test_51OuGi52KwIS1b45LvlM5Q8z0AaTmdNohKDWk3pOEKhNbvOmHJmCEU9DWbSab871Yal3Qw5H2QMXDynjOuQC6NLXB00NBUhtZne'),
(123, 'lucy_smith', 'cc', 'Lucy Smith', 'repurika@outlook.com', '123', 'user24.jpg', 'food,cars', 'sk_test_51OuGi52KwIS1b45LvlM5Q8z0AaTmdNohKDWk3pOEKhNbvOmHJmCEU9DWbSab871Yal3Qw5H2QMXDynjOuQC6NLXB00NBUhtZne'),
(124, 'james_johnson', 'cc', 'James Johnson', 'repurika@outlook.com', '124', 'user25.jpg', 'sports,food', 'sk_test_51OuGi52KwIS1b45LvlM5Q8z0AaTmdNohKDWk3pOEKhNbvOmHJmCEU9DWbSab871Yal3Qw5H2QMXDynjOuQC6NLXB00NBUhtZne'),
(125, 'sophia_williams', 'cc', 'Sophia Williams', 'repurika@outlook.com', '125', 'user26.jpg', 'food,travel', 'sk_test_51OuGi52KwIS1b45LvlM5Q8z0AaTmdNohKDWk3pOEKhNbvOmHJmCEU9DWbSab871Yal3Qw5H2QMXDynjOuQC6NLXB00NBUhtZne'),
(126, 'liam_brown', 'cc', 'Liam Brown', 'repurika@outlook.com', '126', 'user27.jpg', 'food,cars', 'sk_test_51OuGi52KwIS1b45LvlM5Q8z0AaTmdNohKDWk3pOEKhNbvOmHJmCEU9DWbSab871Yal3Qw5H2QMXDynjOuQC6NLXB00NBUhtZne'),
(127, 'olivia_jones', 'cc', 'Olivia Jones', 'repurika@outlook.com', '127', 'user28.jpg', 'technology,food', 'sk_test_51OuGi52KwIS1b45LvlM5Q8z0AaTmdNohKDWk3pOEKhNbvOmHJmCEU9DWbSab871Yal3Qw5H2QMXDynjOuQC6NLXB00NBUhtZne'),
(128, 'william_davis', 'cc', 'William Davis', 'repurika@outlook.com', '128', 'user29.jpg', 'food,books', 'sk_test_51OuGi52KwIS1b45LvlM5Q8z0AaTmdNohKDWk3pOEKhNbvOmHJmCEU9DWbSab871Yal3Qw5H2QMXDynjOuQC6NLXB00NBUhtZne'),
(129, 'emma_miller', 'cc', 'Emma Miller', 'repurika@outlook.com', '129', 'user30.jpg', 'food,cars', 'sk_test_51OuGi52KwIS1b45LvlM5Q8z0AaTmdNohKDWk3pOEKhNbvOmHJmCEU9DWbSab871Yal3Qw5H2QMXDynjOuQC6NLXB00NBUhtZne'),
(130, 'michael_jackson', 'cc', 'Michael Jackson', 'repurika@outlook.com', '130', 'user31.jpg', 'music,food', 'sk_test_51OuGi52KwIS1b45LvlM5Q8z0AaTmdNohKDWk3pOEKhNbvOmHJmCEU9DWbSab871Yal3Qw5H2QMXDynjOuQC6NLXB00NBUhtZne'),
(131, 'ava_taylor', 'cc', 'Ava Taylor', 'repurika@outlook.com', '131', 'user32.jpg', 'food,shopping', 'sk_test_51OuGi52KwIS1b45LvlM5Q8z0AaTmdNohKDWk3pOEKhNbvOmHJmCEU9DWbSab871Yal3Qw5H2QMXDynjOuQC6NLXB00NBUhtZne'),
(132, 'alexander_anderson', 'cc', 'Alexander Anderson', 'repurika@outlook.com', '132', 'user33.jpg', 'food,technology', 'sk_test_51OuGi52KwIS1b45LvlM5Q8z0AaTmdNohKDWk3pOEKhNbvOmHJmCEU9DWbSab871Yal3Qw5H2QMXDynjOuQC6NLXB00NBUhtZne');

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
